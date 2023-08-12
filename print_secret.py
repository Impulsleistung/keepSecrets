
import pandas as pd
import os

# Set the display options
file_path = os.path.join(os.environ['HOME'], 'decrypted_file.json')
df = pd.read_json(file_path)

# Create a function to load and display the content of a JSON file using pandas
def display_json_content(file_path):
    df = pd.read_json(file_path)
    return df

# Test the function
displayed_content = display_json_content(file_path)
print(displayed_content)


