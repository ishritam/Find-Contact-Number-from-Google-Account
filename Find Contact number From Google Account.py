import csv

with open('C:\\Users\\Shritam\\Desktop\\google.csv') as csvfile:
    readCSV = csv.reader(csvfile)

    name = []

    def nam():
        for i in readCSV:
            pri = list(readCSV)
        a = input("Enter The Name1: ")
        b = input("Enter The Name2: ")
        c = input("Enter The Name3: ")
        d = input("Enter The Name4: ")
        e = input("Enter The Name5: ")
        f = input("Enter The Name6: ")
        for j in pri:
            if j[0] == a or j[0] == b or j[0] == c or j[0] == d or j[0] == e or j[0] == f:
                pre = j
                de = list(filter(str.strip, pre))
                name.append(de)

        for i in name:
            print({i[0]: i[-1]})

    nam()
