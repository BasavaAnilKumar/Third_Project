import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load the data
df = pd.read_csv(r"C:\Users\krishna chaithanya\OneDrive\Desktop\Rev_Project2\EDA\Cleaned_data\ecommerce_cleansed_data.csv")

# Display the first few rows
df.head()

# Check for null values in all columns
null_values = df.isnull().sum()

# Display the null values for all columns
print(null_values)

# Distribution of product categories
plt.figure(figsize=(10, 6))
sns.countplot(y='product_category', data=df, order=df['product_category'].value_counts().index)
plt.title('Distribution of Product Categories')
plt.show()

# Distribution of payment types
plt.figure(figsize=(8, 4))
sns.countplot(x='payment_type', data=df)
plt.title('Distribution of Payment Types')
plt.show()

# Distribution of prices
plt.figure(figsize=(8, 4))
sns.histplot(df['price'], bins=50, kde=True)
plt.title('Price Distribution')
plt.show()

# Distribution of quantity (including rogue values)
plt.figure(figsize=(8, 4))
sns.histplot(df['qty'], bins=50, kde=True)
plt.title('Quantity Distribution')
plt.show()

# Countplot for 'payment_txn_success'
plt.figure(figsize=(8, 4))
sns.countplot(x='payment_txn_success', data=df)
plt.title('Payment Transaction Success vs Failure')
plt.show()

# Countplot for 'failure_reason' (for failed transactions)
plt.figure(figsize=(8, 4))
sns.countplot(x='failure_reason', data=df[df['payment_txn_success'] == 'N'])
plt.title('Reasons for Payment Failure')
plt.show()