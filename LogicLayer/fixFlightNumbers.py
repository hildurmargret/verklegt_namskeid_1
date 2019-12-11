from DataLayer.getDestinations import*
from ModelClasses.flightRoute import*
import operator


def fixFlNo(flights, destinations):

    for j in range(len(destinations)):
        if destinations[j].id == 'KEF':
            del destinations[j]


    #print('helo' + str(len(flights)))
    #print('belo' + str(len(destinations)))

    retFlights = []
    for flight in flights:
        new_flNo = 'NA'

        for i in range(len(destinations)):
            if flight.departingFrom == destinations[i].id or flight.arrivingAt == destinations[i].id:
                if (i+1) < 10:
                    new_flNo = new_flNo + '0' + str(i+1)
                else:
                    new_flNo = new_flNo + str(i+1)

        flight.flightNumber = new_flNo

    for j in range(len(destinations)):
        flightsToDest_i = []
        flightsFromDest_i = []

        for flight in flights:
            if flight.departingFrom == destinations[j].id:
                flightsFromDest_i.append(flight)
            elif flight.arrivingAt == destinations[j].id:
                flightsToDest_i.append(flight)

        print(len(flightsFromDest_i))
        print(len(flightsToDest_i))

        flightsFromDest_i.sort(key=lambda flight: flight.departure)
        flightsToDest_i.sort(key=lambda flight: flight.departure)

        print('helo' + str(len(flightsFromDest_i)))

        counter = -1
        day = str(flightsFromDest_i[0].departure[0:10]) + '00:00:00'

        for k in range(len(flightsFromDest_i)):
            print(k)
            print(flightsFromDest_i[k].flightNumber)
            date = str(flightsFromDest_i[k].departure[0:10]) + '00:00:00'
            if day != date:
                counter = 0
            else:
                counter = counter + 1

            flightsFromDest_i[k].flightNumber = flightsFromDest_i[k].flightNumber + str(counter*2 + 1)
            flightsToDest_i[k].flightNumber = flightsToDest_i[k].flightNumber + str(counter*2)
            retFlights.append(flightsToDest_i[k])
            retFlights.append(flightsFromDest_i[k])
            day = str(flightsFromDest_i[k].departure[0:10]) + '00:00:00'

        #retFlights.sort(key=lambda flight: flight.departure)


    return retFlights
