import sqlite3
import random
import string

conn = sqlite3.connect('identifier.sqlite')
cursor = conn.cursor()

for i in range(1000000):
    product_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
    category = random.choice(['Sneakers', 'Boots', 'Sandals', 'Heels', 'Flats', 'Loafers'])
    price = round(random.uniform(20.0, 200.0), 2)
    country = random.choice(['USA', 'China', 'Germany', 'Russia'])
    brand = random.choice(
        ['Nike', 'Adidas', 'Puma', 'Reebok', 'Converse', 'Vans', 'New Balance', 'Timberland', 'Skechers',
         'Dr. Martens'])

    material = random.choice(['Cotton', 'Leather', 'Plastic', 'Synthetic', 'Rubber', 'Denim', 'Canvas'])
    quantity = random.randint(0, 100)

    cursor.execute('''
        INSERT INTO Products (product_name, category, price, country, brand, material, quantity)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (product_name, category, price, country, brand, material, quantity))


for i in range(1000000):
    product_id = random.randint(1, 1000000)
    color = ''.join(random.choices(string.ascii_lowercase, k=5))

    cursor.execute('''
        INSERT INTO Colors (product_id, color)
        VALUES (?, ?)
    ''', (product_id, color))

for i in range(1000000):
    product_id = random.randint(1, 1000000)
    size = random.choice([1.5, 2.0, 3.5, 4.0, 5.5, 6.0, 7.5, 8.0, 9.5, 9.0])

    cursor.execute('''
        INSERT INTO Sizes (product_id, size)
        VALUES (?, ?)
    ''', (product_id, size))

for i in range(1000000):
    first_name = ''.join(random.choices(string.ascii_uppercase, k=6))
    last_name = ''.join(random.choices(string.ascii_uppercase, k=8))
    email = f"{first_name.lower()}.{last_name.lower()}@main.ru"
    phone = ''.join(random.choices(string.digits, k=10))

    cursor.execute('''
        INSERT INTO Customers (first_name, last_name, email, phone)
        VALUES (?, ?, ?, ?)
    ''', (first_name, last_name, email, phone))

for i in range(1000000):
    customer_id = random.randint(1, 1000000)
    order_date = f"2023-01-{random.randint(1, 31)}"

    cursor.execute('''
        INSERT INTO Orders (customer_id, order_date)
        VALUES (?, ?)
    ''', (customer_id, order_date))

for i in range(1000000):
    order_id = random.randint(1, 1000000)
    product_id = random.randint(1, 1000000)

    cursor.execute('''
        INSERT INTO OrderDetails (order_id, product_id)
        VALUES (?, ?)
    ''', (order_id, product_id))


conn.commit()
conn.close()
