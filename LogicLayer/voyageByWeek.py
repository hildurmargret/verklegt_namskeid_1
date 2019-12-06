
import csv
from Date import*

def voyageByWeek():

    path='/Users/valdisbaerings/Documents/verklegt_namskeid_1/Documents/github/Verklegt1/UPDATEDSTUDENTDATA/'

    inpt=50
    inpt_year=2019
    daterange = getDateRangeFromWeek(inpt, inpt_year)
    #print daterange

    firstDay = str(getDay(daterange[1]))
    firstMonth = str(getMonth(daterange[1]))
    firstYear = str(getYear(daterange[1]))

    lastDay = str(getDay(daterange[0]))
    lastMonth = str(getMonth(daterange[0]))
    lastYear = str(getYear(daterange[0]))

    voyRet = []
    voyDep = []
    depDay = []
    depMonth = []
    depYear = []
    depMinute = []
    depHour = []
    arrDay = []
    arrMonth = []
    arrYear = []
    arrMinute = []
    arrHour = []
    tel=0

    today=now()

    if today>daterange[1]:
        file=path+'PastFlights.csv'
    else:
        file=path+'UpcomingFlights copy.csv'
    #print file

    with open(file,'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            depDay.append(str(getDay(row['departure'])))
            depMonth.append(str(getMonth(row['departure'])))
            depYear.append(str(getYear(row['departure'])))
            depMinute.append(str(getMinute(row['departure'])))
            depHour.append(str(getHour(row['departure'])))
            arrDay.append(str(getDay(row['arrival'])))
            arrMonth.append(str(getMonth(row['arrival'])))
            arrYear.append(str(getYear(row['arrival'])))
            arrMinute.append(str(getMinute(row['arrival'])))
            arrHour.append(str(getHour(row['arrival'])))

            flugnr=row['flightNumber']
            no=int(flugnr[4:len(flugnr)])
            #print no

            if firstDay <= depDay[tel] and firstMonth <= depMonth[tel] and firstYear <= depYear[tel] and lastDay >= depDay[tel] and lastMonth >= depMonth[tel] and lastYear >= depYear[tel]:
                deptTime = depDay[tel] + '/' + depMonth[tel] + '/' + depYear[tel] + ' at ' + depHour[tel] + ':' + depMinute[tel]
                arvlTime = arrDay[tel] + '/' + arrMonth[tel] + '/' + arrYear[tel] + ' at ' + arrHour[tel] + ':' + arrMinute[tel]

                if no%2 == 0:
                    voyDep.append(row['flightNumber'] + ', ' + row['departingFrom'] + ', ' + row['arrivingAt'] + ', Departure: ' + deptTime + ', Arrival: ' + arvlTime)

                elif no%2 != 0:
                    voyRet.append(row['flightNumber'] + ', ' + row['departingFrom'] + ', ' + row['arrivingAt'] + ', Departure: ' + deptTime + ', Arrival: ' + arvlTime)
            tel=tel+1

    return voyDep, voyRet

dep, ret = voyageByWeek()

for i in range(len(dep)):
    print('VOYAGE DEPARTURE')
    print dep[i]
    print('VOYAGE RETURN')
    print ret[i]
    print
