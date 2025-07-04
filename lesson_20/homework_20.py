import sqlite3

try:
    connection = sqlite3.connect('products.sqlite')
    print("✅ Connection to products.sqlite")

    cursor = connection.cursor()

    cursor.execute("ATTACH DATABASE 'categories.sqlite' AS cat")

    join = ''' SELECT 
        products.products_name,
        products.description,
        products.price,
        categories.category_name
            FROM "categories"
            INNER JOIN "products" ON "categories"."category_id" = "products"."category_id" '''

    cursor.execute(join)
    results = cursor.fetchall()

    for row in results:
        print(row)

except Exception as error:
    print(f"⚠️ Error creating DB\nError:{error}")

finally:
    if connection:
        cursor.close()
        connection.close()
        print("SQLITE3 connection is closed")