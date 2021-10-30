import json

with open(r"C:\Miscellaneous\Software Testing Tutorials\Interview Questions & Answers\Miscellaneous Documents\samplejson.json") as file:
    json_data = json.load(file)
    print(json_data)
    json_all = json_data['Geeks']
    print(json_all)
    for list_names in json_all:
        print(list_names)
    first_medicine_list = (list_names['Geekname'])
    print(fsirst_medicine_list)