import pandas as pd

# Load the decrypted file into a pandas dataframe
df = pd.read_json('$HOME/decrypted_file.json')

# Print the dataframe with nice formatting
with pd.option_context('display.max_rows', None, 'display.max_columns', None, 'display.width', 1000):
    print(df)
