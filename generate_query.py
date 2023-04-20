import csv
import os

# Print the current working directory
print(os.getcwd())

# Open the CSV file and create a reader object
with open('sections.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)

    # Initialize the SQL query
    sql_query = "INSERT INTO section (SectionID, Section_Name, Active, Course_id) VALUES "

    # Loop through each row in the CSV file and append values to the SQL query
    for row in reader:
        # Extract the data from the current row
        forum_id = row['ï»¿Section_ID']
        name = row['Section_Name']
        date = row['Active']
        active = row["Course_id"]

        # Append the values to the SQL query
        sql_query += f"({forum_id}, '{name}', '{date}', '{active}'), "

    # Remove the last comma and space from the SQL query
    sql_query = sql_query[:-2]

    # Add a semicolon to the end of the SQL query
    sql_query += ";"

    # Print the SQL query
    with open(f"section_query.sql", "w") as f:
            f.write(sql_query)
