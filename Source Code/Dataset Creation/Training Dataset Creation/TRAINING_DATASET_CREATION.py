import pandas as pd
import random
import openpyxl

def read_cipher_text(file_path):
    
    df = pd.read_excel(file_path)
    return df['cipher_text']

def remove_underscores(sheet):
    
    for col in sheet.iter_cols():
        for cell in col:
            cell.value = cell.value.replace('_', ' ')

excel_files = ['PLAYFAIR_CIPHER_DATASET.xlsx','POLYBIUS_SQUARE_CIPHER_DATASET.xlsx','BACONIAN_CIPHER_DATASET.xlsx','ATBASH_CIPHER_DATASET.xlsx','VIGENERE_CIPHER_DATASET.xlsx','SCYTALE_CIPHER_DATASET.xlsx','RAIL_FENCE_CIPHER_DATASET.xlsx','HILL_CIPHER_DATASET.xlsx','GRONSFIELD_CIPHER_DATASET.xlsx','COLUMNAR_TRANSPOSITION_CIPHER_DATASET.xlsx','CAESAR_CIPHER_DATASET.xlsx','AFFINE_CIPHER_DATASET.xlsx']

merged_data = []

for file in excel_files:
    df = pd.read_excel(file)
    column_names = df.columns.tolist()
    cipher_text_column = next((col for col in column_names if 'Cipher Text' in col), None)

    if cipher_text_column:
        cipher_text = df[cipher_text_column].tolist()
        label = file.split('_DATASET.')[0]
        labeled_data = [(text, label) for text in cipher_text]
        merged_data.extend(labeled_data)
    else:
        print(f"Could not find the ciphertext column in file : {file}")

merged_df = pd.DataFrame(merged_data, columns=['Cipher Text', 'Cipher Label'])

merged_df_lowercase = merged_df.copy()
merged_df_lowercase['Cipher Text'] = merged_df_lowercase['Cipher Text'].str.lower()

for _ in range(3):
    merged_df = merged_df.sample(frac=1).reset_index(drop=True)
    merged_df_lowercase = merged_df_lowercase.sample(frac=1).reset_index(drop=True)

output_file_name = 'FULL_12_CIPHERS.xlsx'
merged_df_lowercase.to_excel(output_file_name, index=False)

print(f"Data been saved to {output_file_name}.")


def main():

    try:
        workbook = openpyxl.load_workbook(output_file_name)
        sheet = workbook.active
        remove_underscores(sheet)
        workbook.save(f"modified_{output_file_name}")
        print(f"Column names in '{output_file_name}' have been modified successfully and saved as 'MODIFIED_{output_file_name}'.")
    except FileNotFoundError:
        print(f"Error: File '{output_file_name}' not found.")
    except openpyxl.utils.exceptions.InvalidFileException:
        print(f"Error: '{output_file_name}' is not a valid Excel file.")

if __name__ == "__main__":
    
    main()



