from LogicLayer.checkIfManned import*
def printVoyageList(voyage):

    # if linur[0].flightNumber[4]>linur[1].flightNumber[4]:
    #     print('VOYAGE DEPARTURE:')
    #     print(linur[1].flightNumber + ', ' + linur[1].departingFrom + ' to ' + linur[1].arrivingAt + ', ' + ' Departure: ' + linur[1].departure + ', Arrival: ' + linur[1].arrival)
    #     print('VOYAGE RETURN:')
    #     print(linur[0].flightNumber + ', ' + linur[0].departingFrom + ' to ' + linur[0].arrivingAt + ', ' + ' Departure: ' + linur[0].departure + ', Arrival: ' + linur[0].arrival)
    #
    # else:
    #     print('VOYAGE DEPARTURE:')
    #     print(linur[0].flightNumber + ', ' + linur[0].departingFrom + ' to ' + linur[0].arrivingAt + ', ' + ' Departure: ' + linur[0].departure + ', Arrival: ' + linur[0].arrival)
    #     print('VOYAGE RETURN:')
    #     print(linur[1].flightNumber + ', ' + linur[1].departingFrom + ' to ' + linur[1].arrivingAt + ', ' + ' Departure: ' + linur[1].departure + ', Arrival: ' + linur[1].arrival)

    print('VOYAGE DEPARTURE:')
    print(voyage.departureFlight.flightNumber + ', ' + voyage.departureFlight.departingFrom + ' to ' + voyage.departureFlight.arrivingAt + ', ' + ' Departure: ' + voyage.departureFlight.departure + ', Arrival: ' + voyage.departureFlight.arrival)
    print('VOYAGE RETURN:')
    print(voyage.returnFlight.flightNumber + ', ' + voyage.returnFlight.departingFrom + ' to ' + voyage.returnFlight.arrivingAt + ', ' + ' Departure: ' + voyage.returnFlight.departure + ', Arrival: ' + voyage.returnFlight.arrival)

    cap, cop, fsm = checkIfManned(voyage.departureFlight)
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
    print('\n')

    return
