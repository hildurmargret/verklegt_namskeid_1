from LogicLayer.Date import*

def printWS(pastFlights, employees):

    for k in range(len(employees)):
        if employees[k].role == 'Cabincrew':
            print(employees[k].name + ', ' + employees[k].SSN + ', ' + employees[k].address + ', ' + employees[k].phoneNumber + ', ' + employees[k].role + ', ' + employees[k].rank + '\n')
        else:
            print(employees[k].name + ', ' + employees[k].SSN + ', ' + employees[k].address + ', ' + employees[k].phoneNumber + ', ' + employees[k].role + ', ' + employees[k].rank + ', ' + employees[k].licence + '\n')
        print
        print('PAST FLIGHTS')
        for j in range(len(pastFlights)):
            print('Flight number: ' + pastFlights[j].flightNumber + ', From ' + pastFlights[j].departingFrom + ' to ' + pastFlights[j].arrivingAt + ', ', end = '')
            print('Departure: ' + pastFlights[j].departure + ', Arrival: ' + pastFlights[j].arrival)
        print('\n')

        print('UPCOMING FLIGHTS')
        for j in range(len(pastFlights)):
            print('Flight number: ' + pastFlights[j].flightNumber + ', From ' + pastFlights[j].departingFrom + ' to ' + pastFlights[j].arrivingAt + ', ', end = '')
            print('Departure: ' + pastFlights[j].departure + ', Arrival: ' + pastFlights[j].arrival)
        print('\n')
        #     print('Flight number: ' + upcFlights[j].flightNumber + ', From ' + upcFlights[j].departingFrom + ' to ' + upcFlights[j].arrivingAt + ', ', end = '')
        #     print('Departure: ' upcFlights[j].departure + ', Arrival: ' + upcFlights[j].arrival)
        # print('\n')
        print
        print('-----------------------------------------------------------------------------------------------------')
        print

    return
