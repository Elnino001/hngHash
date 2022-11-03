
import csv
import json
from math import e
import hashlib


# Get file paths
csvFilePath = input("Enter csv file path: ")
jsonFilePath = input("Enter json file location: ")

csv_file = open(csvFilePath, 'r', encoding='utf-8')
csv_reader = csv.DictReader(csv_file)

icount = 0
list_of_json = []
for row in csv_reader:
    out = json.dumps(row, indent=4)
    #save the json
    jsonOutPut = open(jsonFilePath + str(icount)+ '.json', 'w', encoding='utf-8')
    p = jsonOutPut.write(out)
    hashString = hashlib.sha256(str(p).encode()).hexdigest()
    g=dict(row)
    g["HASH"]= hashString
    list_of_json.append(g)
    icount+=1

jsonOutPut.close()
csv_file.close()

myfile = open("output.csv", 'w')
writer = csv.DictWriter(myfile, fieldnames=["Series Number", "Filename", 'Name', "Description", "Gender", "Attributes", "UUID", "HASH"])
writer.writeheader()
writer.writerows(list_of_json)
myfile.close()

myfile = open('output.csv', 'r')
myfile.read()
myfile.close()




