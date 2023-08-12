import pandas as pd
import os

# Set the display options
file_path = os.path.join(os.environ['HOME'], 'decrypted_file.json')
df = pd.read_json(file_path)

print(df.iloc[:, 0])