import csv
import os

# Print the current working directory
print(os.getcwd())

# Open the CSV file and create a reader object
with open('fakeEventsData.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)

    # Initialize the SQL query
    sql_query = "INSERT INTO calendarevents (Event_no, Event_name, Event_date, Course_ID) VALUES "

    # Loop through each row in the CSV file and append values to the SQL query
    for row in reader:
        print(row)
        # Extract the data from the current row
        forum_id = row['ï»¿Event_no']
        name = row['Event_name']
        grade = row['Event_date']
        course_id=row["Course_ID"]
        

        # Append the values to the SQL query
        sql_query += f"({forum_id}, '{name}', '{grade}', '{course_id}'), "

    # Remove the last comma and space from the SQL query
    sql_query = sql_query[:-2]

    # Add a semicolon to the end of the SQL query
    sql_query += ";"

    # Print the SQL query
    with open(f"eventdata_query.sql", "w") as f:
            f.write(sql_query)
