import pandas as pd

excel_file_path = r"C:\Users\kartik.patel\Downloads\kp_new.xlsx"
read_values_from_excel = pd.read_excel(excel_file_path, sheet_name='Sheet1')
print(read_values_from_excel)

write_excel = read_values_from_excel.to_excel(r"C:\Users\kartik.patel\Downloads\kp_write.xlsx",sheet_name='Sheet1',index=False)
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

#with pd.ExcelWriter(r"C:\Users\kartikp\Downloads\CTS Automation_team tag vs form name.xlsx",engine='xlsxwriter') as writer:
#    read_values_from_excel.to_excel(writer,sheet_name='Sheet1',index=False,startcol=5)

# new_excel_file_path = r"C:\Users\kartikp\Downloads\kp.xlsx"
# new_excel_file_path = pd.read_excel(new_excel_file_path,sheet_name='Sheet1')
