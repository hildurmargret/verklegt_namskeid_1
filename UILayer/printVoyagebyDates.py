from LogicLayer.checkIfManned import*
def printVoyagebyDates(dep,ret):
    for i in range(len(dep)):
        print('VOYAGE DEPARTURE')
        print(dep[i].flightNumber + ', ' + dep[i].departingFrom + ' to ' + dep[i].arrivingAt + ', ' + ' Departure: ' + dep[i].departure + ', Arrival: ' + dep[i].arrival)
        print('VOYAGE RETURN')
        print(ret[i].flightNumber + ', ' + ret[i].departingFrom + ' to ' + ret[i].arrivingAt + ', ' + ' Departure: ' + ret[i].departure + ', Arrival: ' + ret[i].arrival)
        print('\n', end='')
        cap, cop, fsm = checkIfManned(dep[i])
        if cap and cop and fsm:
            print('Voyage is fully manned')
        else:
            print('Voyage is not fully manned')
            if not cap:
                print('Missing a captain')
            if not cop:
                print('Missing a copilot')
            if not fsm:
                print('Missing a flight service manager')
        print('\n', end='')
        print('----------------------------------------------------------------------------------------------------')
        seats=dep[i].soldTickets
        print("There are " + str(seats)+ " seats sold")
        print('----------------------------------------------------------------------------------------------------')
    return
