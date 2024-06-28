import re
import openpyxl

def extract_function_prototypes(file_path):
    """
    Extract function prototypes (including return type and parameters) from a header file.
    
    Args:
    file_path (str): The path of the header file.
    
    Returns:
    list: List of tuples containing return type, function prototype, and parameters.
    """
    with open(file_path, 'r') as header_file:
        content = header_file.read()

    # Regular expression pattern to match function prototypes with return type and parameters
    function_pattern = r'\b(?:void|int|char|float|double|unsigned|long|short|struct\s+\w+)\s+\w+\s*\([^;]*\);'
    prototypes = re.findall(function_pattern, content)

    # Extracting prototypes, return type, and parameters into a list of tuples
    prototypes_with_params = []
    for prototype in prototypes: # This loop iterates over each function prototype found in the header file. The prototypes list contains these prototypes as strings.
        # Split prototype into return type, function name, and parameters (if available)
        match = re.match(r'(\b(?:void|int|char|float|double|unsigned|long|short|struct\s+\w+)\s+)(\w+)\s*(\([^;]*\))', prototype)
        if match:
            return_type, func_name, params = match.groups()
            prototypes_with_params.append((return_type.strip(), f'{func_name.strip()}', params.strip()))

    return prototypes_with_params

def write_prototypes_to_excel(prototypes_with_params, output_path):
    """
    Write function prototypes, return type, parameters, and unique IDs to an Excel sheet.
    
    Args:
    prototypes_with_params (list): List of tuples containing return type, function prototypes, and parameters.
    output_path (str): The path of the output Excel file.
    
    Returns:
    None
    """
    # Create a new workbook and select the active sheet
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = 'Function Prototypes'

    # Write header row
    sheet['A1'] = 'Return Type'
    sheet['B1'] = 'Function Name'
    sheet['C1'] = 'Arguments'
    sheet['D1'] = 'Unique ID'

    # Write each prototype with parameters and a unique ID starting from 'IDX0'
    for index, (return_type, prototype, parameters) in enumerate(prototypes_with_params, start = 0):
        unique_id = f'IDX{index:03d}'
        sheet[f'A{index+2}'] = return_type.strip()
        sheet[f'B{index+2}'] = prototype.strip()
        sheet[f'C{index+2}'] = parameters.strip()
        sheet[f'D{index+2}'] = unique_id

    # Save workbook to specified output path
    workbook.save(output_path)
    print(f"Function prototypes with parameters saved to '{output_path}'.")

if __name__ == "__main__":
    # Paths to input header file and output Excel file
    header_file_path = 'Bootloader.h'
    output_excel_path = 'Function_Prototypes.xlsx'

    # Extract function prototypes from header file
    extracted_prototypes = extract_function_prototypes(header_file_path)

    # Write prototypes, return type, parameters, and unique IDs to Excel file
    write_prototypes_to_excel(extracted_prototypes, output_excel_path)
