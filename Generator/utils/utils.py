from faker import Faker

# Create a Faker instance
fake = Faker()

# Product categories and types
product_categories = [
    'Fashion', 'Electronics', 'Books', 'Groceries', 
    'Fitness & Sports', 'Baby Products', 'Office Supplies', 
    'Garden & Outdoors', 'Home Appliances', 'Footwear'
]

product_names = {
    'Fashion': ['Jacket', 'Sneakers', 'Handbag', 'Sunglasses'],
    'Electronics': ['Smartphone', 'Smartwatch', 'Bluetooth Speaker', 'Headphones'],
    'Books': ['Fiction Novel', 'Non-Fiction', 'Comic Book', 'Textbook'],
    'Groceries': ['Organic Rice', 'Almond Milk', 'Olive Oil', 'Chia Seeds'],
    'Fitness & Sports': ['Dumbbells', 'Treadmill', 'Yoga Mat', 'Fitness Tracker'],
    'Baby Products': ['Baby Lotion', 'Diapers', 'Baby Monitor', 'Baby Bottles'],
    'Office Supplies': ['Stapler', 'Whiteboard', 'File Folders', 'Desk Chair'],
    'Garden & Outdoors': ['Lawn Mower', 'Watering Can', 'Garden Hose', 'Patio Furniture'],
    'Home Appliances': ['Washing Machine', 'Microwave', 'Refrigerator', 'Air Conditioner'],
    'Footwear': ['Running Shoes', 'Formal Shoes', 'Flip Flops', 'Boots']
}

# Countries and cities
countries = {
    'India': ['Hyderabad', 'Delhi', 'Bengaluru', 'Chennai', 'Mumbai'],
    'Australia': ['Sydney', 'Melbourne', 'Brisbane', 'Perth', 'Adelaide'],
    'Canada': ['Toronto', 'Vancouver', 'Montreal', 'Calgary', 'Ottawa'],
    'Japan': ['Tokyo', 'Osaka', 'Kyoto', 'Yokohama', 'Sapporo']
    
}

# Define multiple failure reasons
failure_reasons = [ 'Payment Declined', 'Insufficient Funds', 'Expired Card',  'Transaction Timeout']

# Payment types
payment = ['CreditCard', 'NetBanking', 'Wallet', 'UPI']

# E-commerce websites
sites = ['www.bestbuy.com', 'www.walmart.com', 'www.target.com', 'www.flipkart.com', 'www.shopify.com']
