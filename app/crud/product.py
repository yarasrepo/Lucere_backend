from db.database import get_db_connection

def get_all_products():
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT product_name, product_url, product_type, clean_ingreds FROM Products")
    rows = cursor.fetchall()
    
    products = []
    for row in rows:
        product = {
            "product_name": row[0],
            "product_url": row[1],
            "product_type": row[2],
            "clean_ingreds": row[3]
        }
        products.append(product)

    cursor.close()
    connection.close()

    return {"products": products}

def get_product_by_ingredient(product_ingr: str):
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute("""
    SELECT product_name, product_url, product_type
    FROM Products 
    WHERE clean_ingreds LIKE ? 
    """, 
    (f"%{product_ingr}%",))
    products = cursor.fetchall()
    
    products_list = [
        {"product_name": product[0], "product_url": product[1], "product_type": product[2]}
        for product in products
    ]

    cursor.close()
    connection.close()

    return products_list