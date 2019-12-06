import csv
from getStaff1_4 import staffInfo

path='/Users/hildur/Documents/github/verklegt_namskeid_1/Documents/github/Verklegt1/UPDATEDSTUDENTDATA/'
fileName = 'CrewCopy.csv'

file = path + fileName

file1 = open(file, "w")

inp_ssn = '3009907461'
inpt = 'Buland 1'
fieldnames = ['ssn']

with file1 as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    employees = staffInfo(1)

    csv_writer.writeheader()

    #for rows in employees:
    csv_writer.writerow(employees['ssn'][0])
