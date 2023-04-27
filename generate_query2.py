import csv
import os

# Print the current working directory
print(os.getcwd())

# Open the CSV file and create a reader object
with open('Enrol.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)

    # Initialize the SQL query and row counter
    sql_query = "INSERT INTO enrol (Student_ID, Course_id, Grade) VALUES "
    row_count = 0

    # Loop through each row in the CSV file and append values to the SQL query
    for row in reader:
        # Extract the data from the current row
        forum_id = row['Student_ID']
        name = row['Course_ID']
        grade = row['Grade']

        # Append the values to the SQL query
        sql_query += f"({forum_id}, '{name}', {grade}), "
        row_count += 1

        # Check if the row count is divisible by 1000 or if it's the last row
        if row_count % 1000 == 0 or row_count == reader.line_num - 1:
            # Remove the last comma and space from the SQL query
            sql_query = sql_query[:-2]

            # Add a semicolon to the end of the SQL query
            sql_query += ";"

            # Write the SQL query to the SQL file
            with open(f"newenrol_query.sql", "a") as f:
                f.write(sql_query)

            # Reset the SQL query for the next batch of rows
            sql_query = "INSERT INTO enrol (Student_ID, Course_id, Grade) VALUES "
