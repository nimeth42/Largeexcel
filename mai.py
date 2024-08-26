import pandas as pd
import numpy as np

# Number of rows and columns you want
num_rows = 1000  # You can change this to the desired number of rows
num_cols = 10    # You can change this to the desired number of columns

# Generate random data
data = np.random.rand(num_rows, num_cols)

# Create a DataFrame
df = pd.DataFrame(data, columns=[f'Column_{i+1}' for i in range(num_cols)])

# Save the DataFrame to an Excel file
df.to_excel('random_data.xlsx', index=False)

print("Random data has been generated and saved to 'random_data.xlsx'")
