import openpyxl


def fill_column_with_sheet_name(filename):
    wb = openpyxl.load_workbook(filename)

    for sheet in wb:
        sigu_column_index = "F"
        sigu_column = sheet[sigu_column_index]

        for cell in sigu_column[1:]:
            if sheet[f"A{cell.row}"].value is not None:
                cell.value = sheet.title
            else:
                break

    wb.save(filename)
    print("Sheet names added successfully.")


fill_column_with_sheet_name("kor_addresses.xlsx")
