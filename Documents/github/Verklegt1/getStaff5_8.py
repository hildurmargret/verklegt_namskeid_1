
import csv
from leitaStaff import leitaStaff

path='/Users/valdisbaerings/Documents/verklegt_namskeid_1/Documents/github/Verklegt1/UPDATEDSTUDENTDATA/'
skra1='PastFlights.csv'
file1=path+skra1

skra2='Crew.csv'
file2=path+skra2

inp=5
inpt='son'
ssn=''
rank=''

with open(file2,'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        ssn,rank=leitaStaff(inpt,file2,ssn,rank)
        if row['ssn']==ssn:
            lina=row['ssn']+','+row['name']+','+row['role']+','+row['rank']+','+row['licence']
            print(lina)


with open(file1,'r') as csvFile:
    reader=csv.DictReader(csvFile)
    for row in reader:
        if rank=='Flight Attendant':
            if ssn in row['fa1']:
                print(row['arrivingAt'])
            if ssn in row['fa2']:
                print(row['arrivingAt'])
        if rank=='Flight Service Manager':
            if ssn in row['fsm']:
                print(row['arrivingAt'])
        if rank=='Captain':
            if ssn in row['captain']:
                print(row['arrivingAt'])
        if rank=='Copilot':
            if ssn in row['copilot']:
                print(row['arrivingAt'])
