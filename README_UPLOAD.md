Creating a detailed and step-by-step documentation for your script will help your clients understand how to use it effectively. Here is a structured guide that you can provide to them:

---

# Documentation for Image Upload Application

## Overview

This application facilitates the process of uploading images contained within ZIP files to an AWS S3 bucket. It allows users to select ZIP files or a folder containing ZIP files through a graphical user interface (GUI), extracts the images, and uploads them to a specified S3 bucket under a brand-specific folder.

## Prerequisites

Before using this application, please ensure you have the following:

- Python installed on your system.
- `boto3`, `tkinter`, `zipfile`, `io`, `environ`, and `shutil` libraries installed. You can install these dependencies using the command `pip install boto3 python-dotenv`.
- An AWS account and an S3 bucket where the images will be uploaded.
- AWS Access Key ID, AWS Secret Access Key, and the S3 Bucket Name.

## Configuration

1. **Environment Variables**: Set up the required environment variables for AWS credentials and S3 bucket details. You can do this by creating a `.env` file in the same directory as the script with the following contents:

   ```
   AWS_ACCESS_KEY_ID=your_access_key_id
   AWS_SECRET_ACCESS_KEY=your_secret_access_key
   REGION_NAME=your_region_name
   BUCKET_NAME=your_bucket_name
   ```

2. **AWS Permissions**: Ensure the AWS user whose credentials are used has sufficient permissions to upload files to the specified S3 bucket.

## Usage Guide

1. **Starting the Application**:
   - Run the script using a Python interpreter. This will open the graphical user interface.

2. **Selecting ZIP Files**:
   - Click on the "Select ZIP Files" button to open a file dialog. Navigate to the location of your ZIP files, select them, and click "Open". You can select multiple ZIP files by holding down the `Ctrl` key while clicking.
   - Alternatively, you can click on the "Select Folder" button to select a folder. The application will automatically find all ZIP files within the selected folder.

3. **Entering the Brand Name**:
   - In the "Brand Name" entry field, type the name of the brand for which you are uploading images. This name will be used to create a brand-specific folder in your S3 bucket.

4. **Uploading Images**:
   - Click on the "Submit" button to start the extraction and upload process. The application will first extract images from the selected ZIP files, then upload them to your S3 bucket, organized under the specified brand folder.

5. **Completion**:
   - Once the upload process is complete, the application will display a message indicating successful upload. If there were any errors during the process, error messages would be displayed.

## Notes

- The application currently supports `.png`, `.jpg`, `.jpeg`, `.gif`, and `.bmp` image formats.
- Ensure the AWS credentials provided have the necessary permissions to perform upload operations in the specified S3 bucket.

## Troubleshooting

- **Authentication Errors**: Check if the AWS credentials in the `.env` file are correct and have the necessary permissions.
- **No ZIP Files Found**: Ensure you've selected the correct folder or ZIP files and that the ZIP files contain supported image formats.

## Contact Support

For any issues or inquiries, please contact the support team at [your support email].

---
