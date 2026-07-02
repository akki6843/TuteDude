'''
# Connect to PostgreSQL database and create a table named "employees" with columns "name", "age", and "department".
# Insert records into the "employees" table.
# Allow the user to input employee details and insert them into the table.
# Fetch all records from the "employees" table and display them in a DataFrame.
# Finally, close the connection to the database.
'''
import psycopg2
import pandas as pd

def connect_to_postgresql():
    connect = psycopg2.connect(dbname="postgres",
                            user="postgres", 
                            password="12345", 
                            host="localhost", 
                            port="5432")
    print(connect)
    print("Connection to PostgreSQL database successful!")
    return connect

def create_table(connect):
    cursor = connect.cursor()
    cursor.execute('''
                CREATE TABLE IF NOT EXISTS employees (name text, age int, department text);
    ''')

    print("Table created successfully!")
    connect.commit()

def insert_data(connect):
    cursor = connect.cursor()
    cursor.execute('''
                INSERT INTO employees (name, age, department) VALUES ('RAJ', 25, 'HR');
                INSERT INTO employees (name, age, department) VALUES ('VENU', 31, 'IT');
                INSERT INTO employees (name, age, department) VALUES ('DILIP', 68, 'Finance');
    ''')
    print("Data inserted successfully!")
    connect.commit()


def user_input(connect):
    print("Enter employee details:")
    name = input("Enter employee name: ")
    age = int(input("Enter employee age: "))
    department = input("Enter employee department: ")
    
    cursor = connect.cursor()
    cursor.execute('''
                INSERT INTO employees (name, age, department) VALUES (%s, %s, %s);
    ''', (name, age, department))
    
    print("Data inserted successfully!")
    connect.commit()

def fetch_data(connect):
    cursor = connect.cursor()
    cursor.execute('''
                   SELECT * FROM employees;
                   ''')
    records = cursor.fetchall()
    column_names = [desc[0] for desc in cursor.description]
    df = pd.DataFrame(records, columns=column_names)
    print(df)
    print("Data fetched successfully!")
    return df

def close_connection(connect):
    connect.close()
    print("Connection closed successfully!")

if __name__ == "__main__":
    connect = connect_to_postgresql()
    # create_table(connect)  # Run this line only once to create the table, then comment it out to avoid errors on subsequent runs.
    # insert_data(connect) # Run this line only once to insert data, then comment it out to avoid duplicate entries on subsequent runs.
    user_input(connect)  
    df = fetch_data(connect)
    close_connection(connect)
    print("All operations completed successfully!")
