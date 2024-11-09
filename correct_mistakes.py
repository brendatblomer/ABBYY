
# we import the packages we need
import pandas as pd
import re
from pathlib import Path

# We use the excel we want to arrange and change the group column to index so is not affected
path_excel = Path("borrar_luego") / "1973_abbyy.xlsx"
df_original = pd.read_excel(path_excel)

# We create a copy so we dont modify the original DataFrame
df_new = df_original.copy()

# Functions for cleanining data: 

def replacement_of_a (selected_column):
    """ This function is for specific columns that are changes,
    ABBYY reads triangles as "A" or "a" so we need to fix that first.

    selected_column (series): Here we introduce the name of the column we want to clean.
    Return: it returns the column but with the replacement done, changing "A" and "a" for "-"
    """
    return str(selected_column).replace("A", "-").replace("a", "-")


def complete_cleaning(selected_column):
    """ This function clean all things that are not numbers or "-".
    
    selected_column (series): Here we introduce the name of the column we want to clean.
    Return: it gives us back the column without any character that is not a number or a -, and as a integer. 
    """

    only_numbers = re.sub(r'[^0-9-]', '', str(selected_column))
    if only_numbers.lstrip('-').isdigit():
        return int(only_numbers)
    else:
        return only_numbers

### Now we have to adjust after looking at the data, which functions we want to use for this specific DataFrame

# List of columns for first function (normally just "Change in inventories")
column_with_a = ['Change in inventories']

# Apply first function just to columns selected with "a" or "A" instead of "-"
for column in column_with_a:
    df_new[column] = df_new[column].apply(replacement_of_a)

# Apply second functions to all columns but Group
for column in df_new.columns:
    if column != "Group":
        df_new[column] = df_new[column].apply(complete_cleaning)

# Save excel with a new name
df_new.to_excel('file_ready_1973.xlsx', index=False)
print("File corrected and saved as 'file_ready_1973.xlsx' ready for pasting and checking with PDF")

