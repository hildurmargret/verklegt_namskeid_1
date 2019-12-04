
##def StaffInfo(inp):

import csv
from leitaStaff import leitaStaff

path='/Users/valdisbaerings/Documents/verklegt_namskeid_1/Documents/github/Verklegt1/UPDATEDSTUDENTDATA/'
skra='Crew.csv'

inp=1
inpt='Rhonda'

file=path+skra

ssn='yellow'
rank=''

with open(file,'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        if inp==1:
            lina=row['ssn']+row['name']+row['role']+row['rank']+row['licence']
            print(lina)
        elif inp==2:
            if row['role']=='Pilot':
                print(row['ssn'], row['name'], row['role'], row['rank'], row['licence'])
        elif inp==3:
            if row['role']=='Cabincrew':
                print(row['ssn'], row['name'], row['role'], row['rank'])
        elif inp==4:
            #inpt=input('Please enter the name or SSN of employee')
            ssn,rank=leitaStaff(inpt,file,ssn,rank)
            break
