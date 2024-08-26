import pandas as pd
import numpy as np

# Total number of rows and columns you want
total_rows = 2_000_000
num_cols = 10  # You can change this to the desired number of columns
chunk_size = 100_000  # Number of rows per chunk

# Create an Excel writer object to write to the Excel file
with pd.ExcelWriter('random_data_large.xlsx', engine='openpyxl') as writer:
    for i in range(0, total_rows, chunk_size):
        # Generate a chunk of random data
        data_chunk = np.random.rand(min(chunk_size, total_rows - i), num_cols)
        
        # Create a DataFrame
        df = pd.DataFrame(data_chunk, columns=[f'Column_{j+1}' for j in range(num_cols)])
        
        # Write the DataFrame chunk to the Excel file
        df.to_excel(writer, sheet_name='Sheet1', startrow=i, header=(i == 0), index=False)

print("Random data has been generated and saved to 'random_data_large.xlsx'")
