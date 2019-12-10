import csv
from LogicLayer.leitaStaff import *
from UILayer.printWorkSchedule import*
from DataLayer.saveWorkSchedule import*
from LogicLayer.Date import*
from ModelClasses.Staff import *
from ModelClasses.Voyage import *
from DataLayer.OpenFile import *
from DataLayer.read_crew_file import *
from DataLayer.read_pastFlights import *

def staffInfo2(input_string):

    skra1='Crew.csv'
    skra2='PastFlights.csv'
    skra3='UpcomingFlights.csv'

    file1=OpenFile(skra1)
    allStaff=read_crew_file(file1)

    ssn=[]
    rank=[]
    employees=[]
    numOfDest=[]
    pastFlights=[]
    upcFlights=[]

    for i in range(len(allStaff)):
        ssn, rank = leitaStaff(input_string, allStaff, ssn, rank)
        for j in range(len(ssn)):
            if allStaff[i].SSN == ssn[j]:
                empl = createStaff(allStaff[i].name, allStaff[i].SSN, allStaff[i].address, allStaff[i].phoneNumber,allStaff[i].emailAddress,allStaff[i].rank,allStaff[i].role,allStaff[i].licence)
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

    file2=OpenFile(skra2) #pastFlights

    allPastFlights=read_pastFlights(file2)

    #Past flights
    for i in range(len(employees)):
        for j in range(len(allPastFlights)):

            deptTime = str(getDay(allPastFlights[j].departure)) + '/' + str(getMonth(allPastFlights[j].departure)) + '/' + str(getYear(allPastFlights[j].departure)) + ' at ' + str(getHour(allPastFlights[j].departure)) + ':' + str(getMinute(allPastFlights[j].departure))
            arvlTime = str(getDay(allPastFlights[j].arrival)) + '/' + str(getMonth(allPastFlights[j].arrival)) + '/' + str(getYear(allPastFlights[j].arrival)) + ' at ' + str(getHour(allPastFlights[j].arrival)) + ':' + str(getMinute(allPastFlights[j].arrival))

            if employees[i].rank=='Flight Attendant' and employees[i].SSN in (allPastFlights[j].fa1 or allPastFlights[j].fa2):
                flight=createVoyage(allPastFlights[j].flightNumber, allPastFlights[j].departingFrom, allPastFlights[j].arrivingAt, deptTime, arvlTime,0,0)
                pastFlights.append(flight)

            elif employees[i].rank=='Flight Service Manager' and employees[i].SSN in allPastFlights[j].fsm:
                flight=createVoyage(allPastFlights[j].flightNumber, allPastFlights[j].departingFrom, allPastFlights[j].arrivingAt, deptTime, arvlTime,0,0)
                pastFlights.append(flight)

            elif employees[i].rank=='Captain' and employees[i].SSN in allPastFlights[j].captain:
                flight=createVoyage(allPastFlights[j].flightNumber, allPastFlights[j].departingFrom, allPastFlights[j].arrivingAt, deptTime, arvlTime,0,0)
                pastFlights.append(flight)

            elif employees[i].rank=='Copilot' and employees[i].SSN in allPastFlights[j].copilot:
                flight=createVoyage(allPastFlights[j].flightNumber, allPastFlights[j].departingFrom, allPastFlights[j].arrivingAt, deptTime, arvlTime,0,0)
                pastFlights.append(flight)

        numOfDest.append(len(pastFlights))

    return numOfDest, pastFlights, upcFlights, employees
