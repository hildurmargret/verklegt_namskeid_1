from DataLayer.getDestinations import*
import operator


def fixFlNo(flights, destinations):

    for dest in destinations:
        if dest.id == 'KEF':
            del dest

    retFlights = []

    for i in range(len(destinations)):
        flightsToDest_i = []
        flightsFromDest_i = []

        for flight in flights:
            new_flNo = 'NA'

            if flight.departingFrom == destinations[i].id or flight.arrivingAt == destinations[i].id:

                if (i+1) < 10:
                    new_flNo = new_flNo + '0' + str(i+1)
                else:
                    new_flNo = new_flNo + str(i+1)

                if flight.departingFrom == destinations[i]:
                    flightsFromDest_i.append(flight)
                elif flight.arrivingAt == destinations[i]:
                    flightsToDest_i.append(flight)

            flightsFromDest_i.sort(key=operator.attrgetter('departure'))
            flightsToDest_i.sort(key=operator.attrgetter('departure'))

            for j in range(len(flightsToDest_i)):
                new_flNo = new_flNo + str(i*2)

            for k in range(len(flightsFromDest_i)):
                new_flNo = new_flNo + str(i*2 + 1)

            flight.flightNumber = new_flNo
            retFlights.append(flight)

    return retFlights
