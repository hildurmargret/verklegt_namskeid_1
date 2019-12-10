import csv
from ModelClasses.Staff import*
def saveUpdatedCabin(employee):

    staff=[]
    path="/Users/palinakroyer/github/verklegt_namskeid_1/csvFiles/CrewCopy.csv"
    with open(path,'r') as File1:
        csv_reader = csv.DictReader(File1)
        for row in csv_reader:
            empl = createCabin(row['name'],row['ssn'],row['address'],row['phonenumber'],'email',row['rank'],row['role'])
            staff.append(empl)
    File1.close()

    f=open(path, 'w')

    writer = csv.writer(f)
    writer.writerow( ('ssn', 'name', 'role','rank','licence','address','phonenumber') )

    for i in range(len(staff)):
        if staff[i].SSN==employee.SSN:
            writer.writerow((employee.SSN,employee.name,employee.role,employee.rank,'N/A',employee.address,employee.phoneNumber))
        else:
            writer.writerow((staff[i].SSN,staff[i].name,staff[i].role,staff[i].rank,staff[i].licence,staff[i].address,staff[i].phoneNumber))
