import difflib

first_file = r"C:\Users\kartik.patel\PycharmProjects\SeleniumWithPython\file handling\test data\175327_W4.xml"
second_file = r"C:\Users\kartik.patel\PycharmProjects\SeleniumWithPython\file handling\test data\175328_W4.xml"

first_file_lines = open(first_file).readlines()
second_file_lines = open(second_file).readlines()
difference = difflib.HtmlDiff().make_file(first_file_lines,second_file_lines,first_file,second_file)
difference_report = open(r"C:\Users\kartik.patel\PycharmProjects\SeleniumWithPython\file handling\test data\difference_report.html",'w')
difference_report.write(difference)
difference_report.close()