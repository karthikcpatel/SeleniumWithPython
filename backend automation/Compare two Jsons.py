import json

with open(r"C:\Work\Software Testing Tutorials\Web Services\API Automation\sample json for practise.json") as file1:
    json_data_1 = json.load(file1)
    print(json_data_1)

with open(r"C:\Work\Software Testing Tutorials\Web Services\API Automation\sample json for practise copy.json") as file2:
    json_data_2 = json.load(file2)
    print(json_data_2)

assert json_data_1 == json_data_2