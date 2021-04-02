import json

with open(r"C:\Work\Software Testing Tutorials\Web Services\API Automation\sample json for practise.json") as file:
    json_data = json.load(file)
    print(json_data)
    json_medications = json_data['medications']
    print(json_medications)
    json_aceInhibitors_li = json_medications[0]
    print(json_aceInhibitors_li)
    json_aceInhibitors_dict = json_aceInhibitors_li['aceInhibitors']
    print(json_aceInhibitors_dict)
    json_medications_name_li = json_aceInhibitors_dict[0]
    print(json_medications_name_li)
    json_medications_name_dict = json_medications_name_li['name']
    print(json_medications_name_dict)