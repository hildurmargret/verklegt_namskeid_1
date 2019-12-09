
def printVoyagebyDates(dep,ret):
    for i in range(len(dep)):
        print('VOYAGE DEPARTURE')
        print(dep[i].flightNumber + ', ' + dep[i].departingFrom + ' to ' + dep[i].arrivingAt + ', ' + ' Departure: ' + dep[i].departure + ', Arrival: ' + dep[i].arrival)
        print('VOYAGE RETURN')
        print(ret[i].flightNumber + ', ' + ret[i].departingFrom + ' to ' + ret[i].arrivingAt + ', ' + ' Departure: ' + ret[i].departure + ', Arrival: ' + ret[i].arrival)
        print('\n')
    return
