import mysql.connector
from mysql.connector import Error

def create_database():
    try:

        my_db = mysql.connector.connect(
            host='localhost',
            user='your_username',   
            passwordd='your_password'

            )

        
        if connection.is_connected():
            cursor = connection.cursor()
            # Create database if it doesn't exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store;")
            print("Database 'alx_book_store' created successfully!")
    
    except Error as e:
        print("except mysql.connector.Error")
    
    finally:
        # Close cursor and connection
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_database()
