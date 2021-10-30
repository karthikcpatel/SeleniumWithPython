import os.path
import xml.etree.ElementTree as ET
import filecmp

tree = ET.parse(r"C:\Users\kartik.patel\OneDrive - Vertex, Inc\Desktop\174848_US_NY_Yonkers_Calc_Guide_RO_Surcharge_Method_response.xml")
root = tree.getroot()
print(root)
#print(root[1].attrib)
#print(root[2][1].text)
#for child in root:
#    print(child.tag, child.attrib)

file1 = r"CC:\Users\kartik.patel\OneDrive - Vertex, Inc\Desktop\respone 1\174848_US_NY_Yonkers_Calc_Guide_RO_Surcharge_Method_response.xml"
file2 = r"C:\Users\kartik.patel\OneDrive - Vertex, Inc\Desktop\respone 2\174848_US_NY_Yonkers_Calc_Guide_RO_Surcharge_Method_response.xml"
diff = filecmp.cmp('file1','file2')
