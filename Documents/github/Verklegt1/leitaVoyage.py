import csv
from Date import*

def leitaVoyage():

    path = '/Users/hildur/Documents/github/verklegt_namskeid_1/Documents/github/Verklegt1/UPDATEDSTUDENTDATA/'
    file1 = path + 'UpcomingFlights copy.csv'
    file2 = path + 'PastFlights.csv'

    inpt = 'NA013' #flugnumer
    dest = inpt[2:4]
    no = int(inpt[4:len(inpt)])
    voyage = []
    voyRet = ['VOYAGE RETURN:']
    voyDep = ['VOYAGE DEPARTURE:']


    with open(file1,'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
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

            voyage.append(voyDep)
            voyage.append(voyRet)

    return voyage

bla = leitaVoyage()
print(bla[0][0])
print(bla[0][1])
print(bla[1][0])
print(bla[1][1])
