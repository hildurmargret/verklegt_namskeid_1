from LogicLayer.Date import*
import csv
from ModelClasses.Staff import*
from DataLayer.OpenFile import *
from DataLayer.read_crew_file import *
from DataLayer.read_pastFlights import *

def emplWorking(inptDate):

    inptDay = str(inptDate[0:2])
    inptMonth = str(inptDate[3:5])
    inptYear = str(inptDate[6:10])

    standardDate = inptYear + '-'+ inptMonth + '-' + inptDay + 'T' + '00:00:00'

    file2='Crew.csv'
    allStaff=read_crew_file(file2)

    today=now()

    if today>standardDate:
        file1='PastFlights copy.csv'
    else:
        file1='UpcomingFlights copy3.csv'

    allPastFlights=read_pastFlights(file1)

    updemplSSN=[]
    working=[]
    emplSSN = []
    employees = []
    noemployees=[]
    emplDest=[]
    emplLOKA=[]

    for j in range(len(allPastFlights)):
        day = str(getDay(allPastFlights[j].departure))
        month = str(getMonth(allPastFlights[j].departure))
        year = str(getYear(allPastFlights[j].departure))

        if inptDay == day and inptMonth == month and inptYear == year:
            emplSSN.append(allPastFlights[j].captain)
            emplSSN.append(allPastFlights[j].copilot)
            emplSSN.append(allPastFlights[j].fsm)
            emplSSN.append(allPastFlights[j].fa1)
            emplSSN.append(allPastFlights[j].fa2)

    for i in emplSSN:
        if i not in updemplSSN:
            updemplSSN.append(i)

    for j in range(len(allStaff)):
        for i in range(len(updemplSSN)):
            if allStaff[j].SSN == updemplSSN[i]:
                empl = createStaff(allStaff[j].name, allStaff[j].SSN, allStaff[j].address, allStaff[j].phoneNumber,allStaff[j].emailAddress,allStaff[j].rank,allStaff[j].role,allStaff[j].licence)
                employees.append(empl)

        if allStaff[j].SSN not in updemplSSN:
            emp = createStaff(allStaff[j].name, allStaff[j].SSN, allStaff[j].address, allStaff[j].phoneNumber,allStaff[j].emailAddress,allStaff[j].rank,allStaff[j].role,allStaff[j].licence)
            noemployees.append(emp)

    for k in range(len(allPastFlights)):
        day = str(getDay(allPastFlights[k].departure))
        month = str(getMonth(allPastFlights[k].departure))
        year = str(getYear(allPastFlights[k].departure))

        if inptDay == day and inptMonth == month and inptYear == year:
            for i in range(len(employees)):
                if employees[i].rank == 'Captain' and allPastFlights[k].captain == employees[i].SSN and allPastFlights[k].arrivingAt != 'KEF':
                    emplDest.append(allPastFlights[k].arrivingAt + employees[i].SSN)
                elif employees[i].rank == 'Copilot' and allPastFlights[k].copilot == employees[i].SSN and allPastFlights[k].arrivingAt != 'KEF':
                    emplDest.append(allPastFlights[k].arrivingAt + employees[i].SSN)
                elif employees[i].rank == 'Flight Service Manager' and allPastFlights[k].fsm == employees[i].SSN and allPastFlights[k].arrivingAt != 'KEF':
                    emplDest.append(allPastFlights[k].arrivingAt + employees[i].SSN)
                elif employees[i].rank == 'Flight Attendant' and (allPastFlights[k].fa1 == employees[i].SSN or allPastFlights[k].fa2 == employees[i].SSN) and allPastFlights[k].arrivingAt != 'KEF':
                    emplDest.append(allPastFlights[k].arrivingAt + employees[i].SSN)

    for j in range(len(allStaff)):
        for i in range(len(emplDest)):
            if allStaff[j].SSN == str(emplDest[i][3:len(emplDest[i])]):
                emplLOKA.append(allStaff[j].name + ', ' + allStaff[j].role + ' - ' + str(emplDest[i][0:3]))

    return employees, noemployees, emplLOKA
