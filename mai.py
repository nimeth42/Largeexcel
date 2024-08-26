import pandas as pd

def save_large_dataframe(df, filename, sheet_name_prefix='Sheet', chunk_size=1048576):
    """
    Save a large DataFrame to an Excel file by splitting it across multiple sheets.
    
    Parameters:
    - df: The DataFrame to save.
    - filename: The name of the Excel file to create.
    - sheet_name_prefix: Prefix for sheet names.
    - chunk_size: Maximum number of rows per sheet.
    """
    with pd.ExcelWriter(filename, engine='openpyxl') as writer:
        # Calculate the number of chunks
        num_chunks = len(df) // chunk_size + 1
        
        for i in range(num_chunks):
            start_row = i * chunk_size
            end_row = start_row + chunk_size
            chunk_df = df.iloc[start_row:end_row]
            
            # Create a sheet name
            sheet_name = f'{sheet_name_prefix}_{i+1}'
            
            # Write chunk to a sheet
            chunk_df.to_excel(writer, sheet_name=sheet_name, index=False, header=(i == 0))

# Example usage
# Load your large DataFrame (replace with your actual DataFrame loading code)
df = pd.read_excel('your_large_file.xlsx')

# Save the DataFrame to an Excel file with multiple sheets
save_large_dataframe(df, 'large_file_split.xlsx')
