import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

class EcommerceDataAnalyzer:
    def __init__(self, file_path):
        """Initializes the class and loads the data from the specified file path."""
        self.file_path = file_path
        self.data = self.load_data()

    def load_data(self):
        """Loads the CSV file into a DataFrame."""
        return pd.read_csv(self.file_path)

    def display_data_info(self):
        """Displays the data types and missing values of the dataframe."""
        print("Data Info:")
        print(self.data.info())  # Data types and missing values

    def check_duplicates(self):
        """Checks for duplicates and prints the count."""
        num_duplicates = self.data.duplicated().sum()
        print(f"Number of duplicates: {num_duplicates}")

    def check_null_values(self):
        """Checks for null values in the DataFrame and prints them."""
        null_values = self.data.isnull().sum()
        print("Null Values:")
        print(null_values)

    def plot_category_distribution(self):
        """Plots the distribution of product categories."""
        plt.figure(figsize=(8, 4))
        sns.countplot(y='product_category', data=self.data, order=self.data['product_category'].value_counts().index)
        plt.title('Distribution of Product Categories')
        plt.show()

    def plot_payment_type_distribution(self):
        """Plots the distribution of payment types."""
        plt.figure(figsize=(8, 4))
        sns.countplot(x='payment_type', data=self.data)
        plt.title('Distribution of Payment Types')
        plt.show()

    def plot_price_distribution(self):
        """Plots the distribution of prices."""
        plt.figure(figsize=(8, 4))
        sns.histplot(self.data['price'], bins=50, kde=True)
        plt.title('Price Distribution')
        plt.show()

    def plot_quantity_distribution(self):
        """Plots the distribution of quantities, including rogue values."""
        plt.figure(figsize=(8, 4))
        sns.histplot(self.data['qty'], bins=50, kde=True)
        plt.title('Quantity Distribution')
        plt.show()

    def plot_payment_success_distribution(self):
        """Plots the count of successful vs failed payment transactions."""
        plt.figure(figsize=(8, 4))
        sns.countplot(x='payment_txn_success', data=self.data)
        plt.title('Payment Transaction Success vs Failure')
        plt.show()

    def plot_failure_reason_distribution(self):
        """Plots the reasons for payment failure, considering failed transactions only."""
        plt.figure(figsize=(8, 4))
        sns.countplot(x='failure_reason', data=self.data[self.data['payment_txn_success'] == 'N'])
        plt.title('Reasons for Payment Failure')
        plt.show()

if __name__ == "__main__":
    # Load data
    file_path = r"C:\Users\MrAKB\OneDrive\Desktop\Rev_Project2\ecommerce_raw_data.csv"
    analyzer = EcommerceDataAnalyzer(file_path)
    
    # Perform analysis
    analyzer.display_data_info()
    analyzer.check_duplicates()
    analyzer.check_null_values()
    
    # Visualizations
    analyzer.plot_category_distribution()
    analyzer.plot_payment_type_distribution()
    analyzer.plot_price_distribution()
    analyzer.plot_quantity_distribution()
    analyzer.plot_payment_success_distribution()
    analyzer.plot_failure_reason_distribution()
