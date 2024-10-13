import os
from google.cloud import storage

class GCSBucketManager:
    def __init__(self, json_key_path):
        """Initializes the manager and sets Google application credentials."""
        self.json_key_path = json_key_path
        self.set_google_application_credentials()

    def set_google_application_credentials(self):
        """Sets the environment variable for Google Application Credentials."""
        if not os.path.exists(self.json_key_path):
            raise FileNotFoundError(f"Service account key file '{self.json_key_path}' not found.")
        
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = self.json_key_path
        print(f"Google application credentials set to: {self.json_key_path}")

    def create_bucket_and_folders(self, bucket_name, folders):
        """Creates a GCS bucket and multiple folders."""
        try:
            # Initialize a GCS client
            storage_client = storage.Client()  # Will use the credentials set in the environment variable
        except Exception as e:
            print(f"Error initializing GCS client: {e}")
            return

        # Create the bucket
        try:
            bucket = storage_client.create_bucket(bucket_name)  # Creates the bucket
            print(f"Bucket '{bucket.name}' created.")
        except Exception as e:
            print(f"Error creating bucket: {e}")
            return

        # Create folders
        for folder in folders:
            blob = bucket.blob(f"{folder}/")  # Append a slash to create a "folder"
            try:
                blob.upload_from_string('')  # Upload an empty string to create the folder
                print(f"Folder '{folder}' created in bucket '{bucket.name}'.")
            except Exception as e:
                print(f"Error creating folder '{folder}': {e}")

if __name__ == "__main__":
    try:
        # Set the path to your service account key JSON
        json_key_path = r"C:\Service accounts\trans-parsec-433112-p7-1089350c80d6.json"
        
        # Initialize GCSBucketManager
        gcs_manager = GCSBucketManager(json_key_path)

        # Configuration
        bucket_name = "rev_pro2anil"  # Replace with your desired bucket name
        folders_to_create = ["gendata", "cleandata"]

        # Create the bucket and folders
        gcs_manager.create_bucket_and_folders(bucket_name, folders_to_create)

    except FileNotFoundError as fnf_error:
        print(f"Error: {fnf_error}")
    except Exception as e:
        print(f"Error occurred: {str(e)}")