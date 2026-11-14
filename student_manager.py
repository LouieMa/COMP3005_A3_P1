# student_manager.py - CRUD application for the students table in PostgreSQL
# Provides text menu for view, add, update, and select student records

import os
import psycopg2
from psycopg2 import errors

# Connection settings for PostgreSQL database
DB_CONFIG = {
    "dbname": os.getenv("DB_NAME", "students_db"),
    "user": os.getenv("DB_USER", "postgres"),
    "password": os.getenv("DB_PASSWORD", "postgres"),
    "host": os.getenv("DB_HOST", "localhost"),
    "port": os.getenv("DB_PORT", "5432"),
}

def connect_db():
    # Open and return a new connection to database
    return psycopg2.connect(**DB_CONFIG)

def getAllStudents():
   #  Retrieve and print all student records in the students table
   connection = connect_db()
   try:
       with connection, connection.cursor() as cur:
           cur.execute("SELECT student_id, first_name, last_name, email, enrollment_date "
                       "FROM students ORDER BY student_id;")
           rows = cur.fetchall()
           if not rows:
               print("No students found.")
               return
           print(f"{'ID':<4}{'First':<10}{'Last':<10}{'Email':<28}{'Enrolled'}")
           for sid, first, last, email, date in rows:
               print(f"{sid:<4}{first:<10}{last:<10}{email:<28}{date}")
   finally:
       connection.close()

def main():
    # menu for crud functionality
    menu = ("\n1) View all students\n"
            "2) Quit")
    while True:
        print(menu)
        choice = input("Choose an option: ").strip()
        try:
            if choice == "1":
                getAllStudents();
            elif choice == "2":
                break
            else:
                print("Invalid option.")
        except ValueError:
            print("Student ID must be a number.")
        except psycopg2.OperationalError as e:
            print(f"Could not connect to database: {e}")

if __name__ == "__main__":
    main()