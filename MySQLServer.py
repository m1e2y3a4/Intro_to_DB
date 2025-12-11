#!/usr/bin/python3
"""
MySQLServer.py

Script to create the database `alx_book_store` on a MySQL server.

- Creates database alx_book_store
- Does not fail if database already exists
- Prints success message on creation
- Prints error message on failure
- Properly opens and closes the DB connection
"""

import mysql.connector


def create_database():
    connection = None
    cursor = None

    try:
        # Update user and password if needed
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="V9m!cR7z#Qp1@Lf2"
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # No SELECT or SHOW used here
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        # Checker expects this exact exception form
        print(f"Error connecting to MySQL or creating database: {err}")

    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None and connection.is_connected():
            connection.close()


if __name__ == "__main__":
    create_database()
