import pandas as pd
import os

def display_json_content(file_path):
    """
    Load and display the content of a JSON file.
    
    Args:
    file_path (str): The path to the JSON file.
    
    Returns:
    DataFrame: A pandas DataFrame containing the contents of the JSON file.
    """
    df = pd.read_json(file_path)
    return df

# Set the path to the JSON file
json_file_path = os.path.join(os.environ['HOME'], 'decrypted_file.json')

# Display the content of the JSON file
displayed_content = display_json_content(json_file_path)
print(displayed_content)