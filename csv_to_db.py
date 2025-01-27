import pandas as pd
import sqlite3

# Load the CSV data into a DataFrame
df = pd.read_csv('data.csv')

# Create a database connection
conn = sqlite3.connect('students.db')

# Write records stored in a DataFrame to a SQL database.
df.to_sql('students', conn, if_exists='replace', index=False)

# Close the connection
conn.close()
