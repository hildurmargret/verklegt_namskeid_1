from LogicLayer.checkIfManned import*
from DataLayer.getAirplaneCapacity import *

def printVoyagebyDates(dep,ret):
    #print(len(dep))
    #print(len(ret))
    for i in range(len(dep)):
        print('\n')
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
        print('----------------------------------------------------------------------------------------------------')

        seats_out=dep[i].soldTickets
        seats_home=ret[i].soldTickets
        #print(type(capa))
        #print(type(seats))
        if seats_out=='':
            seats_out=0
        if seats_home=='':
            seats_home=0
        if not dep[i].aircraftId:
            print('No airplane assigned to this voyage')

        else:
            capa=airplaneCapacity(dep[i].aircraftId)
            avail_out=capa-int(seats_out)
            avail_home=capa-int(seats_home)
            print("There are " + str(seats_out)+ " seats sold outbound")
            print('There are ' + str(avail_out) + ' seats available outbound')
            print('')
            print("There are " + str(seats_home)+ " seats sold homebound")
            print('There are ' + str(avail_home) + ' seats available homebound')

        print('----------------------------------------------------------------------------------------------------')
    return
