import csv
import random
from utils.utils import fake, product_categories, product_names, countries, sites, payment, failure_reasons

def generate_data():
    """Creates a valid ecommerce data following the defined schema."""
    order_id = fake.random_number(digits=6)
    customer_id = fake.random_number(digits=6)
    customer_name = fake.name()
    product_id = fake.random_number(digits=6)
    product_category = random.choice(product_categories)
    product_name = random.choice(product_names[product_category])
    payment_type = fake.random_element(payment)  # Types:'CreditCard', 'NetBanking', 'Wallet', 'UPI'
    qty = random.randint(1, 100)
    price = round(random.uniform(10.0, 2000.0), 2)  # Price range between 10.0 and 2000.0
    datetime = fake.date_time_between(start_date='-1y', end_date='now').strftime("%Y-%m-%d %H:%M")
    country = random.choice(list(countries.keys()))
    city = random.choice(countries[country])
    ecommerce_website_name = random.choice(sites)
    payment_txn_id = fake.uuid4().split('-')[0]
    payment_txn_success = random.choice(['Y', 'N'])  # Y=Success, N=Failed
    failure_reason = "" if payment_txn_success == 'Y' else random.choice(failure_reasons)
 # Reason for payment failure
    
    return [
        order_id, customer_id, customer_name, product_id, product_name, product_category,
        payment_type, qty, price, datetime, country, city, ecommerce_website_name,
        payment_txn_id, payment_txn_success, failure_reason
    ]

def generate_rogue_data():
    """Creates a rogue ecommerce data with anomalies in 'payment_txn_success' and 'qty', while maintaining the validity of other fields."""
    
    # Rogue values for 'price' and 'qty'
   
    qty = random.randint(-100, -1)# Unreasonably high quantity
    payment_txn_success = random.choice(['Unknown', 'Error', 'Failure']) 
    # Other fields remain valid
    order_id = fake.random_number(digits=6)
    customer_id = fake.random_number(digits=6)
    customer_name = fake.name()
    product_id = fake.random_number(digits=6)
    product_category = random.choice(product_categories)
    product_name = random.choice(product_names[product_category])
    payment_type = fake.random_element(payment)
    datetime = fake.date_time_between(start_date='-1y', end_date='now').strftime("%Y-%m-%d %H:%M")
    country = random.choice(list(countries.keys()))
    price = round(random.uniform(100.0, 4000.0), 2) 
    city = random.choice(countries[country])
    ecommerce_website_name = random.choice(sites)
    payment_txn_id = fake.uuid4().split('-')[0]
    failure_reason = "" if payment_txn_success == 'Y' else random.choice(failure_reasons)
    
    return [
        order_id, customer_id, customer_name, product_id, product_name, product_category,
        payment_type, qty, price, datetime, country, city, ecommerce_website_name,
        payment_txn_id, payment_txn_success, failure_reason
    ]

def write_to_csv(num_records, rogue_percentage, file_name='ecommerce_raw_data.csv'):
    """Writes valid and rogue records to a CSV file according to the specified schema."""
    num_rogue_records = int(num_records * rogue_percentage)
    
    with open(file_name, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([
            'order_id', 'customer_id', 'customer_name', 'product_id', 'product_name', 'product_category', 
            'payment_type', 'qty', 'price', 'datetime', 'country', 'city', 'ecommerce_website_name', 
            'payment_txn_id', 'payment_txn_success', 'failure_reason'
        ])
        
        for _ in range(num_records):
            if random.random() < (num_rogue_records / num_records):
                record = generate_rogue_data()
            else:
                record = generate_data()
            
            writer.writerow(record)

# Example usage: generate 10000 records with 10% rogue records for 'payment_txn_success' and 'qty' columns
write_to_csv(num_records=10000, rogue_percentage=0.1)
