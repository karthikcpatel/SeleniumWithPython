import pandas as pd

excel_file_path = r"C:\Users\kartikp\Downloads\kp.xlsx"
read_values_from_excel = pd.read_excel(excel_file_path, sheet_name='Sheet1')
print(read_values_from_excel)

write_excel = read_values_from_excel.to_excel(r"C:\Users\kartikp\Downloads\Write Excel Using Pandas.xlsx",sheet_name='Sheet1',index=False)
print(write_excel)

#write_in_existing_excel = read_values_from_excel.to_excel(r"C:\Users\kartikp\Downloads\CTS Automation_team tag vs form name.xlsx",sheet_name='Sheet2',startcol=3,index=False)
#print(write_in_existing_excel)

#with pd.ExcelWriter(r"C:\Users\kartikp\Downloads\CTS Automation_team tag vs form name.xlsx",engine='openpyxl', mode='a') as writer:
#    read_values_from_excel.to_excel(writer,sheet_name='Sheet2',index=False)

write_data_in_excel = pd.DataFrame({'Name': ['Kartik', 'Amit', 'Bhavesh', 'Vimal','Mohit'],'Age': [30, 28, 25, 24,26]})
excel_writer = pd.ExcelWriter(r"C:\Users\kartikp\Downloads\CTS Automation_team tag vs form name.xlsx",engine='openpyxl',mode='a')
write_data_in_excel.to_excel(excel_writer,index=False,sheet_name='Sheet2')
excel_writer.save()

#with pd.ExcelWriter(r"C:\Users\kartikp\Downloads\CTS Automation_team tag vs form name.xlsx",engine='xlsxwriter') as writer:
#    read_values_from_excel.to_excel(writer,sheet_name='Sheet1',index=False,startcol=5)

new_excel_file_path = r"C:\Users\kartikp\Downloads\kp.xlsx"
new_excel_file_path = pd.read_excel(new_excel_file_path,sheet_name='Sheet1')
