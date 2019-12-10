from LogicLayer.Date import*

def printCompleteWS(pastFlights, upcFlights, employees):

    for k in range(len(employees)):
        if employees[k].role == 'Cabincrew':
            print(employees[k].name + ', ' + employees[k].SSN + ', ' + employees[k].address + ', ' + employees[k].phoneNumber + ', ' + employees[k].role + ', ' + employees[k].rank + '\n')
        else:
            print(employees[k].name + ', ' + employees[k].SSN + ', ' + employees[k].address + ', ' + employees[k].phoneNumber + ', ' + employees[k].role + ', ' + employees[k].rank + ', ' + employees[k].licence + '\n')
        print
        print('PAST FLIGHTS')
        if len(pastFlights)==0:
            print('No past flights')
        else:
            for j in range(len(pastFlights)):
                print('Flight number: ' + pastFlights[j].flightNumber + ', From ' + pastFlights[j].departingFrom + ' to ' + pastFlights[j].arrivingAt + ', ', end = '')
                print('Departure: ' + pastFlights[j].departure + ', Arrival: ' + pastFlights[j].arrival)
        print('\n',end='')

        print('UPCOMING FLIGHTS')
        if len(upcFlights) == 0:
            print('No upcoming flights')
        else:
            for j in range(len(upcFlights)):
                print('Flight number: ' + upcFlights[j].flightNumber + ', From ' + upcFlights[j].departingFrom + ' to ' + upcFlights[j].arrivingAt + ', ', end = '')
                print('Departure: ' + upcFlights[j].departure + ', Arrival: ' + upcFlights[j].arrival)
        print('\n',end='')
        print('----------------------------------------------------------------------------------------------------')
        print('\n',end='')

    return


def printWeeklyWS(flights, employees, week, year):

    for k in range(len(employees)):
        if employees[k].role == 'Cabincrew':
            print(employees[k].name + ', ' + employees[k].SSN + ', ' + employees[k].address + ', ' + employees[k].phoneNumber + ', ' + employees[k].role + ', ' + employees[k].rank + '\n')
        else:
            print(employees[k].name + ', ' + employees[k].SSN + ', ' + employees[k].address + ', ' + employees[k].phoneNumber + ', ' + employees[k].role + ', ' + employees[k].rank + ', ' + employees[k].licence + '\n')
        print
        print('Week: ' + week + ', Year: ' + year)
        if len(flights)==0:
            print('No flights for this time period')
        else:
            for j in range(len(flights)):
                print('Flight number: ' + flights[j].flightNumber + ', From ' + flights[j].departingFrom + ' to ' + flights[j].arrivingAt + ', ', end = '')
                print('Departure: ' + flights[j].departure + ', Arrival: ' + flights[j].arrival)
        print('\n', end='')
        print('----------------------------------------------------------------------------------------------------')
        print('\n',end='')
