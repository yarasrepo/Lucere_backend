from dotenv import load_dotenv
import os
import pyodbc

load_dotenv()

def get_db_connection():
    driver = os.getenv("DB_DRIVER")
    server = os.getenv("DB_SERVER")
    database = os.getenv("DB_NAME")   
     
    username = os.getenv("DB_USERNAME")
    password = os.getenv("DB_PASSWORD")
    connection = pyodbc.connect(f"""
        Driver={driver};
        Server={server};
        Database={database};
        UID={username};
        PWD={password};
    """
    )
    return connection
