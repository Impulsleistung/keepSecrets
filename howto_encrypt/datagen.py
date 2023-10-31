import pandas as pd
import numpy as np
import json

# Generate random data
data = {
    'Column1': np.random.rand(3),
    'Column2': np.random.rand(3)
}

# Create DataFrame
df = pd.DataFrame(data)

# Write each row of the DataFrame as a separate JSON object to a file
with open('howto_encrypt\data.json', 'w') as file:
    for index, row in df.iterrows():
        json_row = json.dumps(row.to_dict())
        file.write(json_row + '\n')
