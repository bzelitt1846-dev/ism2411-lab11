# Customers.py
# ISM2411
# Bryan Zelitt
# Module 11 Lab: Customer Dictionary & Lookup
# Reflection: 
# 1: Using .get() is a much faster and more concise way to access the values in a dictionary. 
# It also allows for a default value to be returned if the key does not exist.
# 2: It reminds you of excel because it is setup like a grid table with rows and columns. 
# It is useful because the data within it is significantly smaller then the data within an excel spreadsheet.

from dbm import error

print(" --- Exercise 1 --- ")
customer = {
    'name': 'Alice', # Key : Value,
    'Name': 'Not-Alice',
    'email': 'alice@example.com', 
    'tier': 'gold', # Strings
    'ytd_spend': 12400, # Numbers/Integers
}
print(customer['name'])
print(customer['email'])
print(customer['tier'])
print(customer['ytd_spend'])

print(" --- Exercise 2 --- ")
customer['phone'] = '555-5555' # Adding a new key-value pair to the dictionary
print(customer)
customer['tier'] = 'platinum' # Updating the value of an existing key
print(customer)
del customer['Name'] # Deleting a key-value pair from the dictionary
print(customer)

print(customer.get('ytd_spend', 0)) # This allows values to be blank without wasting time with an error

print(" --- Exercise 3 --- ")
print(customer.get("email", "No email on file"))

try:
    print(customer["email"])
except KeyError:
    print("KeyError caught: ", error)

print(" --- Exercise 4 --- ")
for key, value in customer.items():
    print(f"{key}: {value}")

for something in customer:
    print(something, customer[something])

print(" --- Exercise 5 --- ")
tier_discounts = {
    'bronze': 0,
    'silver': 0.05,
    'gold': 0.10,
    'platinum': 0.15
}

purchase = 200
discount_rate = tier_discounts.get(customer['tier'], 0)
final_price = purchase * (1 - discount_rate)
print(f"Tier: {customer['tier']}")
print(f"Discount Rate: {discount_rate * 100}%")
print(f"Final Price: ${final_price:.2f}")

print(" --- Exercise 6 --- ")
customers = [
    {"name": "Bob", "Tier": "silver", "ytd_spend": 3200},
    {"name": "Carol", "Tier": "gold", "ytd_spend": 8750},
    {"name": "David", "Tier": "bronze", "ytd_spend": 450},
]

for record in customers:
    rate = tier_discounts.get(record['Tier'], 0)
    discount = 300 * rate
    print(f"Customer: {record['name']}, Tier: {record['Tier']}, , Discount on $300 Purchase: ${discount:.2f}")

print(" --- Exercise 7 --- ")
catalong = {
    "Widget A": {"Price": 9.99, "stock": 150},
    "Widget C": {"Price": 49.99, "stock": 8},
}
for product_name, product_details in catalong.items():
    if product_details['stock'] < 10:
        print(f"Low Stock: {product_name} - only {product_details['stock']} left.")

print(" --- Exercise 8 --- ")
transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200},
]

sales_by_region = {}
for sale in transactions:
    region = sale['region']
    amount = sale['amount']
    sales_by_region[region] = sales_by_region.get(region, 0) + amount

print(sales_by_region)

for region in sorted(sales_by_region):
    print(f"{region}: ${sales_by_region[region]:.2f}")