import sqlite3
import json
from lunr import lunr

# Connect to the database
conn = sqlite3.connect('students.db')
c = conn.cursor()

# Fetch all records from the students table
c.execute('SELECT * FROM students')
students = c.fetchall()

# Get column names
column_names = [description[0] for description in c.description]

# Rename columns
column_names[0] = 'ID'  # Rename 'Unnamed: 0' to 'ID'
column_names[7] = 'Fall 2019'  # Rename 'Unnamed: 8' to 'Fall 2019'
column_names[8] = 'Fall 2020'  # Rename 'Unnamed: 9' to 'Fall 2020'
column_names[9] = 'Fall 2021'  # Rename 'Unnamed: 10' to 'Fall 2021'
column_names[10] = 'Fall 2022'  # Rename 'Unnamed: 11' to 'Fall 2022'
column_names[11] = 'Fall 2023'  # Rename 'Unnamed: 12' to 'Fall 2023'
column_names[12] = 'Fall 2024'  # Rename 'Unnamed: 12' to 'Fall 2023'
column_names[13] = 'Spring 2020'  # Rename 'Unnamed: 13' to 'Spring 2020'
column_names[14] = 'Spring 2021'  # Rename 'Unnamed: 14' to 'Spring 2021'
column_names[15] = 'Spring 2022'  # Rename 'Unnamed: 15' to 'Spring 2022'
column_names[16] = 'Spring 2023'  # Rename 'Unnamed: 16' to 'Spring 2023'
column_names[17] = 'Spring 2024'  # Rename 'Unnamed: 16' to 'Spring 2023'
column_names[18] = 'Spring 2025'  # Rename 'Unnamed: 17' to 'Spring 2024'

# Create a list of dictionaries with column names
students_dict = [dict(zip(column_names, row)) for row in students]

# Create a Lunr index
index = lunr(
    ref='ID',
    fields=[col for col in column_names if col != 'ID'],
    documents=students_dict
)

# Save the index and data to JSON files
with open('students_index.json', 'w') as f:
    json.dump(index.serialize(), f, indent=4)

with open('students.json', 'w') as f:
    json.dump(students_dict, f, indent=4)

# Close the connection
conn.close()
