import psycopg2
import csv
from config import load_config

def create_table():
    conn = psycopg2.connect(**load_config())
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS phonebook2 (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            phone_number VARCHAR(20) NOT NULL
        );
    ''')
    conn.commit()
    cursor.close()
    conn.close()

def insert_from_console():
    conn = psycopg2.connect(**load_config())
    cursor = conn.cursor()
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    try:
        cursor.execute("CALL insert_or_update_user2(%s, %s);", (name, phone))
    except:
        cursor.execute("INSERT INTO phonebook2 (name, phone_number) VALUES (%s, %s);", (name, phone))
    conn.commit()
    cursor.close()
    conn.close()

def insert_from_csv():
    conn = psycopg2.connect(**load_config())
    cursor = conn.cursor()
    try:
        with open("insert2.csv", newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            headers = next(reader)  # пропустить заголовки
            data = list(reader)

        for row in data:
            if len(row) == 2 and row[0].strip() and row[1].strip():
                cursor.execute("CALL insert_or_update_user2(%s, %s);", (row[0].strip(), row[1].strip()))

        conn.commit()
        print("Batch insert completed.")
    except Exception as e:
        print("Error", e)

def update_user_data():
    conn = psycopg2.connect(**load_config())
    cursor = conn.cursor()
    name = input("Enter name to update: ")
    phone = input("Enter new phone: ")
    cursor.execute("CALL insert_or_update_user2(%s, %s);", (name, phone))
    conn.commit()
    cursor.close()
    conn.close()

def query_data():
    conn = psycopg2.connect(**load_config())
    cursor = conn.cursor()
    choice = input("Enter search pattern (or press Enter to show all): ")
    if choice.strip() == "":
        cursor.execute("SELECT * FROM phonebook2 ORDER BY id;")
    else:
        cursor.execute("SELECT * FROM search_phonebook2(%s);", (choice,))
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    conn.close()

def query_with_pagination():
    conn = psycopg2.connect(**load_config())
    cursor = conn.cursor()
    limit = int(input("Enter limit: "))
    offset = int(input("Enter offset: "))
    cursor.execute("SELECT * FROM get_paginated_records2(%s, %s);", (limit, offset))
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    conn.close()

def delete_user():
    conn = psycopg2.connect(**load_config())
    cursor = conn.cursor()
    value = input("Enter username or phone to delete: ")
    cursor.execute("CALL delete_user2(%s);", (value,))
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == '__main__':
    create_table()
    while True:
        print("\n1. Insert from console\n2. Insert from CSV\n3. Update\n4. Query\n5. Delete\n6. Exit\n7. Query with pagination")
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
            delete_user()
        elif choice == '6':
            break
        elif choice == '7':
            query_with_pagination()
        else:
            print("Invalid choice, please try again.")
