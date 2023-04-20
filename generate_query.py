import csv
import os

# Print the current working directory
print(os.getcwd())

# Open the CSV file and create a reader object
with open('courses-edit.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)

    # Initialize the SQL query
    sql_query = "INSERT INTO section (Course_id, Coursename, Lecturer_ID, CourseLecturer, Coursegrade) VALUES "

    # Loop through each row in the CSV file and append values to the SQL query
    for row in reader:
        # Extract the data from the current row
        forum_id = row['Course_id']
        name = row['Coursename']
        date = row['Lecturer_ID']
        active = row["CourseLecturer"]
        grade = row["Coursegrade"]

        # Append the values to the SQL query
        sql_query += f"('{forum_id}', '{name}', {date}, '{active}', {grade}), "

    # Remove the last comma and space from the SQL query
    sql_query = sql_query[:-2]

    # Add a semicolon to the end of the SQL query
    sql_query += ";"

    # Print the SQL query
    with open(f"courses_query.sql", "w") as f:
            f.write(sql_query)
