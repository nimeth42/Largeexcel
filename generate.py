import pandas as pd
import numpy as np

# Function to generate random data
def generate_random_data(num_rows, num_columns):
    data = {
        f'Column{i+1}': np.random.randint(0, 100, num_rows) for i in range(num_columns)
    }
    data['CommonColumn'] = np.random.randint(0, 50000, num_rows)  # Common column for merging
    return pd.DataFrame(data)

# Generate the first file
num_rows = 1000000  # 1 million rows
num_columns = 10    # 10 columns

df1 = generate_random_data(num_rows, num_columns)
df2 = generate_random_data(num_rows, num_columns)

# Save the data to Excel files
file1 = r'C:\Users\nimeth\Documents\GitHub\Excel read\large_file1.xlsx'
file2 = r'C:\Users\nimeth\Documents\GitHub\Excel read\large_file2.xlsx'

df1.to_excel(file1, index=False)
df2.to_excel(file2, index=False)

print(f"Files generated:\n{file1}\n{file2}")
