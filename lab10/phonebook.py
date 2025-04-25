import psycopg2
import csv
from tabulate import tabulate

# Connect to PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    dbname="postgres",     
    user="postgres", 
    password="232326.Asiko",  
    port="5432"          
)
cur = conn.cursor()

# the phonebook table if it doesn't exist
cur.execute("""
CREATE TABLE IF NOT EXISTS phonebook (
    user_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    phone VARCHAR(255) UNIQUE NOT NULL
)
""")
conn.commit()


while True:
    print("Choose an action:")
    print("1 - Insert data manually")
    print("2 - Load data from CSV")
    print("3 - Update data")
    print("4 - Search data (by name or phone)")
    print("5 - Delete entry (by name or phone)")
    print("6 - Show all entries")
    print("0 - Exit")

    choice = input("Your choice: ")

    if choice == "1":
        name = input("Name: ")
        phone = input("Phone: ")
        cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (name, phone))
        conn.commit()
        print(" Data inserted!")

    elif choice == "2":
        path = input("Enter CSV file path: ")
        with open(path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  
            for row in reader:
                if len(row) >= 2:
                    cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (row[0], row[1]))
            conn.commit()
            print(" CSV data loaded!")

    elif choice == "3":
        old_phone = input("Enter the phone number you want to update: ")
        new_name = input("New name (leave blank to keep unchanged): ")
        new_phone = input("New phone (leave blank to keep unchanged): ")
        if new_name:
            cur.execute("UPDATE phonebook SET name = %s WHERE phone = %s", (new_name, old_phone))
        if new_phone:
            cur.execute("UPDATE phonebook SET phone = %s WHERE phone = %s", (new_phone, old_phone))
        conn.commit()
        print(" Data updated!")

    elif choice == "4":
        key = input("Enter name or phone to search: ")
        cur.execute("SELECT * FROM phonebook WHERE name = %s OR phone = %s", (key, key))
        results = cur.fetchall()
        print(tabulate(results, headers=["ID", "Name", "Phone"], tablefmt="grid"))

    elif choice == "5":
        key = input("Enter name or phone to delete: ")
        cur.execute("DELETE FROM phonebook WHERE name = %s OR phone = %s", (key, key))
        conn.commit()
        print(" Entry deleted (if found).")

    elif choice == "6":
        cur.execute("SELECT * FROM phonebook")
        rows = cur.fetchall()
        print(tabulate(rows, headers=["ID", "Name", "Phone"], tablefmt="fancy_grid"))

    elif choice == "0":
        break

    else:
        print(" Invalid input, try again.")


cur.close()
conn.close()
print(" Program ended.")

