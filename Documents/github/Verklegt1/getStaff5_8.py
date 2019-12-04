
import csv
from leitaStaff import leitaStaff

path='/Users/valdisbaerings/Documents/verklegt_namskeid_1/Documents/github/Verklegt1/UPDATEDSTUDENTDATA/'
skra1='PastFlights.csv'
file1=path+skra1

skra2='Crew.csv'
file2=path+skra2

inp=5
inpt='son'
ssn=[]
rank=[]

with open(file2,'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        ssn,rank=leitaStaff(inpt,file2,ssn,rank)
        for i in range(len(ssn)):
            if row['ssn']==ssn[i]:
                lina=row['ssn']+','+row['name']+','+row['role']+','+row['rank']+','+row['licence']
                print(lina)
                break

with open(file1,'r') as csvFile:
    reader=csv.DictReader(csvFile)
    for i in range(len(ssn)):
        for row in reader:
            if rank[i]=='Flight Attendant':
                if ssn[i] in row['fa1']:
                    print(row['arrivingAt'])
                if ssn[i] in row['fa2']:
                    print(row['arrivingAt'])
            elif rank[i]=='Flight Service Manager':
                if ssn[i] in row['fsm']:
                    print(row['arrivingAt'])
            elif rank[i]=='Captain':
                if ssn[i] in row['captain']:
                    print(row['arrivingAt'])
            elif rank[i]=='Copilot':
                if ssn[i] in row['copilot']:
                    print(row['arrivingAt'])
