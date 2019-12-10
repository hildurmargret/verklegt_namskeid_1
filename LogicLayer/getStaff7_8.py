from LogicLayer.Date import*
import csv
from ModelClasses.Staff import*

def emplWorking(inptDate):

    inptDay = str(inptDate[0:2])
    inptMonth = str(inptDate[3:5])
    inptYear = str(inptDate[6:10])

    standardDate = inptYear + '-'+ inptMonth + '-' + inptDay + 'T' + '00:00:00'

    path='/Users/valdisbaerings/Documents/github/verklegt_namskeid_1/csvFiles/'

    file2=path+'Crew.csv'

    today=now()

    if today>standardDate:
        file1=path+'PastFlights.csv'
    else:
        file1=path+'UpcomingFlights copy.csv'

    updemplSSN=[]
    working=[]
    emplSSN = []
    employees = []
    noemployees=[]
    emplDest=[]
    emplLOKA=[]

    with open(file1,'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            day = str(getDay(row['departure']))
            month = str(getMonth(row['departure']))
            year = str(getYear(row['departure']))

            if inptDay == day and inptMonth == month and inptYear == year:
                emplSSN.append(row['captain'])
                emplSSN.append(row['copilot'])
                emplSSN.append(row['fsm'])
                emplSSN.append(row['fa1'])
                emplSSN.append(row['fa2'])

    for i in emplSSN:
        if i not in updemplSSN:
            updemplSSN.append(i)

    with open(file2, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            for i in range(len(updemplSSN)):
                if row['ssn'] == updemplSSN[i]:
                    empl = createStaff(row['name'],row['ssn'],row['address'],row['phonenumber'],'email',row['rank'],row['role'], row['licence'])
                    employees.append(empl)

            if row['ssn'] not in updemplSSN:
                emp = createStaff(row['name'],row['ssn'],row['address'],row['phonenumber'],'email',row['rank'],row['role'], row['licence'])
                noemployees.append(emp)

    with open(file1,'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            day = str(getDay(row['departure']))
            month = str(getMonth(row['departure']))
            year = str(getYear(row['departure']))

            if inptDay == day and inptMonth == month and inptYear == year:
                for i in range(len(employees)):
                    if employees[i].rank == 'Captain' and row['captain'] == employees[i].SSN and row['arrivingAt'] != 'KEF':
                        emplDest.append(row['arrivingAt'] + employees[i].SSN)
                    elif employees[i].rank == 'Copilot' and row['copilot'] == employees[i].SSN and row['arrivingAt'] != 'KEF':
                        emplDest.append(row['arrivingAt'] + employees[i].SSN)
                    elif employees[i].rank == 'Flight Service Manager' and row['fsm'] == employees[i].SSN and row['arrivingAt'] != 'KEF':
                        emplDest.append(row['arrivingAt'] + employees[i].SSN)
                    elif employees[i].rank == 'Flight Attendant' and (row['fa1'] == employees[i].SSN or row['fa2'] == employees[i].SSN) and row['arrivingAt'] != 'KEF':
                        emplDest.append(row['arrivingAt'] + employees[i].SSN)

    with open(file2, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            for i in range(len(emplDest)):
                if row['ssn'] == str(emplDest[i][3:len(emplDest[i])]):
                    emplLOKA.append(row['name'] + ', ' + row['role'] + ' - ' + str(emplDest[i][0:3]))

    return employees, noemployees, emplLOKA
