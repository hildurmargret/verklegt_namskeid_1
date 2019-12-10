from ModelClasses.Staff import*
import csv
def searchPilotsByLicence(airplaneType):

    path='/Users/hildur/Documents/github/verklegt_namskeid_1/csvFiles/'

    file1 = path + 'Crew.csv'

    pilots = []

    with open(file1,'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            if row['role']=='Pilot' and row['licence']==airplaneType:
                emp = createStaff(row['name'],row['ssn'],row['address'],row['phonenumber'],'email',row['rank'],row['role'],row['licence'])
                pilots.append(emp)

    return pilots
