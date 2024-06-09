import sqlite3
import json

# Connect to the database
conn = sqlite3.connect('students.db')
c = conn.cursor()

# Fetch all records from the students table
c.execute('SELECT * FROM students')
students = c.fetchall()

# Get column names
column_names = [description[0] for description in c.description]

# Convert to a list of dictionaries
students_dict = [dict(zip(column_names, row)) for row in students]

# Write to a JSON file
with open('students.json', 'w') as f:
    json.dump(students_dict, f, indent=4)

# Close the connection
conn.close()
