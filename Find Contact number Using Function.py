import csv
import re
with open('C:\\Users\\Shritam\\Desktop\\google.csv') as csvfile:
    readCSV = csv.reader(csvfile)
    for i in readCSV:
        pri = list(readCSV)
    name = []
    num = []
    for j in pri:
        if j[0] == 'Swarazz' or j[0] == 'Rohan' or j[0] == 'Lucky' or j[0] == 'Chandan' or j[0] == 'Sid'or j[0] == 'Jayanta':
            pre = j

            de = list(filter(str.strip, pre))
            name.append(de)

    for i in name:
        print({i[0]: i[-1]})
