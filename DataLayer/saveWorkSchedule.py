from LogicLayer.Date import*
import sys
import os
def saveCompleteWS(pastFlights, upcFlights, employees):

    absPathFile = os.path.abspath(__file__)
    fileDir = os.path.dirname(os.path.abspath(__file__))
    parentDir = os.path.dirname(fileDir)
    path = parentDir + "/csvFiles/"

    file = open(path+'WorkSchedule.txt','w')

    for k in range(len(employees)):
        if employees[k].role == 'Cabincrew':
            file.write(employees[k].name + ', ' + employees[k].SSN + ', ' + employees[k].address + ', ' + employees[k].phoneNumber + ', ' + employees[k].role + ', ' + employees[k].rank + '\n')
        else:
            file.write(employees[k].name + ', ' + employees[k].SSN + ', ' + employees[k].address + ', ' + employees[k].phoneNumber + ', ' + employees[k].role + ', ' + employees[k].rank + ', ' + employees[k].licence + '\n')

        file.write('\n')
        file.write('PAST FLIGHTS \n')
        if len(pastFlights)==0:
            file.write('No past flights')
        else:
            for j in range(len(pastFlights)):
                file.write('Flight number: ' + pastFlights[j].flightNumber + ', From ' + pastFlights[j].departingFrom + ' to ' + pastFlights[j].arrivingAt + ', ')
                file.write('Departure: ' + pastFlights[j].departure + ', Arrival: ' + pastFlights[j].arrival + '\n')
        file.write('\n')

        file.write('UPCOMING FLIGHTS \n')
        if len(upcFlights)==0:
            file.write('No upcoming flights')
        else:
            for j in range(len(upcFlights)):
                file.write('Flight number: ' + upcFlights[j].flightNumber + ', From ' + upcFlights[j].departingFrom + ' to ' + upcFlights[j].arrivingAt + ', ')
                file.write('Departure: ' + upcFlights[j].departure + ', Arrival: ' + upcFlights[j].arrival + '\n')

        file.write('\n')
        file.write('-----------------------------------------------------------------------------------------------------')
        file.write('\n')

    file.close()
    return


def saveWeeklyWS(flights, employees, week, year):

    absPathFile = os.path.abspath(__file__)
    fileDir = os.path.dirname(os.path.abspath(__file__))
    parentDir = os.path.dirname(fileDir)
    path = parentDir + "/csvFiles/"

    file = open(path + 'WorkSchedule.txt','w')

    for k in range(len(employees)):
        if employees[k].role == 'Cabincrew':
            file.write(employees[k].name + ', ' + employees[k].SSN + ', ' + employees[k].address + ', ' + employees[k].phoneNumber + ', ' + employees[k].role + ', ' + employees[k].rank + '\n')
        else:
            file.write(employees[k].name + ', ' + employees[k].SSN + ', ' + employees[k].address + ', ' + employees[k].phoneNumber + ', ' + employees[k].role + ', ' + employees[k].rank + ', ' + employees[k].licence + '\n')

        file.write('\n')
        file.write('Week: ' + week + ', Year: ' + year + '\n')
        if len(flights)==0:
            file.write('No flights for this time period')
        else:
            for j in range(len(flights)):
                file.write('Flight number: ' + flights[j].flightNumber + ', From ' + flights[j].departingFrom + ' to ' + flights[j].arrivingAt + ', ')
                file.write('Departure: ' + flights[j].departure + ', Arrival: ' + flights[j].arrival + '\n')
        file.write('\n')
        file.write('-----------------------------------------------------------------------------------------------------')
        file.write('\n')
