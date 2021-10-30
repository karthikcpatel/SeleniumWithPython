import difflib

first_file = r"C:\Users\kartik.patel\OneDrive - Vertex, Inc\Desktop\respone 1\174848_US_NY_Yonkers_Calc_Guide_RO_Surcharge_Method_response.xml"
second_file = r"C:\Users\kartik.patel\OneDrive - Vertex, Inc\Desktop\respone 2\174848_US_NY_Yonkers_Calc_Guide_RO_Surcharge_Method_response.xml"

first_file_lines = open(first_file).readlines()
second_file_lines = open(second_file).readlines()
difference = difflib.HtmlDiff().make_file(first_file_lines,second_file_lines,first_file,second_file)
difference_report = open(r"C:\difference_report.html",'w')
difference_report.write(difference)
difference_report.close()