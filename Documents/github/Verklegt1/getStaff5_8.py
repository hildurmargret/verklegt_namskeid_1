
import csv
from leitaStaff import leitaStaff

path='/Users/valdisbaerings/Documents/verklegt_namskeid_1/Documents/github/Verklegt1/UPDATEDSTUDENTDATA/'
skra1='Destinations.csv'
file1=path+skra1

skra2='Crew.csv'
file2=path+skra2

inp=5
inpt='Rhonda'

with open(file1,'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        ssn=leitaStaff(inpt,file1)
        break


with open(file2,'r') as csvFile:
    reader=csv.DictReader(csvFile)
    for row in reader:
        if inp==5:
            if ssn in row['ssn']:
