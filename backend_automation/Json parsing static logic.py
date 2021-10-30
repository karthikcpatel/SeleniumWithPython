import json

with open(r"C:\Miscellaneous\Software Testing Tutorials\Interview Questions & Answers\Miscellaneous Documents\samplejson.json") as file:
    json_data = json.load(file)
    print(json_data)
    json_all = json_data['Geeks']
    print(json_all)
    json_outer = json_all[0]
    print(json_outer)
    json_inner = json_outer['Geekname']
    print(json_inner)