import csv
from ModelClasses.Staff import*
import sys
import os
def saveUpdatedStaff(employee):

    #fallið opnar skrá og skrifar inn uppfærðar upplýsingar

    staff=[]
    ##path="/Users/valdisbaerings/Documents/github/verklegt_namskeid_1/csvFiles/CrewCopy.csv"

    file = OpenFile('CrewCopy.csv')

    with file as File1:
        csv_reader = csv.DictReader(File1)
        for row in csv_reader:
            empl = createStaff(row['name'],row['ssn'],row['address'],row['phonenumber'],'email',row['rank'],row['role'], row['licence'])
            staff.append(empl)
    File1.close()

    absPathFile = os.path.abspath(__file__)
    fileDir = os.path.dirname(os.path.abspath(__file__))
    parentDir = os.path.dirname(fileDir)
    path = parentDir + "/csvFiles/CrewCopy.csv"

    f=open(path, 'w')

    writer = csv.writer(f)
    writer.writerow( ('ssn', 'name', 'role','rank','licence','address','phonenumber') )

    for i in range(len(staff)):
        if staff[i].SSN==employee.SSN:
            writer.writerow((employee.SSN,employee.name,employee.role,employee.rank,employee.licence,employee.address,employee.phoneNumber))
        else:
            writer.writerow((staff[i].SSN,staff[i].name,staff[i].role,staff[i].rank,staff[i].licence,staff[i].address,staff[i].phoneNumber))
