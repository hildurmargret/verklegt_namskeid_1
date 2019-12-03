
##def StaffInfo(inp):

import csv
from leitaStaff import leitaStaff

path='/Users/valdisbaerings/Documents/verklegt_namskeid_1/Documents/github/Verklegt1/UPDATEDSTUDENTDATA/'
skra='Crew.csv'

inp=4
inpt='Rhonda'

file=path+skra

with open(file,'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        if inp==1:
            print(row['ssn'], row['name'], row['role'], row['rank'], row['licence'])
        elif inp==2:
            if row['role']=='Pilot':
                print(row['ssn'], row['name'], row['role'], row['rank'], row['licence'])
        elif inp==3:
            if row['role']=='Cabincrew':
                print(row['ssn'], row['name'], row['role'], row['rank'])
        elif inp==4:
            #inpt=input('Please enter the name or SSN of employee')
            ssn=leitaStaff(inpt,file)
            #print(ssn)
            break
