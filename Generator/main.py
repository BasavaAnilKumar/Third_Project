# ecommerce_data_generator.py
from generator.data_generator import generate_data, generate_rogue_data, write_to_csv

if __name__ == "__main__":
    # Set the number of records
    num_records = 10000
    rogue_percentage = 0.1  # 10% rogue records
    
    # Call the function to write the data to a CSV file
    write_to_csv(num_records, rogue_percentage, 'ecommerce_raw_data.csv')
    
    print(f"{num_records} records have been generated with rogue records and saved to 'ecommerce_raw.csv'")

