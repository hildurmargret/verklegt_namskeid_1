from LogicLayer.Date import *

def printAirplaneStatus(inAir, onGround, input_date, input_time):

    print('')
    print('AIRPLANES IN AIR ' + input_date + ' AT ' + input_time)
    print('')
    for i in range(len(inAir)):
        if inAir[i].arrivingAt == 'KEF':
            d=str(getDay(inAir[i].arrival))
            m=str(getMonth(inAir[i].arrival))
            y=str(getYear(inAir[i].arrival))
            time=str(inAir[i].arrival[11:len(inAir[i].arrival)])
            print('Airplane: ' + inAir[i].aircraftId + ', Destination: ' + inAir[i].arrivingAt + ', Flight number: ' + inAir[i].flightNumber + '\n' + 'Next availability: ' + d + '/' + m + '/' + y + ' at ' + time)
            print('')
        else:
            d=str(getDay(inAir[i].arrival))
            m=str(getMonth(inAir[i].arrival))
            y=str(getYear(inAir[i].arrival))
            time=str(inAir[i].arrival[11:len(inAir[i].arrival)])
            print('Airplane: ' + inAir[i].aircraftId + ', Destination: ' + inAir[i].arrivingAt + ', Flight number: ' + inAir[i].flightNumber + '\n' + 'Next availability: ' + d + '/' + m + '/' + y + ' at ' + time)
            print('')
