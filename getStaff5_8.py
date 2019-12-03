
import csv
from leitaStaff import leitaStaff

path='/Users/valdisbaerings/Documents/verklegt_namskeid_1/Documents/github/Verklegt1/UPDATEDSTUDENTDATA/'
skra1='Destinations.csv'
file1=path+skra1

skra2='Crew.csv'
file2=path+skra2

inp=5

with open(file2,'r') as csvFile:
    reader=csv.DictReader(csvFile)
    for row in reader:
        if inp==5:
            #inpt=inpt('Please enter the name of employee to see all his/her destinations')
            emp=leitaStaff(inpt,file1)
            break
