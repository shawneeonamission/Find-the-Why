import time
import numpy as np
import csv

Operations = np.array([0, 0])
Finance = np.array([0, 0])
Sales = np.array([0, 0])
IT = np.array([0, 0])
Executive = np.array([0, 0])
HR = np.array([0, 0])
lines = 0
string = ""

d = open("departments", "w")
e = open("enjoyment", "w")

rows = []
column = 0


data = open("Quantum Workplace - Sample Survey Data.csv", "r")
reader = csv.reader(data)
fields = next(reader)

for row in reader:
    rows.append(row)

print("Finished Parsing Rows")

for row in rows:
    # parsing each column of a row
    for col in row:
        if column == 3:
            d.write(str(col))
            d.write('\n')
        if column == 19:
            e.write(str(col))
            e.write('\n')
        column = column + 1
    column = 0

print("Finished Parsing Columns")

d = open("departments", "r")
e = open("enjoyment", "r")

enjoyment_lines = e.readlines()

list_of_lines = d.readlines()
for line in list_of_lines:
    string = str(enjoyment_lines[lines])

    if "Operations" in line:
        try:
            float(string)

            Operations[1] = Operations[1] + float(string)
            Operations[0] = Operations[0] + 1
        except ValueError:
            time.sleep(0.000000000000000000000000001)

    elif "Finance" in line:
        try:
            float(string)

            Finance[1] = Finance[1] + float(string)
            Finance[0] = Finance[0] + 1
        except ValueError:
            time.sleep(0.000000000000000000000000001)

    elif "Sales" in line:
        try:
            float(string)

            Sales[1] = Sales[1] + float(string)
            Sales[0] = Sales[0] + 1
        except ValueError:
            time.sleep(0.000000000000000000000000001)

    elif "Information Technology" in line:
        try:
            float(string)

            IT[1] = IT[1] + float(string)
            IT[0] = IT[0] + 1
        except ValueError:
            time.sleep(0.000000000000000000000000001)

    elif "Executive" in line:
        try:
            float(string)

            Executive[1] = Executive[1] + float(string)
            Executive[0] = Executive[0] + 1
        except ValueError:
            time.sleep(0.000000000000000000000000001)

    elif "HR" in line:
        try:
            float(string)

            HR[1] = HR[1] + float(string)
            HR[0] = HR[0] + 1
        except ValueError:
            time.sleep(0.000000000000000000000000001)

    lines = lines + 1

print("Finished Sorting Answers")

Operations = Operations.astype(np.float)
Finance = Finance.astype(np.float)
Sales = Sales.astype(np.float)
IT = IT.astype(np.float)
Executive = Executive.astype(np.float)
HR = HR.astype(np.float)

if float(Operations[0]) > 0:
    Operations[1] = float(Operations[1]) / float(Operations[0])
    time.sleep(0.000000000000000000000000001)
else:
    time.sleep(0.000000000000000000000000001)
if float(Finance[0]) > 0:
    Finance[1] = float(Finance[1]) / float(Finance[0])
else:
    time.sleep(0.000000000000000000000000001)
if float(Sales[0]) > 0:
    Sales[1] = float(Sales[1]) / float(Sales[0])
else:
    time.sleep(0.000000000000000000000000001)
if float(IT[0]) > 0:
    IT[1] = float(IT[1]) / float(IT[0])
else:
    time.sleep(0.000000000000000000000000001)
if float(Executive[0]) > 0:
    Executive[1] = float(Executive[1]) / float(Executive[0])
else:
    time.sleep(0.000000000000000000000000001)
if float(HR[0]) > 0:
    HR[1] = float(HR[1]) / float(HR[0])
else:
    time.sleep(0.000000000000000000000000001)

print("Finished Calculating Averages")

r = open("results", "w")

r.write("Average Enjoyment Score of Everyone that "
        "finished the survey in the Operations Department is " + str(float(Operations[1])) + "\n")
r.write("Average Enjoyment Score of Everyone that "
        "finished the survey in the Finance Department is " + str(Finance[1]) + "\n")
r.write("Average Enjoyment Score of Everyone that finished the survey in the Sales Department is " + str(Sales[1]) + "\n")
r.write("Average Enjoyment Score of Everyone that "
        "finished the survey in the Information Technology Department is " + str(IT[1]) + "\n")
r.write("Average Enjoyment Score of Everyone that "
        "finished the survey in the Executive Department is " + str(Executive[1]) + "\n")
r.write("Average Enjoyment Score of Everyone that finished the survey in the HR Department is " + str(HR[1]) + "\n")
