
# defstaffInfo2(inp):

import csv
from leitaStaff import leitaStaff

path='/Users/hildur/Documents/github/verklegt_namskeid_1/Documents/github/Verklegt1/UPDATEDSTUDENTDATA/'
skra1='PastFlights.csv'
file1=path+skra1

skra2='Crew.csv'
file2=path+skra2

inpt='son'
ssn=[]
rank=[]
dest=[]
linur=[]
fjoldiAfStad=[]

with open(file2,'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        ssn,rank=leitaStaff(inpt,file2,ssn,rank)
        for i in range(len(ssn)):
            if row['ssn']==ssn[i]:
                lina=row['ssn']+', '+row['name']+', '+row['role']+', '+row['rank']+', '+row['licence']
                linur.append(lina)
                #print(lina)
                break

for i in range(len(linur)):
    with open(file1,'r') as csvFile:
        reader=csv.DictReader(csvFile)
        for row in reader:
            if rank[i]=='Flight Attendant':
                if ssn[i] in row['fa1'] and row['arrivingAt']!='KEF':
                    dest.append(row['arrivingAt'])
                if ssn[i] in row['fa2'] and row['arrivingAt']!='KEF':
                    dest.append(row['arrivingAt'])
            elif rank[i]=='Flight Service Manager':
                if ssn[i] in row['fsm'] and row['arrivingAt']!='KEF':
                    dest.append(row['arrivingAt'])
            elif rank[i]=='Captain':
                if ssn[i] in row['captain'] and row['arrivingAt']!='KEF':
                    dest.append(row['arrivingAt'])
            elif rank[i]=='Copilot':
                if ssn[i] in row['copilot'] and row['arrivingAt']!='KEF':
                    dest.append(row['arrivingAt'])
        fjoldiAfStad.append(len(dest))

#Prentun, þarf að setja annars staðar
counter = 0
for j in range(len(fjoldiAfStad)):
    print linur[j]
    for i in range(fjoldiAfStad[j]-counter):
        print(dest[i+counter])
    counter=fjoldiAfStad[j]
    print
