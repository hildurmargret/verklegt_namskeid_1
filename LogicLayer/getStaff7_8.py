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
    emplSSN = []
    employees = []
    noemployees=[]
    emplDest=[]

    #Past flights
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
                emplDest.append(row['arrivingAt'])

    for i in emplSSN:
        if i not in updemplSSN:
            updemplSSN.append(i)



    with open(file2, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            for i in range(len(updemplSSN)):
                if row['ssn'] == updemplSSN[i]:
                    if row['licence'] == 'N/A':
                        empl = createCabin(row['name'],row['ssn'],row['address'],row['phonenumber'],'email',row['rank'],row['role'])
                        employees.append(empl)
                    else:
                        empl = createPilot(row['name'],row['ssn'],row['address'],row['phonenumber'],'email',row['rank'],row['role'],row['licence'])
                        employees.append(empl)

    with open(file2, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            if row['ssn'] not in updemplSSN:
                if row['licence'] == 'N/A':
                    emp = createCabin(row['name'],row['ssn'],row['address'],row['phonenumber'],'email',row['rank'],row['role'])
                    noemployees.append(emp)
                else:
                    emp = createPilot(row['name'],row['ssn'],row['address'],row['phonenumber'],'email',row['rank'],row['role'],row['licence'])
                    noemployees.append(emp)

    return employees, noemployees
