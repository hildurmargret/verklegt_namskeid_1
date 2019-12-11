from DataLayer.getDestinations import*
from ModelClasses.flightRoute import*
import operator


def fixFlNo(flights, destinations):

    for dest in destinations:
        if dest.id == 'KEF':
            destinations.remove(dest)

    for dest in destinations:
        print(dest.id)

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

    for dest in destinations:
        flightsToDest_i = []
        flightsFromDest_i = []

        for flight in flights:
            if flight.departingFrom == dest.id:
                flightsFromDest_i.append(flight)
            elif flight.arrivingAt == dest.id:
                flightsToDest_i.append(flight)

        flightsFromDest_i.sort(key=lambda flight: flight.departure)
        flightsToDest_i.sort(key=lambda flight: flight.departure)


        counter = -1
        day = str(flightsFromDest_i[0].departure[0:10]) + '00:00:00'

        for k in range(len(flightsFromDest_i)):

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

    return retFlights
