import sqlite3
import os
from datetime import datetime, timedelta
import random

# -----------------------
# PATH SETUP
# -----------------------
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DB_PATH = os.path.join(BASE_DIR, "data", "sales.db")

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# -----------------------
# DROP TABLES (RESET CLEANLY)
# -----------------------
cursor.execute("DROP TABLE IF EXISTS customers")
cursor.execute("DROP TABLE IF EXISTS products")
cursor.execute("DROP TABLE IF EXISTS orders")
cursor.execute("DROP TABLE IF EXISTS order_items")

# -----------------------
# CREATE TABLES
# -----------------------
cursor.execute("""
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    region TEXT
)
""")

cursor.execute("""
CREATE TABLE products (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_name TEXT,
    category TEXT,
    price REAL
)
""")

cursor.execute("""
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER,
    order_date TEXT,
    total_amount REAL
)
""")

cursor.execute("""
CREATE TABLE order_items (
    order_item_id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER,
    product_id INTEGER,
    quantity INTEGER,
    subtotal REAL
)
""")

# -----------------------
# SAMPLE DATA
# -----------------------
customers = [
    ("John Doe", "North"),
    ("Jane Smith", "South"),
    ("Michael Brown", "East"),
    ("Sarah Wilson", "West"),
]

products = [
    ("Laptop", "Electronics", 1200),
    ("Phone", "Electronics", 800),
    ("Headphones", "Electronics", 150),
    ("Shoes", "Fashion", 100),
]

# Insert customers
cursor.executemany(
    "INSERT INTO customers (name, region) VALUES (?, ?)",
    customers
)

# Insert products
cursor.executemany(
    "INSERT INTO products (product_name, category, price) VALUES (?, ?, ?)",
    products
)

# -----------------------
# GENERATE ORDERS
# -----------------------
for _ in range(30):
    customer_id = random.randint(1, len(customers))
    order_date = (datetime.now() - timedelta(days=random.randint(0, 60))).strftime("%Y-%m-%d")

    cursor.execute(
        "INSERT INTO orders (customer_id, order_date, total_amount) VALUES (?, ?, ?)",
        (customer_id, order_date, 0)
    )

    order_id = cursor.lastrowid

    total = 0

    for _ in range(random.randint(1, 3)):
        product_id = random.randint(1, len(products))
        quantity = random.randint(1, 3)

        cursor.execute("SELECT price FROM products WHERE product_id=?", (product_id,))
        price = cursor.fetchone()[0]

        subtotal = price * quantity
        total += subtotal

        cursor.execute(
            "INSERT INTO order_items (order_id, product_id, quantity, subtotal) VALUES (?, ?, ?, ?)",
            (order_id, product_id, quantity, subtotal)
        )

    cursor.execute(
        "UPDATE orders SET total_amount=? WHERE order_id=?",
        (total, order_id)
    )

conn.commit()
conn.close()

print("✅ Database created and seeded successfully!")