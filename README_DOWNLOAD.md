For this Python script, which is designed to generate plain URLs for files stored in an AWS S3 bucket and then save these URLs to a CSV file, a detailed and step-based documentation will be crucial for your clients to effectively utilize the tool. Here's a comprehensive guide that you can provide:

---

# Documentation for S3 URL Generator and CSV Exporter Application

## Overview

This application generates plain URLs for files stored within a specific folder of an AWS S3 bucket and exports these URLs, along with additional file and brand information, to a CSV file. It features a graphical user interface (GUI) for easy input of parameters such as brand name and keyword requirements.

## Prerequisites

Before using this application, ensure you have:

- Python installed on your system.
- `boto3`, `csv`, `environ`, `openpyxl`, and `tkinter` libraries installed. These can be installed through Python's pip package manager with the command `pip install boto3 python-dotenv openpyxl`.
- An active AWS account with access to an S3 bucket.
- AWS Access Key ID and AWS Secret Access Key with permissions to read from the specified S3 bucket.

## Configuration

1. **Environment Variables**: You must set up the required environment variables for AWS credentials and S3 bucket details. This can be done by creating a `.env` file in the script's directory with the following content:

   ```
   AWS_ACCESS_KEY_ID=your_access_key_id
   AWS_SECRET_ACCESS_KEY=your_secret_access_key
   REGION_NAME=your_region_name
   BUCKET_NAME=your_bucket_name
   ```

2. **AWS Permissions**: The AWS user whose credentials are being used needs to have permissions to list objects in the specified S3 bucket.

## Usage Guide

1. **Starting the Application**:
   - Execute the script with a Python interpreter to open the GUI.

2. **Inputting Parameters**:
   - **Brand Name**: Enter the name of the brand associated with the files in the S3 bucket. This will be used to generate the folder path (`brand_name/`) and as part of the exported CSV file's name.
   - **Keyword Acronym**: Specify whether a keyword acronym is necessary for the file naming convention. If "Yes" is selected, an additional input field for the acronym will be enabled.
   - **Acronym**: If keyword acronym is required, enter the specific acronym to be used in sorting the image position within the CSV file.

3. **Exporting URLs**:
   - After entering the parameters, click on the "Submit" button to start the process. The application will generate plain URLs for all files stored under the specified brand folder within the S3 bucket and export these URLs to a CSV file named after the brand. The CSV file will include columns for file name, brand number, part number, brand, URL, and sort order.

4. **CSV File**: 
   - The CSV file will be saved in the same directory as the script. It will be named `{brand_name}.csv` and can be used for further processing or integration with other systems.

## Troubleshooting

- **Authentication Errors**: Verify that the AWS credentials provided in the `.env` file are correct and have the necessary permissions.
- **No URLs Generated**: Ensure that the brand name is correctly entered and matches the folder structure in the S3 bucket. Also, check if there are files in the specified path.

## Support

For any issues or further assistance, please contact the support team at [your support email address].
