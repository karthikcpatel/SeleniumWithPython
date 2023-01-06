import xml.etree.ElementTree as obj

def updateXML(filename):
    tree = obj.ElementTree(file=filename)
    root = tree.getroot()

    for paydate in root.iter("PAYDATE"):
        paydate.text = "20230101"

    tree = obj.ElementTree(root)

    with open(filename,"wb") as fileupdate:
        tree.write(fileupdate)

updateXML(r'C:\Users\kartik.patel\PycharmProjects\SeleniumWithPython\file handling\test data\175328_W4.xml')