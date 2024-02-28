import boto3
import csv
import environ
from openpyxl import load_workbook
from tkinter import Tk, filedialog, simpledialog, Label, Radiobutton, Entry, Button, StringVar

# Load environment variables
env = environ.Env()

# Environment variables for AWS
AWS_ACCESS_KEY_ID = env.str("AWS_ACCESS_KEY_ID", "")
AWS_SECRET_ACCESS_KEY = env.str("AWS_SECRET_ACCESS_KEY", "")
REGION_NAME = env.str("REGION_NAME", "")
BUCKET_NAME = env.str("BUCKET_NAME", "")

# Initialize the S3 client
s3 = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=REGION_NAME,
)

def generate_plain_urls(bucket_name, prefix):
    """Generate plain URLs for all files in a specific S3 folder with pagination."""
    plain_urls = []
    continuation_token = None

    while True:
        list_objects_v2_params = {
            'Bucket': bucket_name,
            'Prefix': prefix,
        }
        if continuation_token:
            list_objects_v2_params['ContinuationToken'] = continuation_token

        response = s3.list_objects_v2(**list_objects_v2_params)

        if 'Contents' in response:
            for obj in response['Contents']:
                # Construct the plain URL
                url = f"https://{bucket_name}.s3.amazonaws.com/{obj['Key']}"
                plain_urls.append((obj['Key'], url))

        if 'NextContinuationToken' in response:
            continuation_token = response['NextContinuationToken']
        else:
            break

    return plain_urls

def save_urls_to_csv(presigned_urls, brand_name, keyword_necessary, keyword):
    file_path = f'{brand_name}.csv'
    
    with open(file_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        header = ["File Name", "Brand Number", "Part Number", "Brand", "URL", "Sort Order"]
        writer.writerow(header)
        
        sort_order_tracker = {}
        temp_records = {}

        # Process each URL to categorize by part number
        for file_name, url in presigned_urls:
            file_name_cleaned = file_name.replace(f'{brand_name}/', '')
            part_number = file_name_cleaned.split('_')[1]
            brand_number = f"{file_name_cleaned.split('_')[0]}{part_number}"
            
            if part_number not in temp_records:
                temp_records[part_number] = []
            temp_records[part_number].append((file_name_cleaned, brand_number, url))
        
        # Process and sort each part number group with keyword and "main" consideration
        for part_number, records in temp_records.items():
            if keyword_necessary == "YES":
                # Prioritize by keyword or "main", then by file name
                records.sort(key=lambda x: (
                    keyword.lower() not in x[0].lower() and "main" not in x[0].lower(),
                    x[0]
                ))
            else:
                # Sort by file name if no keyword necessary
                records.sort(key=lambda x: x[0])

            # Assign sort order and write rows
            for idx, (file_name_cleaned, brand_number, url) in enumerate(records, start=1):
                writer.writerow([file_name_cleaned, brand_number, part_number, brand_name, url, idx])

def create_ui():
    def submit_action():
        brand_name = brand_name_var.get()
        keyword_necessary = keyword_necessary_var.get()
        keyword = keyword_var.get() if keyword_necessary == "YES" else None

        if brand_name:
            s3_folder_path = f'{brand_name}/'
            presigned_urls = generate_plain_urls(BUCKET_NAME, s3_folder_path)
            save_urls_to_csv(presigned_urls, brand_name, keyword_necessary, keyword)
            print(f"Pre-signed URLs have been saved to {brand_name}.csv")
        else:
            print("No brand name was provided.")

    def keyword_entry_state():
        if keyword_necessary_var.get() == "YES":
            keyword_entry.config(state='normal')
        else:
            keyword_entry.config(state='disabled')
    
    root = Tk()
    root.title("Download")
    root.geometry("250x320")  # Adjust window size if needed

    keyword_necessary_var = StringVar(value="YES")
    brand_name_var = StringVar()
    keyword_var = StringVar()

    font_settings = ("Arial", 12)  # Example font settings for larger UI elements

    Label(root, text="Brand Name:", font=font_settings).pack(pady=(10, 0))
    Entry(root, textvariable=brand_name_var, font=font_settings).pack(pady=10)

    Label(root, text="Is keyword acronym?", font=font_settings).pack(pady=(10, 0))
    Radiobutton(root, text="Yes", variable=keyword_necessary_var, value="YES", command=keyword_entry_state, font=font_settings).pack(pady=2)
    Radiobutton(root, text="No", variable=keyword_necessary_var, value="NO", command=keyword_entry_state, font=font_settings).pack(pady=2)

    Label(root, text="Acronym:", font=font_settings).pack(pady=(10, 0))
    keyword_entry = Entry(root, textvariable=keyword_var, state='normal', font=font_settings)
    keyword_entry.pack(pady=10)

    Button(root, text="Submit", command=submit_action, font=font_settings).pack(pady=(10, 0))

    root.mainloop()

if __name__ == "__main__":
    create_ui()