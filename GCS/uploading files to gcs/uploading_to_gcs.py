from google.cloud import storage
from google.oauth2 import service_account

class GCSUploader:
    def __init__(self, bucket_name, key_path):
        """Initializes the uploader with the specified bucket and credentials."""
        self.bucket_name = bucket_name
        self.key_path = key_path
        self.credentials = service_account.Credentials.from_service_account_file(key_path)
        self.storage_client = storage.Client(credentials=self.credentials)
        self.bucket = self.storage_client.bucket(bucket_name)

    def upload_csv(self, source_file_name, destination_blob_name, folder_name=None):
        """Uploads a CSV file to the specified folder in the GCS bucket."""
        try:
            # Create the destination path, including the folder if provided
            if folder_name:
                destination_blob_name = f"{folder_name}/{destination_blob_name}"

            # Get the blob and upload the file
            blob = self.bucket.blob(destination_blob_name)
            blob.upload_from_filename(source_file_name)

            print(f"File {source_file_name} uploaded to {self.bucket_name}/{destination_blob_name}.")
        
        except Exception as e:
            print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    # Initialize uploader for the first file
    bucket_name = "rev_pro2anil"
    key_path = r"C:\Service accounts\trans-parsec-433112-p7-1089350c80d6.json"
    uploader = GCSUploader(bucket_name, key_path)

    # Upload first CSV file
    source_file_name = r"C:\Users\MrAKB\OneDrive\Desktop\Rev_Project2\ecommerce_raw_data.csv"  # File to upload
    destination_blob_name = "ecommerce_raw_data.csv"
    folder_name = "gendata"
    uploader.upload_csv(source_file_name, destination_blob_name, folder_name)

    # Upload second CSV file
    source_file_name = r"C:\Users\MrAKB\OneDrive\Desktop\Rev_Project2\ecommerce_cleansed_data.csv"  
    destination_blob_name = "cleaned_ecom_data.csv"
    folder_name = "cleandata"
    uploader.upload_csv(source_file_name, destination_blob_name, folder_name)