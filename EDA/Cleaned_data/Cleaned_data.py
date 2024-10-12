import pandas as pd

# Load the CSV file
df = pd.read_csv(r"C:\Users\krishna chaithanya\OneDrive\Desktop\Rev_Project2\Generator\ecommerce_raw_data.csv")

# 1. Change negative 'qty' values to positive
df['qty'] = df['qty'].abs()

# 2. Fill empty 'failure_reason' with 'Success'
df['failure_reason'] = df['failure_reason'].fillna('Success')

# 3. Change 'payment_txn_success' to 'N' if not 'Y'
df['payment_txn_success'] = df['payment_txn_success'].apply(lambda x: 'Y' if x == 'Y' else 'N')

# Save the cleansed data back to a new CSV file
df.to_csv('ecommerce_cleansed_data.csv', index=False)

print("Data cleansing completed and saved to 'ecommerce_cleansed_data.csv'.")
