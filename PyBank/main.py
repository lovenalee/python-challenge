# Questions
# The total number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period
# The average of the changes in "Profit/Losses" over the entire period
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period

import os
import csv
PyBank_csv = os.path.join("python-challenge","Pybank",'Resources','budget_data.csv')
print("Financial Analysis")
print("----------------------------")
with open(PyBank_csv, 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    header = next(csv_reader)
    NofM = len(list(csv_reader))
    print("Total Months: ",NofM)
    
with open(PyBank_csv, 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    header = next(csv_reader)
    total = 0
    for x in csv.reader(csvfile):
        total += int(x[1])
    
    print("Total: ","$" + str(total))
    
with open(PyBank_csv, 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    header = next(csv_reader)
    a = []
    b = []
    diff = []
    total_diff = 0
    for row in csv_reader:
        a.append(row[1])
        b.append(row[0])  
    for d in range(0,int(NofM)-1):
        diff.append(int(a[int(d)+1])-int(a[int(d)]))
        total_diff += int(a[int(d)+1])-int(a[int(d)])
    print("Average  Change: ","$"+str(round(float(total_diff/len(diff)),2)))
    Max_Diff = max(diff)
    Min_Diff = min(diff)
    for c in range (0,int(NofM)-2):
        if diff[c] == Max_Diff:
            print("Greatest Increase in Profits: ",b[int(c)+1], "("+"$"+str(diff[c])+")")
        elif diff[c] == Min_Diff:
            print("Greatest Decrease in Profits: ",b[int(c)+1], "("+"$"+str(diff[c])+")")
    

