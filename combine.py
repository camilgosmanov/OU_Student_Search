import pandas as pd
import os
import re

# Define a function to extract the number from a string
def extract_number(s):
    match = re.search(r'\d+', s)  # Find the first sequence of digits
    return int(match.group()) if match else 0


def combine_data(directory):
    all_data = pd.DataFrame()

    files = os.listdir(directory)
    files.sort(key=extract_number)
    
    for file in files:
        if file.endswith("Roll.xlsx"):
            df = pd.read_excel(file)
            for x in df.columns:
                if 'last' in x.lower():
                    df.rename(columns={x: 'Last Name'}, inplace=True)
                elif 'first' in x.lower():
                    df.rename(columns={x: 'First Name'}, inplace=True)
                elif 'middle' in x.lower():
                    df.rename(columns={x: 'Middle Name'}, inplace=True)
                elif 'city' in x.lower():
                    df.rename(columns={x: 'City'}, inplace=True)
                elif 'state' in x.lower():
                    df.rename(columns={x: 'State'}, inplace=True)
                elif 'president' in x.lower():
                    df.rename(columns={x: 'President'}, inplace=True)
                else:
                    df.drop(x, axis=1, inplace=True)
            df['Full Name'] = df['First Name'] + ' ' + df['Last Name']
            df['Semester'] = file.removesuffix(" Honor Roll.xlsx")  # Assuming the file name is the semester
            df["Honor Roll"] = df.apply(lambda x: 'Yes*' if '*' in str(x['President']) or x['Full Name']=="Camil Gosmanov" else 'Yes', axis=1)
            df["Score"] = df['President'].apply(lambda x: 4 if '*' in str(x) else 3)
            all_data = pd.concat([all_data, df], axis=0, ignore_index=True)
    
    return all_data

def pivot_data(all_data):
    first_column = all_data.columns[0]  # Get the name of the first column
    pivot_df = all_data.pivot_table(index=['Full Name','Middle Name', 'Last Name', 'City', 'State', 'Score'], 
                                    columns='Semester', 
                                    values=['Honor Roll'], 
                                    aggfunc='max', 
                                    fill_value='No')
    pivot_df.reset_index(inplace=True)

    # Define the custom order of semesters
    #semester_order = ['Fall 2019', 'Spring 2020', 'Fall 2020', 'Spring 2021', 'Fall 2021', 'Spring 2022', 'Fall 2022', 'Spring 2023', 'Fall 2023']  # Add more semesters if needed
    
    # Reorder the MultiIndex in columns based on the custom semester order
    #pivot_df = pivot_df.reindex(columns=[('Honor Roll', semester) for semester in semester_order], level=1)

    pivot_df.to_excel('Combined_Data5.xlsx')  # Write the DataFrame to an Excel file
    

directory = './'  # Directory containing the Excel files
all_data = combine_data(directory)
all_data.fillna("NULL", inplace=True)
all_data['Score'] = all_data.groupby(['Last Name', 'First Name','Middle Name', 'City', 'State'])['Score'].transform('sum')
pivot_data(all_data)  # Pivot the data and write it to an Excel file

