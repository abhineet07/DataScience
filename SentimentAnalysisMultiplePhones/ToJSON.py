import json

def createFile(data):
    with open('Results.json', 'a') as json_file:
        json.dump(data, json_file)

def printingJSON(data):
    new_dict = json.loads(data)
    print(json.dumps(new_dict, indent=4, sort_keys=True))