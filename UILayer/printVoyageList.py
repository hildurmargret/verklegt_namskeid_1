from LogicLayer.checkIfManned import*
def printVoyageList(voyage):

    for i in voyage:
        print('VOYAGE DEPARTURE:')
        print(i.departureFlight.flightNumber + ', ' + i.departureFlight.departingFrom + ' to ' + i.departureFlight.arrivingAt + ', ' + ' Departure: ' + i.departureFlight.departure + ', Arrival: ' + i.departureFlight.arrival)
        print('VOYAGE RETURN:')
        print(i.returnFlight.flightNumber + ', ' + i.returnFlight.departingFrom + ' to ' + i.returnFlight.arrivingAt + ', ' + ' Departure: ' + i.returnFlight.departure + ', Arrival: ' + i.returnFlight.arrival)

        cap, cop, fsm = checkIfManned(i.departureFlight)
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
        print('\n',end='')
        print('----------------------------------------------------------------------------------------------------')
        print('\n',end='')
    return
