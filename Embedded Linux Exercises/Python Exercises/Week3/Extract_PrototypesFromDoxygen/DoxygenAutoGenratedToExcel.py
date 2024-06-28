import bs4
import openpyxl

# Function to extract function prototypes from an HTML file and save them to an Excel file
def extract_prototypes_to_excel(html_file_path, output_excel_path):
    try:
        # Open the HTML file and read its contents
        with open(html_file_path, 'r', encoding='utf-8') as file:
            html_content = file.read()
        
        # Parse the HTML content using BeautifulSoup with the lxml parser
        soup = bs4.BeautifulSoup(html_content, 'lxml')

        # Find all table cells with classes memItemLeft and memItemRight
        left_cells = soup.find_all("td", class_="memItemLeft")
        right_cells = soup.find_all("td", class_="memItemRight")

        # Check if the number of left and right cells are the same
        if len(left_cells) != len(right_cells):
            print("Warning: Mismatch in the number of 'memItemLeft' and 'memItemRight' elements.")
        
        # Create a new Excel workbook and select the active sheet
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        sheet.title = 'Function Prototypes'

        # Set the headers for the Excel columns
        sheet['A1'] = "Return Type"
        sheet['B1'] = "Prototype"

        # Iterate over the found items and append them to the Excel sheet
        for left_cell, right_cell in zip(left_cells, right_cells):
            return_type = left_cell.get_text(strip=True)
            prototype = right_cell.get_text(strip=True)
            print(f"{return_type} {prototype}")  # Print for debugging purposes
            sheet.append([return_type, prototype])

        # Save the workbook to a file
        workbook.save(output_excel_path)
        print(f"Prototypes saved to {output_excel_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Main execution
if __name__ == "__main__":
    html_file_path = "Internal EEPROM Driver_ Source_Internal_EEPROM_prg.c File Reference.html"
    output_excel_path = "EEPROM_Function_Prototypes.xlsx"
    extract_prototypes_to_excel(html_file_path, output_excel_path)
