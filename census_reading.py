import os,openpyxl

os.chdir(r"C:\Pajtek")

wb = openpyxl.Workbook()
wb.create_sheet(title="Bekonik")
sheet = wb["Bekonik"]
sheet['A1'] = "Hello world"
wb.save('example_copy.xlsx')


