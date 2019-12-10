import csv
from ModelClasses.Staff import *

def read_crew_file(file_name):

    allStaff=[]

    with file_name as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            empl = createStaff(row['name'],row['ssn'],row['address'],row['phonenumber'],'email',row['rank'],row['role'],row['licence'])
            allStaff.append(empl)

    return allStaff
