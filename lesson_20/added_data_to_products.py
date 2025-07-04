import sqlite3
from faker import Faker
import random

list_of_country = ["USA", "Taiwan", "Japan", "Germany", "South Korea", "Austria", "China", "Switzerland", "Sweden"]

f = Faker()
fake_products_id = int(f.postcode())
fake_description = f.text(max_nb_chars=150)
fake_price = f.pyfloat(min_value=100, max_value=1000, right_digits=2)
fake_credit = random.choice([True, False])
fake_country_of_manufacture = random.choice(list_of_country)

try:
    connection = sqlite3.connect('products.sqlite')
    print("✅ DB was created")

    cursor = connection.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS "products" (
	products_id INTEGER PRIMARY KEY,
	products_name TEXT NOT NULL UNIQUE,
	category TEXT NOT NULL,
	category_id INTEGER NOT NULL,
	description TEXT NULL,
	price REAL NOT NULL,
	credit Boolean NOT NULL,
	country_of_manufacture TEXT NOT NULL,
    FOREIGN KEY (category_id) REFERENCES categories(category_id)
);
""")

    cursor.execute(f"""INSERT INTO "products"
    ("products_id", "products_name", "category", "category_id", "description", "price", "credit", "country_of_manufacture")
    VALUES ({fake_products_id},
    'HyperX Cloud II Headset', 
    'peripheral_devices', 
    26284,
    '{fake_description}', {fake_price}, {fake_credit}, '{fake_country_of_manufacture}')""")
    connection.commit()

    cursor.execute("""SELECT * from products""")
    print(cursor.fetchall())



except Exception as error:
    print(f"⚠️ Error creating DB\nError:{error}")

finally:
    if connection:
        cursor.close()
        connection.close()
        print("SQLITE3 connection is closed")