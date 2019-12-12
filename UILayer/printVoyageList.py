from LogicLayer.checkIfManned import*
from LogicLayer.Date import *
def printVoyageList(voyage,daterange):

    ar1=str(getYear(daterange[0]))
    man1=str(getMonth(daterange[0]))
    dag1=str(getDay(daterange[0]))

    ar2=str(getYear(daterange[1]))
    man2=str(getMonth(daterange[1]))
    dag2=str(getDay(daterange[1]))

    print('FLIGHTS DURING TIME PERIOD: ' + dag2 + '/' + man2 + '/' + ar2 + ' TO ' + dag1 + '/' + man1 + '/' + ar1)
    print('')

    for i in voyage:
        retDeptTime = str(getDay(i.returnFlight.departure)) + '/' + str(getMonth(i.returnFlight.departure)) + '/' + str(getYear(i.returnFlight.departure)) + ' at ' + str(getHour(i.returnFlight.departure)) + ':' + str(getMinute(i.returnFlight.departure))
        retArvlTime = str(getDay(i.returnFlight.arrival)) + '/' + str(getMonth(i.returnFlight.arrival)) + '/' + str(getYear(i.returnFlight.arrival)) + ' at ' + str(getHour(i.returnFlight.arrival)) + ':' + str(getMinute(i.returnFlight.arrival))
        depDeptTime = str(getDay(i.departureFlight.departure)) + '/' + str(getMonth(i.departureFlight.departure)) + '/' + str(getYear(i.departureFlight.departure)) + ' at ' + str(getHour(i.departureFlight.departure)) + ':' + str(getMinute(i.departureFlight.departure))
        depArvlTime = str(getDay(i.departureFlight.arrival)) + '/' + str(getMonth(i.departureFlight.arrival)) + '/' + str(getYear(i.departureFlight.arrival)) + ' at ' + str(getHour(i.departureFlight.arrival)) + ':' + str(getMinute(i.departureFlight.arrival))

        print('VOYAGE DEPARTURE:')
        print(i.departureFlight.flightNumber + ', ' + i.departureFlight.departingFrom + ' to ' + i.departureFlight.arrivingAt + ', ' + ' Departure: ' + depDeptTime + ', Arrival: ' + depArvlTime)
        print('VOYAGE RETURN:')
        print(i.returnFlight.flightNumber + ', ' + i.returnFlight.departingFrom + ' to ' + i.returnFlight.arrivingAt + ', ' + ' Departure: ' + retDeptTime + ', Arrival: ' + retArvlTime)

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
        if i.departureFlight.soldTickets == '':
            seats=0
        else:
            seats=i.departureFlight.soldTickets
        print("There are " + str(seats)+ " seats sold")
        print('----------------------------------------------------------------------------------------------------')

        print('\n',end='')
    return
