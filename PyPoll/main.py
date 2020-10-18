# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.

import os
import csv

PyPoll_csv = os.path.join("python-challenge","PyPoll",'Resources','election_data.csv')

f = open("python-challenge/PyPoll/Analysis/Analysis.txt", "w")

print("Election Results",file=f)
print("-------------------------",file=f)
with open(PyPoll_csv, 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    header = next(csv_reader)
    NofV= len(list(csv_reader))
    print("Total Votes:",NofV,file=f)
print("-------------------------",file=f)
    
with open(PyPoll_csv, 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    header = next(csv_reader)
    name = []
    percentage = {}
    for row in csv_reader:
        name.append(row[2])
    name.sort()
    for x in range(0,NofV):
        if name[x] != name[int(x)-1]:
            percentage[name[x]] = name.count(name[x])/int(NofV)
            print(name[x],": ","{:.3%}".format(percentage[name[x]]),"({:})".format(name.count(name[x])),file=f)
    print("-------------------------",file=f)
    print("Winner: ",max(percentage,key = percentage.get),file=f)
    print("-------------------------",file=f)

