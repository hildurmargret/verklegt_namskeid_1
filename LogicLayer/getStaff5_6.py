import csv
from LogicLayer.leitaStaff import *
from UILayer.printWorkSchedule import*
from DataLayer.saveWorkSchedule import*
from LogicLayer.Date import*
from ModelClasses.Staff import *
from ModelClasses.Voyage import *

def staffInfo2(number, input_string):

    path='/Users/hildur/Documents/github/verklegt_namskeid_1/csvFiles/'
    skra1='PastFlights.csv'
    file1=path+skra1

    skra2='Crew.csv'
    file2=path+skra2
    file3=path+'UpcomingFlights.csv'

    ssn=[]
    rank=[]
    pastDest=[]
    pastDept=[]
    pastDeptTime=[]
    pastArvlTime=[]
    upcDest=[]
    upcDept=[]
    upcDeptTime=[]
    upcArvlTime=[]
    pastFlNo=[]
    employees=[]
    numOfDest=[]
    pastFlights=[]
    upcFlights=[]

    with open(file2,'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            ssn,rank=leitaStaff(input_string,file2,ssn,rank)
            for i in range(len(ssn)):
                if row['ssn']==ssn[i]:
                    if row['role'] == 'Cabincrew':
                        empl = createCabin(row['name'],row['ssn'],row['address'],row['phonenumber'],'email',row['rank'],row['role'])
                        employees.append(empl)
                    else:
                        empl = createPilot(row['name'],row['ssn'],row['address'],row['phonenumber'],'email',row['rank'],row['role'],row['licence'])
                        employees.append(empl)
                    break

    """#Upcoming flights
    for i in range(len(employees)):
        with open(file3,'r') as csvFile:
            reader=csv.DictReader(csvFile)
            for row in reader:
                if rank[i]=='Flight Attendant' and ssn[i] in (row['fa1'] or row['fa2']):
                    upcDeptTime.append(row['departure'])
                    upcArvlTime.append(row['arrival'])
                    upcFlNo.append(row['flightNumber'])
                    upcDest.append(row['arrivingAt'])
                    upcDept.append(row['departingFrom'])
                elif rank[i]=='Flight Service Manager' and ssn[i] in row['fsm']:
                    upcDeptTime.append(row['departure'])
                    upcArvlTime.append(row['arrival'])
                    upcFlNo.append(row['flightNumber'])
                    upcDest.append(row['arrivingAt'])
                    upcDept.append(row['departingFrom'])
                elif rank[i]=='Captain' and ssn[i] in row['captain']:
                    upcDeptTime.append(row['departure'])
                    upcArvlTime.append(row['arrival'])
                    upcFlNo.append(row['flightNumber'])
                    upcDest.append(row['arrivingAt'])
                    upcDept.append(row['departingFrom'])
                elif rank[i]=='Copilot' and ssn[i] in row['copilot']:
                    upcDeptTime.append(row['departure'])
                    upcArvlTime.append(row['arrival'])
                    upcFlNo.append(row['flightNumber'])
                    upcDest.append(row['arrivingAt'])
                    upcDept.append(row['departingFrom'])"""

    #Past flights
    for i in range(len(employees)):
        with open(file1,'r') as csvFile:
            reader=csv.DictReader(csvFile)
            for row in reader:
                deptTime = str(getDay(row['departure'])) + '/' + str(getMonth(row['departure'])) + '/' + str(getYear(row['departure'])) + ' at ' + str(getHour(row['departure'])) + ':' + str(getMinute(row['departure']))
                arvlTime = str(getDay(row['arrival'])) + '/' + str(getMonth(row['arrival'])) + '/' + str(getYear(row['arrival'])) + ' at ' + str(getHour(row['arrival'])) + ':' + str(getMinute(row['arrival']))

                if rank[i]=='Flight Attendant' and ssn[i] in (row['fa1'] or row['fa2']):
                    flight=createVoyage(row['flightNumber'], row['departingFrom'], row['arrivingAt'], deptTime, arvlTime,0,0)
                    pastFlights.append(flight)

                    # pastDeptTime.append(row['departure'])
                    # pastArvlTime.append(row['arrival'])
                    # pastFlNo.append(row['flightNumber'])
                    # pastDest.append(row['arrivingAt'])
                    # pastDept.append(row['departingFrom'])
                elif rank[i]=='Flight Service Manager' and ssn[i] in row['fsm']:
                    flight=createVoyage(row['flightNumber'], row['departingFrom'], row['arrivingAt'], deptTime, arvlTime,0,0)
                    pastFlights.append(flight)

                    # pastDeptTime.append(row['departure'])
                    # pastArvlTime.append(row['arrival'])
                    # pastFlNo.append(row['flightNumber'])
                    # pastDest.append(row['arrivingAt'])
                    # pastDept.append(row['departingFrom'])
                elif rank[i]=='Captain' and ssn[i] in row['captain']:
                    flight=createVoyage(row['flightNumber'], row['departingFrom'], row['arrivingAt'], deptTime, arvlTime,0,0)
                    pastFlights.append(flight)

                    # pastDeptTime.append(row['departure'])
                    # pastArvlTime.append(row['arrival'])
                    # pastFlNo.append(row['flightNumber'])
                    # pastDest.append(row['arrivingAt'])
                    # pastDept.append(row['departingFrom'])
                elif rank[i]=='Copilot' and ssn[i] in row['copilot']:
                    flight=createVoyage(row['flightNumber'], row['departingFrom'], row['arrivingAt'], deptTime, arvlTime,0,0)
                    pastFlights.append(flight)

                    # pastDeptTime.append(row['departure'])
                    # pastArvlTime.append(row['arrival'])
                    # pastFlNo.append(row['flightNumber'])
                    # pastDest.append(row['arrivingAt'])
                    # pastDept.append(row['departingFrom'])

            #numOfDest.append(len(pastDest))
            numOfDest.append(len(pastFlights))

    return numOfDest, pastFlights, upcFlights, employees
