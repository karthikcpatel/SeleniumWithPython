import pandas as pd

excel_file_path = r"C:\Users\kartik.patel\Downloads\January 2023.xlsx"
read_values_from_excel = pd.read_excel(excel_file_path, sheet_name='Sheet1')
print(read_values_from_excel)

write_excel = read_values_from_excel.to_excel(r"C:\Users\kartik.patel\Downloads\New_Write.xlsx",sheet_name='Sheet3',index=False)
print(write_excel)
print("Successfully copied and printed values in Sheet 1 of an excel")

with pd.ExcelWriter(r"C:\Users\kartik.patel\Downloads\kp_write.xlsx",engine='openpyxl', mode='a') as writer:
   read_values_from_excel.to_excel(writer,sheet_name='Sheet2',index=False)
print("Successfully copied and printed values in Sheet 2 of an excel")

write_data_in_excel = pd.DataFrame({'Name': ['Kartik', 'Amit', 'Bhavesh', 'Vimal','Mohit'],'Age': [30, 28, 25, 24,26]})
excel_writer = pd.ExcelWriter(r"C:\Users\kartik.patel\Downloads\kp_write.xlsx",engine='openpyxl',mode='a')
write_data_in_excel.to_excel(excel_writer,index=False,sheet_name='Sheet3')
excel_writer.save()
print("Successfully printed static data in Sheet 3 of an excel")
