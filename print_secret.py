import pandas as pd
import os

# Set the display options
pd.set_option('display.max_rows', 10)
pd.set_option('display.max_columns', 10)

file_path = os.path.join(os.environ['HOME'], 'decrypted_file.json')
df = pd.read_json(file_path)

df_str = df.to_string(index=False, border=True)
print(df_str)