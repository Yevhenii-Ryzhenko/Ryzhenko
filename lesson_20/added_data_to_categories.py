import sqlite3
from faker import Faker
import random

all_tax_groups = 'ABCDEF'
f = Faker()
fake_category_id = f.port_number()
fake_tax_group = random.choice(all_tax_groups)
fake_tax_percentage = random.randrange(0,100)
fake_responsible_person = f.name()

try:
    connection = sqlite3.connect('categories.sqlite')
    print("✅ DB was created")

    cursor = connection.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS "categories" (
	category_id INTEGER NOT NULL,
	category_name TEXT NOT NULL UNIQUE,
	tax_group TEXT NULL,
	tax_percentage INTEGER NULL,
	responsible_person TEXT NULL,
	CONSTRAINT user_pk PRIMARY KEY (category_id)
);
""")

    cursor.execute(f"""INSERT INTO "categories"
    ("category_id", "category_name", "tax_group", "tax_percentage", "responsible_person")
    VALUES ({fake_category_id}, 'peripheral_devices', '{fake_tax_group}', {fake_tax_percentage}, '{fake_responsible_person}')""")
    connection.commit()

    cursor.execute("""SELECT * from categories""")
    print(cursor.fetchall())

except Exception as error:
    print(f"⚠️ Error creating DB\nError:{error}")

finally:
    if connection:
        cursor.close()
        connection.close()
        print("SQLITE3 connection is closed")