import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def load_data(file_path):
    """Loads the CSV file into a DataFrame."""
    return pd.read_csv(file_path)


def display_data_info(data):
    """Displays the data types and missing values of the dataframe."""
    print("Data Info:")
    print(data.info())  # Data types and missing values

def check_duplicates(data):
    """Checks for duplicates and prints the count."""
    num_duplicates = data.duplicated().sum()
    print(f"Number of duplicates: {num_duplicates}")


def check_null_values(df):
    """Checks for null values in the DataFrame and prints them."""
    null_values = df.isnull().sum()
    print(null_values)

def plot_category_distribution(df):
    """Plots the distribution of product categories."""
    plt.figure(figsize=(10, 6))
    sns.countplot(y='product_category', data=df, order=df['product_category'].value_counts().index)
    plt.title('Distribution of Product Categories')
    plt.show()

def plot_payment_type_distribution(df):
    """Plots the distribution of payment types."""
    plt.figure(figsize=(8, 4))
    sns.countplot(x='payment_type', data=df)
    plt.title('Distribution of Payment Types')
    plt.show()

def plot_price_distribution(df):
    """Plots the distribution of prices."""
    plt.figure(figsize=(8, 4))
    sns.histplot(df['price'], bins=50, kde=True)
    plt.title('Price Distribution')
    plt.show()

def plot_quantity_distribution(df):
    """Plots the distribution of quantities, including rogue values."""
    plt.figure(figsize=(8, 4))
    sns.histplot(df['qty'], bins=50, kde=True)
    plt.title('Quantity Distribution')
    plt.show()

def plot_payment_success_distribution(df):
    """Plots the count of successful vs failed payment transactions."""
    plt.figure(figsize=(8, 4))
    sns.countplot(x='payment_txn_success', data=df)
    plt.title('Payment Transaction Success vs Failure')
    plt.show()

def plot_failure_reason_distribution(df):
    """Plots the reasons for payment failure, considering failed transactions only."""
    plt.figure(figsize=(8, 4))
    sns.countplot(x='failure_reason', data=df[df['payment_txn_success'] == 'N'])
    plt.title('Reasons for Payment Failure')
    plt.show()

if __name__ == "__main__":
    # Load data
    file_path = r"C:\Users\krishna chaithanya\OneDrive\Desktop\Rev_Project2\EDA\Cleaned_data\ecommerce_cleansed_data.csv"
    df = load_data(file_path)
    display_data_info(df)
    check_duplicates(df)
    
    # Check for null values
    check_null_values(df)

    # Visualizations
    plot_category_distribution(df)
    plot_payment_type_distribution(df)
    plot_price_distribution(df)
    plot_quantity_distribution(df)
    plot_payment_success_distribution(df)
    plot_failure_reason_distribution(df)