from LogicLayer.checkIfManned import*
from LogicLayer.Date import *
from DataLayer.getAirplaneCapacity import *

def printSearchedVoyage(voyage):

    for i in voyage:
        print('\n')
        retDeptTime = str(getDay(i.returnFlight.departure)) + '/' + str(getMonth(i.returnFlight.departure)) + '/' + str(getYear(i.returnFlight.departure)) + ' at ' + str(getHour(i.returnFlight.departure)) + ':' + str(getMinute(i.returnFlight.departure))
        retArvlTime = str(getDay(i.returnFlight.arrival)) + '/' + str(getMonth(i.returnFlight.arrival)) + '/' + str(getYear(i.returnFlight.arrival)) + ' at ' + str(getHour(i.returnFlight.arrival)) + ':' + str(getMinute(i.returnFlight.arrival))
        depDeptTime = str(getDay(i.departureFlight.departure)) + '/' + str(getMonth(i.departureFlight.departure)) + '/' + str(getYear(i.departureFlight.departure)) + ' at ' + str(getHour(i.departureFlight.departure)) + ':' + str(getMinute(i.departureFlight.departure))
        depArvlTime = str(getDay(i.departureFlight.arrival)) + '/' + str(getMonth(i.departureFlight.arrival)) + '/' + str(getYear(i.departureFlight.arrival)) + ' at ' + str(getHour(i.departureFlight.arrival)) + ':' + str(getMinute(i.departureFlight.arrival))

        print('VOYAGE DEPARTURE:')
        print(i.departureFlight.flightNumber + ', ' + i.departureFlight.departingFrom + ' to ' + i.departureFlight.arrivingAt + ', ' + ' Departure: ' + depDeptTime + ', Arrival: ' + depArvlTime)
        print('VOYAGE RETURN:')
        print(i.returnFlight.flightNumber + ', ' + i.returnFlight.departingFrom + ' to ' + i.returnFlight.arrivingAt + ', ' + ' Departure: ' + retDeptTime + ', Arrival: ' + retArvlTime)
        print('')
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
        print('----------------------------------------------------------------------------------------------------')

        seats_out=i.departureFlight.soldTickets
        seats_home=i.returnFlight.soldTickets
        #print(type(capa))
        #print(type(seats))
        if seats_out=='':
            seats_out=0
        if seats_home=='':
            seats_home=0
        if not i.departureFlight.aircraftId:
            print('No airplane assigned to this voyage')

        else:
            capa=airplaneCapacity(i.departureFlight.aircraftId)
            avail_out=capa-int(seats_out)
            avail_home=capa-int(seats_home)
            print("There are " + str(seats_out)+ " seats sold outbound")
            print('There are ' + str(avail_out) + ' seats available outbound')
            print('')
            print("There are " + str(seats_home)+ " seats sold homebound")
            print('There are ' + str(avail_home) + ' seats available homebound')

        print('----------------------------------------------------------------------------------------------------')

        print('\n',end='')
    return
