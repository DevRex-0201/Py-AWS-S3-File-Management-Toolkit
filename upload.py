import boto3
import os
from tkinter import Tk, Label, Entry, Button, filedialog
import zipfile
import io
import environ
import shutil

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


selected_zip_files = []  # Global variable to store selected ZIP files

def upload_to_s3(local_file_path, s3_key, bucket_name=BUCKET_NAME):
    try:
        # Upload file to S3 bucket
        s3.upload_file(local_file_path, bucket_name, s3_key)
        print(f"File uploaded successfully to S3 with key: {s3_key}")
    except Exception as e:
        print(f"Error uploading file to S3: {e}")

def extract_images(zip_files, brand_folder):
    # Ensure the brand folder exists
    if not os.path.exists(brand_folder):
        os.makedirs(brand_folder)
    
    # Extract image files from each ZIP file
    for zip_file in zip_files:
        with zipfile.ZipFile(zip_file, 'r') as zip_ref:
            for file_info in zip_ref.infolist():
                if file_info.filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                    with zip_ref.open(file_info) as file:
                        out_path = os.path.join(brand_folder, os.path.basename(file_info.filename))
                        with open(out_path, 'wb') as out_file:
                            shutil.copyfileobj(file, out_file)

def upload_images(brand_folder):
    # Upload all image files in the brand folder to S3
    for root, dirs, files in os.walk(brand_folder):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                local_file_path = os.path.join(root, file)
                s3_key = f"{brand_folder}/{file}"
                upload_to_s3(local_file_path, s3_key)

def select_files():
    global selected_zip_files
    selected_zip_files = filedialog.askopenfilenames(filetypes=[('ZIP files', '*.zip')])
    if not selected_zip_files:
        print("No ZIP files selected.")

def select_folder():
    global selected_zip_files
    folder_path = filedialog.askdirectory()
    if folder_path:
        selected_zip_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.zip')]
    if not selected_zip_files:
        print("No ZIP files found in the selected folder.")

def submit(s3_folder_entry):
    brand_folder = s3_folder_entry.get()  # Get Brand folder name from entry widget
    if selected_zip_files and brand_folder:
        # First, extract all images
        extract_images(selected_zip_files, brand_folder)
        # Then, upload all extracted images
        upload_images(brand_folder)
        print("All images have been uploaded successfully.")
    else:
        print("No ZIP files selected or Brand folder name is empty.")

def create_ui():
    root = Tk()
    root.title("Upload")
    root.geometry("250x240")  # Adjusted Width x Height for additional button
    font_settings = ("Arial", 12)  # Example font settings for larger UI elements
    
    Label(root, text="Brand Name:", font=font_settings).pack(pady=(10, 0))
    s3_folder_entry = Entry(root, font=font_settings)
    s3_folder_entry.pack(pady=5)

    browse_button = Button(root, text="Select ZIP Files", font=font_settings, command=select_files)
    browse_button.pack(pady=10)  # Adjust padding for layout

    folder_button = Button(root, text="Select Folder", font=font_settings, command=select_folder)
    folder_button.pack(pady=10)  # Button for selecting folder

    submit_button = Button(root, text="Submit", font=font_settings, command=lambda: submit(s3_folder_entry))
    submit_button.pack(pady=10)  # Adjust padding for layout

    root.mainloop()

# Call the function to create UI and start the application
create_ui()