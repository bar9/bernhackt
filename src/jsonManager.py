import sys, json, hashlib
from sys import argv, stdout
data = ""

class jsonManager:
    
    data

    def __init__(self):
        with open('output.json', 'r') as f:
            self.data = json.load(f)

    def setField(self, filePath, variableName, value):
        self.data[filePath][variableName] = value
        with open('output.json', 'w') as outfile:
            json.dump(data, outfile)

    def getField(self, filePath, variableName):
        return self.data[filePath][variableName]

    def newFile(self, filePath):
        new={console_input: {"blockchain_status": "pending", "confirmation_date:": "", "transaction_id": "", "is_tracked": 1, "verified_hash": "", "calculated_hash:": get_hash(console_input)}}
        self.data.append(new)

        with open('output.json', 'w') as outfile:
            json.dump(self.data, outfile)   

    

    