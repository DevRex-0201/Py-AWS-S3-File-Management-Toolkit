Creating a unified README document for both the upload and download scripts will streamline the process for your users, offering a comprehensive guide on how to use both tools effectively. Below is a suggested format for such a document.

---

# AWS S3 File Management Toolkit

## Overview

This toolkit provides two main functionalities: uploading images contained within ZIP files to an AWS S3 bucket (Upload Script) and generating plain URLs for files stored within a specific folder of an AWS S3 bucket, exporting these URLs to a CSV file (Download Script). Designed with a user-friendly graphical interface, this toolkit simplifies the process of managing files in an S3 bucket.

## Prerequisites

Before using this toolkit, ensure you have:

- Python installed on your system.
- The following Python libraries installed: `boto3`, `tkinter`, `zipfile`, `io`, `environ`, `shutil`, `csv`, `openpyxl`. You can install these dependencies using the command: `pip install boto3 python-dotenv openpyxl`.
- An AWS account with an S3 bucket set up.
- AWS Access Key ID and AWS Secret Access Key with permissions for the required operations on the S3 bucket.

## Configuration

### Environment Variables

Set up the required environment variables for AWS credentials and S3 bucket details by creating a `.env` file in the same directory as the scripts with the following contents:

```plaintext
AWS_ACCESS_KEY_ID=your_access_key_id
AWS_SECRET_ACCESS_KEY=your_secret_access_key
REGION_NAME=your_region_name
BUCKET_NAME=your_bucket_name
```

### AWS Permissions

The AWS user whose credentials are being used needs to have permissions to upload files to and list objects in the specified S3 bucket.

## Usage

### Uploading Images to S3 (Upload Script)

1. **Starting the Application**: Run the upload script using Python. This opens the graphical user interface (GUI).
2. **Selecting ZIP Files or Folder**: Use the GUI to select ZIP files directly or a folder containing ZIP files for uploading.
3. **Entering Brand Name**: Input the brand name associated with the images. This name will be used to organize the images in the S3 bucket.
4. **Uploading Images**: Click on the "Submit" button to start the upload process. The script will extract images from the ZIP files and upload them to the specified brand folder in the S3 bucket.

### Generating and Exporting URLs to CSV (Download Script)

1. **Starting the Application**: Run the download script using Python to open the GUI.
2. **Inputting Parameters**: Provide the necessary information, including the brand name and whether a keyword acronym is needed. If required, specify the acronym.
3. **Exporting URLs**: Click "Submit" to generate and export the URLs. The script retrieves all files under the specified brand folder in the S3 bucket and exports the URLs, along with additional file information, to a CSV file.

## Troubleshooting

- **Authentication Errors**: Verify the AWS credentials in the `.env` file.
- **Upload Errors**: Ensure the ZIP files contain supported image formats and that the AWS user has upload permissions.
- **Download Errors**: Check that the brand name matches the folder structure in the S3 bucket and that the AWS user has permissions to list objects.

## Support

For any issues or further assistance, please contact the support team at [your support email address].

---
