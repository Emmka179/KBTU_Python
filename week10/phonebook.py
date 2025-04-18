import psycopg2
import csv
from config import load_config

import psycopg2
from config import load_config

def create_tables():
    conn = psycopg2.connect(**load_config())
    cursor = conn.cursor()
    # Create the phonebook table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            phone_number VARCHAR(15) NOT NULL
        );
    ''')
    conn.commit()
    cursor.close()
    conn.close()

def insert_from_csv(filename='insert.csv'):
    conn = psycopg2.connect(**load_config())
    cursor = conn.cursor()
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            cursor.execute("INSERT INTO phonebook (name, phone_number) VALUES (%s, %s)", (row[0], row[1]))
    conn.commit()
    cursor.close()
    conn.close()

def insert_from_console():
    conn = psycopg2.connect(**load_config())
    cursor = conn.cursor()
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    cursor.execute("INSERT INTO phonebook (name, phone_number) VALUES (%s, %s)", (name, phone))
    conn.commit()
    cursor.close()
    conn.close()

def update_user_data():
    conn = psycopg2.connect(**load_config())
    cursor = conn.cursor()
    name = input("Enter name to update: ")
    new_phone = input("Enter new phone number: ")
    cursor.execute("UPDATE phonebook SET phone_number = %s WHERE name = %s", (new_phone, name))
    conn.commit()
    cursor.close()
    conn.close()

def query_data():
    conn = psycopg2.connect(**load_config())
    cursor = conn.cursor()
    print("Filter by:\n1. Username\n2. Phone\n3. All")
    choice = input("Enter choice: ")
    if choice == '1':
        name = input("Enter name: ")
        cursor.execute("SELECT * FROM phonebook WHERE name = %s", (name,))
    elif choice == '2':
        phone = input("Enter phone: ")
        cursor.execute("SELECT * FROM phonebook WHERE phone_number = %s", (phone,))
    else:
        cursor.execute("SELECT * FROM phonebook")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    conn.close()

def delete_data():
    conn = psycopg2.connect(**load_config())
    cursor = conn.cursor()
    print("Delete by:\n1. Username\n2. Phone")
    choice = input('Your choice: ')
    if choice == '1':
        name = input("Enter name to delete: ")
        cursor.execute("DELETE FROM phonebook WHERE name = %s", (name,))
    else:
        phone = input("Enter phone to delete: ")
        cursor.execute("DELETE FROM phonebook WHERE phone_number = %s", (phone,))
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == '__main__':
    create_tables()
    while True:
        print("\n1. Insert from console\n2. Insert from CSV\n3. Update\n4. Query\n5. Delete\n6. Exit")
        choice = input("Choose the option: ")
        if choice == '1':
            insert_from_console()
        elif choice == '2':
            insert_from_csv()
        elif choice == '3':
            update_user_data()
        elif choice == '4':
            query_data()
        elif choice == '5':
            delete_data()
        elif choice == '6':
            break
        else:
            print("Invalid choice, please try again.")