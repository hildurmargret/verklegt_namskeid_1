import csv
from LogicLayer.leitaStaff import *
from UILayer.printWorkSchedule import*
from DataLayer.saveWorkSchedule import*
from LogicLayer.Date import*
from ModelClasses.Staff import *
from ModelClasses.flightRoute import *
from DataLayer.OpenFile import *
from DataLayer.read_crew_file import *
from DataLayer.read_pastFlights import *

def staffInfo2(input_string):

    skra1='CrewCopy.csv'
    skra2='PastFlights copy.csv'
    skra3='UpcomingFlights copy3.csv'

    skra=OpenFile(skra1)

    allStaff=read_crew_file(skra) #listi allra starfsmanna

    ssn=[]
    rank=[]
    employees=[]
    numOfupcDest=[]
    numOfpastDest=[]
    pastFlights=[]
    upcFlights=[]

    for i in range(len(allStaff)): #fer í gegnum alla starfsmenn
        ssn, rank = leitaStaff(input_string, allStaff, ssn, rank) #skilar listum af kennitölum og rank starfsm sem passa við input
        for j in range(len(ssn)): #fer i gegnum listann ssn
            if allStaff[i].SSN == ssn[j]: #ber saman kennitölur ur báðum listum og by til kasatilvik af starfsmönnum sem passa við input
                empl = createStaff(allStaff[i].name, allStaff[i].SSN, allStaff[i].address, allStaff[i].phoneNumber,allStaff[i].emailAddress,allStaff[i].rank,allStaff[i].role,allStaff[i].licence)
                employees.append(empl) #by til lista af öllum starfsmönnum sem passa við inputið
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

    allUpcFlights=read_pastFlights(skra3) #öll upcomingflights

    #Upcoming flights
    for i in range(len(employees)): #fer í gegnum alla starfsmenn sem passa við input
        for j in range(len(allUpcFlights)): #í gegnum öll upcoming flights

            deptTime = str(getDay(allUpcFlights[j].departure)) + '/' + str(getMonth(allUpcFlights[j].departure)) + '/' + str(getYear(allUpcFlights[j].departure)) + ' at ' + str(getHour(allUpcFlights[j].departure)) + ':' + str(getMinute(allUpcFlights[j].departure))
            arvlTime = str(getDay(allUpcFlights[j].arrival)) + '/' + str(getMonth(allUpcFlights[j].arrival)) + '/' + str(getYear(allUpcFlights[j].arrival)) + ' at ' + str(getHour(allUpcFlights[j].arrival)) + ':' + str(getMinute(allUpcFlights[j].arrival))
            #fæ departure tima og arrival tima a akjosanlegu formati


            #ef rank starfsmans er flight attendant og eg finn hann a viðeigandi stað i upcoming flights þa buum við til
            #klasatilvik fluginu og set í upc flights.
            if employees[i].rank=='Flight Attendant' and employees[i].SSN in (allUpcFlights[j].fa1 or allUpcFlights[j].fa2):
                flight=createFlightRoute(allUpcFlights[j].flightNumber, allUpcFlights[j].departingFrom, allUpcFlights[j].arrivingAt, deptTime, arvlTime,allUpcFlights[j].aircraftId, allUpcFlights[j].soldTickets, allUpcFlights[j].captain, allUpcFlights[j].copilot, allUpcFlights[j].fsm, allUpcFlights[j].fa1, allUpcFlights[j].fa2)
                upcFlights.append(flight)

            #Geri nakvæmlega sama fyrir allt mögulegt rank starfsmanna
            elif employees[i].rank=='Flight Service Manager' and employees[i].SSN in allUpcFlights[j].fsm:
                flight=createFlightRoute(allUpcFlights[j].flightNumber, allUpcFlights[j].departingFrom, allUpcFlights[j].arrivingAt, deptTime, arvlTime,allUpcFlights[j].aircraftId, allUpcFlights[j].soldTickets, allUpcFlights[j].captain, allUpcFlights[j].copilot, allUpcFlights[j].fsm, allUpcFlights[j].fa1, allUpcFlights[j].fa2)
                upcFlights.append(flight)

            elif employees[i].rank=='Captain' and employees[i].SSN in allUpcFlights[j].captain:
                flight=createFlightRoute(allUpcFlights[j].flightNumber, allUpcFlights[j].departingFrom, allUpcFlights[j].arrivingAt, deptTime, arvlTime,allUpcFlights[j].aircraftId, allUpcFlights[j].soldTickets, allUpcFlights[j].captain, allUpcFlights[j].copilot, allUpcFlights[j].fsm, allUpcFlights[j].fa1, allUpcFlights[j].fa2)
                upcFlights.append(flight)

            elif employees[i].rank=='Copilot' and employees[i].SSN in allUpcFlights[j].copilot:
                flight=createFlightRoute(allUpcFlights[j].flightNumber, allUpcFlights[j].departingFrom, allUpcFlights[j].arrivingAt, deptTime, arvlTime,allUpcFlights[j].aircraftId, allUpcFlights[j].soldTickets, allUpcFlights[j].captain, allUpcFlights[j].copilot, allUpcFlights[j].fsm, allUpcFlights[j].fa1, allUpcFlights[j].fa2)
                upcFlights.append(flight)

        numOfupcDest.append(len(upcFlights))

    allPastFlights=read_pastFlights(skra2)


    #Nakvæmlega sama gert fyrir past flights
    #Past flights
    for i in range(len(employees)):
        for j in range(len(allPastFlights)):

            deptTime = str(getDay(allPastFlights[j].departure)) + '/' + str(getMonth(allPastFlights[j].departure)) + '/' + str(getYear(allPastFlights[j].departure)) + ' at ' + str(getHour(allPastFlights[j].departure)) + ':' + str(getMinute(allPastFlights[j].departure))
            arvlTime = str(getDay(allPastFlights[j].arrival)) + '/' + str(getMonth(allPastFlights[j].arrival)) + '/' + str(getYear(allPastFlights[j].arrival)) + ' at ' + str(getHour(allPastFlights[j].arrival)) + ':' + str(getMinute(allPastFlights[j].arrival))

            if employees[i].rank=='Flight Attendant' and employees[i].SSN in (allPastFlights[j].fa1 or allPastFlights[j].fa2):
                flight=createFlightRoute(allPastFlights[j].flightNumber, allPastFlights[j].departingFrom, allPastFlights[j].arrivingAt, deptTime, arvlTime,allPastFlights[j].aircraftId, allPastFlights[j].soldTickets, allPastFlights[j].captain, allPastFlights[j].copilot, allPastFlights[j].fsm, allPastFlights[j].fa1, allPastFlights[j].fa2)
                pastFlights.append(flight)

            elif employees[i].rank=='Flight Service Manager' and employees[i].SSN in allPastFlights[j].fsm:
                flight=createFlightRoute(allPastFlights[j].flightNumber, allPastFlights[j].departingFrom, allPastFlights[j].arrivingAt, deptTime, arvlTime,allPastFlights[j].aircraftId, allPastFlights[j].soldTickets, allPastFlights[j].captain, allPastFlights[j].copilot, allPastFlights[j].fsm, allPastFlights[j].fa1, allPastFlights[j].fa2)
                pastFlights.append(flight)

            elif employees[i].rank=='Captain' and employees[i].SSN in allPastFlights[j].captain:
                flight=createFlightRoute(allPastFlights[j].flightNumber, allPastFlights[j].departingFrom, allPastFlights[j].arrivingAt, deptTime, arvlTime,allPastFlights[j].aircraftId, allPastFlights[j].soldTickets, allPastFlights[j].captain, allPastFlights[j].copilot, allPastFlights[j].fsm, allPastFlights[j].fa1, allPastFlights[j].fa2)
                pastFlights.append(flight)

            elif employees[i].rank=='Copilot' and employees[i].SSN in allPastFlights[j].copilot:
                flight=createFlightRoute(allPastFlights[j].flightNumber, allPastFlights[j].departingFrom, allPastFlights[j].arrivingAt, deptTime, arvlTime,allPastFlights[j].aircraftId, allPastFlights[j].soldTickets, allPastFlights[j].captain, allPastFlights[j].copilot, allPastFlights[j].fsm, allPastFlights[j].fa1, allPastFlights[j].fa2)
                pastFlights.append(flight)

        numOfpastDest.append(len(pastFlights))

    return numOfpastDest, numOfupcDest, pastFlights, upcFlights, employees
