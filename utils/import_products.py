import pandas as pd
from db.database import get_db_connection

def import_csv_data():
    csv_file = "skincare_products_clean.csv"
    df = pd.read_csv(csv_file)

    connection= get_db_connection()

    cursor = connection.cursor()
    
    cursor.execute("""
    IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='Products' AND xtype='U')
    BEGIN
    CREATE TABLE Products (
        product_name NVARCHAR(255),
            product_url NVARCHAR(500),
            product_type NVARCHAR(100),
            clean_ingreds NVARCHAR(MAX)
        )
    END
    """)
    connection.commit()
    
    cursor.execute("SELECT COUNT(*) FROM Products")
    count = cursor.fetchone()[0]
    
    if count > 0:
        print("Data already exists in the Products table. Skipping CSV import.")
    else:
        for index, row in df.iterrows():
            cursor.execute("""
            INSERT INTO Products (product_name, product_url, product_type, clean_ingreds) 
            VALUES (?, ?, ?, ?)
            """, 
            row['product_name'], 
            row['product_url'], 
            row['product_type'], 
            row['clean_ingreds'])
            
        connection.commit()
        print("Data imported successfully!")

    cursor.close()
    connection.close()

        