### THIS IS JUST AN EXTRA ONE, WE CAN JUST ADD THE FUNCTION TO THE OTHER PYTHON CODE
# we import the packages we need
import pandas as pd
import re

# Functions for cleanining data: 

def replacement_of_a (selected_column):
    """ This function is for specific columns that are changes,
    ABBYY reads triangles as "A" or "a" so we need to fix that first.

    selected_column (series): Here we introduce the name of the column we want to clean.
    Return: it returns the column but with the replacement done, changing "A" and "a" for "-"
    """
    return str(selected_column).replace("A", "-").replace("a", "-")
    

def replacement_of_letters (selected_column):
    """ This function changes the letters that could have been confused with numbers,
    ABBYY reads 1 as i or I for example. And also we convert all empty cells to "0"
    and cells with "x" to empty cells.

    selected_column (series): Here we introduce the name of the column we want to clean.
    Return: it returns the column but with the replacement done, changing "I" and "i" for "1", etc.
    """
    text = str(selected_column)

    # feel free to add replacements that you saw and feel you need
    text = text.replace("I", "1").replace("i", "1")
    text = text.replace("s", "5").replace("S", "5")
    text = text.replace("k", "8").replace("K", "8")
    text = re.sub(r'[oOóÓcCgG]', '0', text)

    if text.strip() == "":
        return 0
    elif text.strip().lower() == "x":
        return "" 
    
    if text.isdigit() or (text.lstrip('-').isdigit() and text.count('-') == 1): 
        return int(text)
    
    return text

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
    

# EXAMPLE:
df = pd.DataFrame({
    'columna1': ['I', 's', 'k', 'o', 'x', ' ', None, '1234', 'a5678'],
    'columna2': ['cG', 'Ó', '5', 'x', 'oO', 'r   sK', 'ÓÓ', '12345', '-9876']
})

df_new = df.applymap(replacement_of_a)
df_new = df_new.applymap(replacement_of_letters)
df_new = df_new.applymap(complete_cleaning)

# Now we see the corrections :)
print(df)
print(df_new)