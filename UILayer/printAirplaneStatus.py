from LogicLayer.Date import *

def printAirplaneStatus(inAir, onGround, input_date, input_time):

    #fall til að prenta status flugvela

    print('')
    print('AIRPLANES IN AIR ' + input_date + ' AT ' + input_time)
    print('----------------------------------------------------------------------------------------------------')
    for i in range(len(inAir)):
        if inAir[i].arrivingAt == 'KEF':
            d=str(getDay(inAir[i].arrival))
            m=str(getMonth(inAir[i].arrival))
            y=str(getYear(inAir[i].arrival))
            time=str(inAir[i].arrival[11:len(inAir[i].arrival)])
            if inAir[i].aircraftId == '':
                print('Airplane: No assigned airplane, Destination: ' + inAir[i].arrivingAt + ', Flight number: ' + inAir[i].flightNumber + '\n' + 'Next availability: ' + d + '/' + m + '/' + y + ' at ' + time)
            else:
                print('Airplane: ' + inAir[i].aircraftId + ', Destination: ' + inAir[i].arrivingAt + ', Flight number: ' + inAir[i].flightNumber + '\n' + 'Next availability: ' + d + '/' + m + '/' + y + ' at ' + time)
            print('')
        else:
            time = add_hour(inAir[i].departure,5)
            d=str(getDay(time))
            m=str(getMonth(time))
            y=str(getYear(time))
            timi=str(time[11:len(time)])

            if inAir[i].aircraftId == '':
                print('Airplane: No assigned airplane, Destination: ' + inAir[i].arrivingAt + ', Flight number: ' + inAir[i].flightNumber + '\n' + 'Next availability: ' + d + '/' + m + '/' + y + ' at ' + timi)
            else:
                print('Airplane: ' + inAir[i].aircraftId + ', Destination: ' + inAir[i].arrivingAt + ', Flight number: ' + inAir[i].flightNumber + '\n' + 'Next availability: ' + d + '/' + m + '/' + y + ' at ' + timi)
            print('')
