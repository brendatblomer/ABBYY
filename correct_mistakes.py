
# we import the packages and functions we need
import pandas as pd
from pathlib import Path
from correct_mistakes_functions import replacement_of_a, replacement_of_letters, complete_cleaning

# We use the excel we want to arrange and change the group column to index so is not affected
path_excel = Path("borrar_luego") / "1973_abbyy.xlsx"
df_original = pd.read_excel(path_excel)

# We create a copy so we dont modify the original DataFrame
df_new = df_original.copy()

### Now we have to adjust after looking at the data, which functions we want to use for this specific DataFrame

# List of columns for first function (normally just "Change in inventories")
column_with_a = ['Change in inventories']

# Apply first function just to columns selected with "a" or "A" instead of "-"
for column in column_with_a:
    df_new[column] = df_new[column].apply(replacement_of_a)

# Apply second function to all columns but Group
for column in df_new.columns:
    if column != "Group":
        df_new[column] = df_new[column].apply(replacement_of_letters)

# Apply third functions to all columns but Group
for column in df_new.columns:
    if column != "Group":
        df_new[column] = df_new[column].apply(complete_cleaning)

# Save excel with a new name
df_new.to_excel('file_ready_1973.xlsx', index=False)
print("File corrected and saved as 'file_ready_1973.xlsx' ready for pasting and checking with PDF")

