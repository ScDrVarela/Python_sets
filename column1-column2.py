import pandas as pd

# Replace 'C:/Users/Miguel Varela/Desktop/databases_names_processed.xlsx'
# with the actual file path and file name
file_path = 'C:/Users/Miguel Varela/Desktop/databases_names_processed.xlsx'

try:
    # Read the Excel file into a pandas DataFrame
    df = pd.read_excel(file_path, sheet_name='remaining-columns')

    # Choose the column for Set A
    column_a = 'column1'     # Replace 'column1' with the desired column name for Set A

    # Remove rows with missing values in column_a
    df_cleaned_a = df.dropna(subset=[column_a])

    # Create Set A
    set_a = set(df_cleaned_a.loc[:, column_a])

    # Choose the column for Set B
    column_b = 'column2'     # Replace 'Column2' with the desired column name for Set B

    # Remove rows with missing values in column_b
    df_cleaned_b = df.dropna(subset=[column_b])

    # Create Set B
    set_b = set(df_cleaned_b.loc[:, column_b])

    # Perform the set operation (column1) - (column2)
    set_c = set_a - set_b

    # Print the result (Set C)
    print("Set C (column1 - column2):", set_c)
except FileNotFoundError:
    print("File not found. Please check the file path.")
except Exception as e:
    print("An error occurred:", e)
#This