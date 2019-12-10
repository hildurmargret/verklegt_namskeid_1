import csv
from LogicLayer.Date import*
from DataLayer.OpenFile import*
from ModelClasses.Voyage import*
from ModelClasses.flightRoute import*

def leitaVoyage(inpt):

    #path = '/Users/hildur/Documents/github/verklegt_namskeid_1/Documents/github/Verklegt1/UPDATEDSTUDENTDATA/'
    #file1 = path + 'UpcomingFlights copy.csv'
    #file2 = path + 'PastFlights.csv'

    dest = inpt[2:4]
    no = int(inpt[4:len(inpt)])
    voyage = createVoyage()
    found_bool = 0

    if not found_bool:
        file1=OpenFile('UpcomingFlights copy.csv')
    else:
        file1=OpenFile('PastFlights.csv')

    with file1 as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:

            deptTime = str(getDay(row['departure'])) + '/' + str(getMonth(row['departure'])) + '/' + str(getYear(row['departure'])) + ' at ' + str(getHour(row['departure'])) + ':' + str(getMinute(row['departure']))
            arvlTime = str(getDay(row['arrival'])) + '/' + str(getMonth(row['arrival'])) + '/' + str(getYear(row['arrival'])) + ' at ' + str(getHour(row['arrival'])) + ':' + str(getMinute(row['arrival']))

            if no%2 == 0 and row['flightNumber'] == inpt:
                flight = createFlightRoute(row['flightNumber'],row['departingFrom'],row['arrivingAt'],deptTime,arvlTime,0,0)
                voyage.departureFlight = flight
                #voyage.append(voy)

            elif no%2 == 0 and (row['flightNumber'] == ('NA' + dest + str(no+1))):
                flight = createFlightRoute(row['flightNumber'],row['departingFrom'],row['arrivingAt'],deptTime,arvlTime,0,0)
                voyage.returnFlight = flight
                #voyage.append(voy)

            elif no%2 != 0 and row['flightNumber'] == inpt:
                flight = createFlightRoute(row['flightNumber'],row['departingFrom'],row['arrivingAt'],deptTime,arvlTime,0,0)
                voyage.returnFlight = flight
                #voyage.append(voy)

            elif no%2 != 0 and row['flightNumber'] == ('NA' + dest + str(no-1)):
                flight = createFlightRoute(row['flightNumber'],row['departingFrom'],row['arrivingAt'],deptTime,arvlTime,0,0)
                voyage.departureFlight = flight
                #voyage.append(voy)

    return voyage
