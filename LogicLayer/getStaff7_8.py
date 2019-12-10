from LogicLayer.Date import*
import csv
from ModelClasses.Staff import*

def emplWorking(inptDate):

    #inptDate = '10/11/2019'
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

    #print(today)
    updemplSSN=[]
    working=[]
    emplSSN = []
    employees = []
    noemployees=[]
    emplDest=[]
    emplLOKA=[]

    #Past flights
    with open(file1,'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            day = str(getDay(row['departure']))
            month = str(getMonth(row['departure']))
            year = str(getYear(row['departure']))

            if inptDay == day and inptMonth == month and inptYear == year:
                #empl=empAndDest(row['captain'], row['arrivingAt'])
                #working.append(empl)
                emplSSN.append(row['captain']) #+ row['arrivingAt'])
                emplSSN.append(row['copilot']) #+ row['arrivingAt'])
                emplSSN.append(row['fsm']) #+ row['arrivingAt'])
                emplSSN.append(row['fa1']) #+ row['arrivingAt'])
                emplSSN.append(row['fa2']) #+ row['arrivingAt'])
                #emplDest.append(row['arrivingAt'])

    for i in emplSSN:
        if i not in updemplSSN:
            updemplSSN.append(i)

    with open(file2, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            for i in range(len(updemplSSN)):
                if row['ssn'] == updemplSSN[i]:
                    #print(row['ssn'])
                    #if row['licence'] == 'N/A':
                    empl = createStaff(row['name'],row['ssn'],row['address'],row['phonenumber'],'email',row['rank'],row['role'], row['licence'])
                    employees.append(empl)
                    #else:
                    #    empl = createPilot(row['name'],row['ssn'],row['address'],row['phonenumber'],'email',row['rank'],row['role'],row['licence'])
                    #    employees.append(empl)
            if row['ssn'] not in updemplSSN:
                #if row['licence'] == 'N/A':
                emp = createStaff(row['name'],row['ssn'],row['address'],row['phonenumber'],'email',row['rank'],row['role'], row['licence'])
                noemployees.append(emp)
                #else:
                #    emp = createPilot(row['name'],row['ssn'],row['address'],row['phonenumber'],'email',row['rank'],row['role'],row['licence'])
                #    noemployees.append(emp)

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
                        #print(employees[i].name)
                    elif employees[i].rank == 'Flight Attendant' and (row['fa1'] == employees[i].SSN or row['fa2'] == employees[i].SSN) and row['arrivingAt'] != 'KEF':
                        emplDest.append(row['arrivingAt'] + employees[i].SSN)


    #print(str(emplDest[0][3:len(emplDest)]))

    with open(file2, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            for i in range(len(emplDest)):
                if row['ssn'] == str(emplDest[i][3:len(emplDest[i])]):
                    emplLOKA.append(row['name'] + ', ' + row['role'] + ' - ' + str(emplDest[i][0:3]))


    #for i in range(len(employees)):
    #    print(employees[i].name)
    #print(emplDest)
    #print(len(employees))
    #print(emplLOKA)

    #for i in range(len(employees)):
    #    print(employees[i].name)

    #for i in range(len(noemployees)):
    #    print(noemployees[i].name)

    return employees, noemployees, emplLOKA

# class empAndDest():
#
#     def __init__(self, employee, destination):
#         self.employee=employee
#         self.destination=destination
