import pandas as pd

class DataCleaner:
    def __init__(self, input_file_path, output_file_path):
        self.input_file_path = input_file_path
        self.output_file_path = output_file_path
        self.df = None

    def load_data(self):
        """Load data from the CSV file."""
        self.df = pd.read_csv(self.input_file_path)

    def clean_data(self):
        """Perform data cleaning operations."""
        # 1. Change negative 'qty' values to positive
        self.df['qty'] = self.df['qty'].abs()

        # 2. Fill empty 'failure_reason' with 'Success'
        self.df['failure_reason'] = self.df['failure_reason'].fillna('Success')

        # 3. Change 'payment_txn_success' to 'N' if not 'Y'
        self.df['payment_txn_success'] = self.df['payment_txn_success'].apply(
            lambda x: 'Y' if x == 'Y' else 'N'
        )

    def save_data(self):
        """Save the cleansed data to a new CSV file."""
        self.df.to_csv(self.output_file_path, index=False)
        print(f"Cleansed data saved to {self.output_file_path}")

if __name__ == "__main__":
    # Specify the input and output file paths
    input_file_path = r"C:\Users\MrAKB\OneDrive\Desktop\Rev_Project2\ecommerce_raw_data.csv"
    output_file_path = r"C:\Users\MrAKB\OneDrive\Desktop\Rev_Project2\ecommerce_cleansed_data.csv"

    # Create an instance of DataCleaner
    cleaner = DataCleaner(input_file_path, output_file_path)

    # Execute the cleaning process
    cleaner.load_data()
    cleaner.clean_data()
    cleaner.save_data()
