import csv
from LogicLayer.Date import*
from DataLayer.OpenFile import*

def leitaVoyage(inpt):

    #path = '/Users/hildur/Documents/github/verklegt_namskeid_1/Documents/github/Verklegt1/UPDATEDSTUDENTDATA/'
    #file1 = path + 'UpcomingFlights copy.csv'
    #file2 = path + 'PastFlights.csv'

    dest = inpt[2:4]
    no = int(inpt[4:len(inpt)])
    voyage = []
    found_bool = 0

    if not found_bool:
        file1=OpenFile('UpcomingFlights copy.csv')
    else:
        file1=OpenFile('PastFlights.csv')

    with file1 as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            voyDep = ['VOYAGE RETURN:']
            voyRet = ['VOYAGE DEPARTURE:']

            deptTime = str(getDay(row['departure'])) + '/' + str(getMonth(row['departure'])) + '/' + str(getYear(row['departure'])) + ' at ' + str(getHour(row['departure'])) + ':' + str(getMinute(row['departure']))
            arvlTime = str(getDay(row['arrival'])) + '/' + str(getMonth(row['arrival'])) + '/' + str(getYear(row['arrival'])) + ' at ' + str(getHour(row['arrival'])) + ':' + str(getMinute(row['arrival']))

            if no%2 == 0 and row['flightNumber'] == inpt:
                voyDep.append(row['flightNumber'] + ', ' + row['departingFrom'] + ', ' + row['arrivingAt'] + ', Departure: ' + deptTime + ', Arrival: ' + arvlTime)


            elif no%2 == 0 and (row['flightNumber'] == ('NA' + dest + str(no+1))):
                voyRet.append(row['flightNumber'] + ', ' + row['departingFrom'] + ', ' + row['arrivingAt'] + ', Departure: ' + deptTime + ', Arrival: ' + arvlTime)

            elif no%2 != 0 and row['flightNumber'] == inpt:
                voyRet.append(row['flightNumber'] + ', ' + row['departingFrom'] + ', ' + row['arrivingAt'] + ', Departure: ' + deptTime + ', Arrival: ' + arvlTime)

            elif no%2 != 0 and row['flightNumber'] == ('NA' + dest + str(no-1)):
                voyDep.append(row['flightNumber'] + ', ' + row['departingFrom'] + ', ' + row['arrivingAt'] + ', Departure: ' + deptTime + ', Arrival: ' + arvlTime)

            if len(voyDep) != 1:
                voyage.append(voyDep)
            elif len(voyRet) != 1:
                voyage.append(voyRet)

    return voyage
