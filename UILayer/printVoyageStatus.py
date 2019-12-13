from LogicLayer.Date import*

def printVoyageStatus(dep, ret, status, input_date, input_time):

    #fall til að prenta út stodu vinnuferðar

    print('\n', end='')
    print('THERE ARE ' + str(len(status)) + ' ONGOING VOYAGES ' + input_date + ' AT: ' + input_time)
    print('\n', end='')

    for i in range(len(status)):
        print('VOYAGE ' + str(i+1) +': ' + status[i])
        print('VOYAGE DEPARTURE')
        print(dep[i].flightNumber + ', ' + dep[i].departingFrom + ' to ' + dep[i].arrivingAt + ', ' + ' Departure: ' + dep[i].departure + ', Arrival: ' + dep[i].arrival)
        print('VOYAGE RETURN')
        print(ret[i].flightNumber + ', ' + ret[i].departingFrom + ' to ' + ret[i].arrivingAt + ', ' + ' Departure: ' + ret[i].departure + ', Arrival: ' + ret[i].arrival)
        print('\n', end='')
