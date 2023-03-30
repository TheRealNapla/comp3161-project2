import csv
import os

# Print the current working directory
print(os.getcwd())

# Open the CSV file and create a reader object
with open('accounts.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)

    # Initialize the SQL query
    sql_query = "INSERT INTO account (UserID, Name, Email, Password, Account_Type) VALUES "

    # Loop through each row in the CSV file and append values to the SQL query
    for row in reader:
        # Extract the data from the current row
        user_id = row['ID']
        name = row['Name']
        email = row['Email']
        password = row['Password']
        account_type = row["Account Type"]

        # Append the values to the SQL query
        sql_query += f"({user_id}, '{name}', {email}, '{password}', '{account_type}'), "

    # Remove the last comma and space from the SQL query
    sql_query = sql_query[:-2]

    # Add a semicolon to the end of the SQL query
    sql_query += ";"

    # Print the SQL query
    with open(f"accounts_query.sql", "w") as f:
            f.write(sql_query)
