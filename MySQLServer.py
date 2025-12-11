#!/usr/bin/env python3
"""
MySQLServer.py

Simple script to create the database `alx_book_store` on a MySQL server.

Requirements:
- Prints a success message when the database is created (or already exists).
- Does NOT fail if the database already exists.
- Does NOT use SELECT or SHOW statements.
- Handles connection errors and closes the connection properly.
"""

import mysql.connector
from mysql.connector import Error


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
            connection.commit()
            print("Database 'alx_book_store' created successfully!")

    except Error as err:
        print(f"Error connecting to MySQL or creating database: {err}")

    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None and connection.is_connected():
            connection.close()


if __name__ == "__main__":
    create_database()
