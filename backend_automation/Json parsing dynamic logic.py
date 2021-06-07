import json

with open(r"C:\Work\Software Testing Tutorials\Web Services\API Automation\sample json for practise.json") as file:
    json_data = json.load(file)
    print(json_data)
    json_medications = json_data['medications']
    print(json_medications)
    for list_medicines in json_medications:
        print(list_medicines)
    first_medicine_list = (list_medicines['aceInhibitors'])
    for x in first_medicine_list:
        if x['name'] == 'lisinopril':
            print(x['price'])
        else:
            print("Unable to search the medicine")