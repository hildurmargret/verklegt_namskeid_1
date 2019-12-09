from LogicLayer.Date import*
def saveWS(pastFlights, employees):
    path = '/Users/hildur/Desktop/'
    file = open(path+'WorkSchedule.txt','w')

    for k in range(len(employees)):
        if employees[k].role == 'Cabincrew':
            file.write(employees[k].name + ', ' + employees[k].SSN + ', ' + employees[k].address + ', ' + employees[k].phoneNumber + ', ' + employees[k].role + ', ' + employees[k].rank + '\n')
        else:
            file.write(employees[k].name + ', ' + employees[k].SSN + ', ' + employees[k].address + ', ' + employees[k].phoneNumber + ', ' + employees[k].role + ', ' + employees[k].rank + ', ' + employees[k].licence + '\n')

        file.write('\n')
        file.write('PAST FLIGHTS \n')
        for j in range(len(pastFlights)):
            file.write('Flight number: ' + pastFlights[j].flightNumber + ', From ' + pastFlights[j].departingFrom + ' to ' + pastFlights[j].arrivingAt + ', ')
            file.write('Departure: ' + pastFlights[j].departure + ', Arrival: ' + pastFlights[j].arrival + '\n')
        file.write('\n')

        file.write('UPCOMING FLIGHTS \n')
        for j in range(len(pastFlights)):
            file.write('Flight number: ' + pastFlights[j].flightNumber + ', From ' + pastFlights[j].departingFrom + ' to ' + pastFlights[j].arrivingAt + ', ')
            file.write('Departure: ' + pastFlights[j].departure + ', Arrival: ' + pastFlights[j].arrival + '\n')
        file.write('\n')
        #     print('Flight number: ' + upcFlights[j].flightNumber + ', From ' + upcFlights[j].departingFrom + ' to ' + upcFlights[j].arrivingAt + ', ', end = '')
        #     print('Departure: ' + upcFlights[j].departure + ', Arrival: ' + upcFlights[j].arrival)
        # print('\n')
        file.write('\n')
        file.write('-----------------------------------------------------------------------------------------------------')
        file.write('\n')

    file.close()
