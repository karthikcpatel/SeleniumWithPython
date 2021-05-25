#1. Convert below two lists into dictionary
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

sampleDict = dict(zip(keys, values))
print(sampleDict)

#2. Merge following two Python dictionaries into one
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

dict3 = dict1.copy()
dict3.update(dict2)
print(dict3)

#3. Access the value of key ‘history’ from the below dict
sampleDict = {
   "class":{
      "student":{
         "name":"Mike",
         "marks":{
            "physics":70,
            "history":80
         }
      }
   }
}

print(sampleDict['class']['student']['marks']['history'])

#5. Create a new dictionary by extracting the following keys from a below dictionary
# keys = ["name", "salary"]
# Expected output: {'name': 'Kelly', 'salary': 8000}
sampleDict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"

}
keys=["name","salary"]
for k in keys:
    newdict = {k,sampleDict[k]}
    #newdict = sampleDict.get[k]
    print(newdict)

#6. Delete set of keys from a dictionary
# Expected output: {'city': 'New york', 'age': 25}
sampleDict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"

}
keysToRemove = ["name", "salary"]

sampleDict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"}
keysToRemove = ["name", "salary"]
for i in keysToRemove:
    del sampleDict[i]
print(sampleDict)

#7. Check if a value 200 exists in a dictionary
sampleDict = {'a': 100, 'b': 200, 'c': 300}
print(200 in sampleDict.values())

sampleDict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}

#8. Rename key city to location in the following dictionary
sampleDict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}
sampleDict["location"] = sampleDict.pop("city")
print(sampleDict)

#9. Get the key of a minimum value from the following dictionary
sampleDict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}

print(min(sampleDict, key=sampleDict.get))

#10. Change Brad’s salary to 8500 from a given Python dictionary
sampleDict = {
     'emp1': {'name': 'Jhon', 'salary': 7500},
     'emp2': {'name': 'Emma', 'salary': 8000},
     'emp3': {'name': 'Brad', 'salary': 6500}
}

sampleDict['emp3']['salary'] = 8500
print(sampleDict)