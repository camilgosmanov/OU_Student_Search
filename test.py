import sqlite3

# Connect to the database
conn = sqlite3.connect('students.db')
c = conn.cursor()

# Fetch all records from the students table
c.execute('SELECT * FROM students')

# Get column names
column_names = [description[0] for description in c.description]
print(column_names)  # Print column names for verification

# Close the connection
conn.close()
