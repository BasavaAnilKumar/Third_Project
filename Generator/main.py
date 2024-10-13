# ecommerce_data_generator.py
from generator.data_generator import generate_data, generate_rogue_data, write_to_csv

class DataGeneratorApp:
    def __init__(self):
        self.num_records = 0
        self.rogue_percentage = 0.0

    def get_user_inputs(self):
        self.num_records = int(input("Enter the number of records to generate: "))
        self.rogue_percentage = float(input("Enter the percentage of rogue records (e.g., 0.1 for 10%): "))

    def generate_data(self):
        write_to_csv(self.num_records, self.rogue_percentage, 'ecommerce_raw_data.csv')
        print(f"{self.num_records} records have been generated with {self.rogue_percentage * 100}% rogue records and saved to 'ecommerce_raw_data.csv'")

if __name__ == "__main__":
    try:
        app = DataGeneratorApp()  # Create an instance of DataGeneratorApp
        app.get_user_inputs()     # Get user inputs
        app.generate_data()       # Generate the data
    except ValueError:
        print("Please enter valid numbers for records and rogue percentage.")
