
import csv
from Date import*

def voyageByWeek():

    path='/Users/valdisbaerings/Documents/verklegt_namskeid_1/Documents/github/Verklegt1/UPDATEDSTUDENTDATA/'

    file1=path+'PastFlights.csv'
    file2=path+'UpcomingFlights copy.csv'

    inpt=33
    #firstDate, lastDate = getWeek(inpt)

    firstDate='20/12/2019'
    lastDate='24/12/2019'

    #firstDay = str(getDay(firstDate)
    #firstMonth = str(getMonth(firstDate)
    #firstYear = str(getYear(firstDate)

    #lastDay = str(getDay(lastDate)
    #lastMonth = str(getMonth(lastDate)
    #lastYear = str(getYear(lastDate)

    firstDay = str(firstDate[0:2]) #LAGA
    firstMonth = str(firstDate[3:5]) #LAGA
    firstYear = str(firstDate[6:10]) #LAGA

    lastDay = str(lastDate[0:2]) #LAGA
    lastMonth = str(lastDate[3:5]) #LAGA
    lastYear = str(lastDate[6:10]) #LAGA

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

    with open(file2,'r') as csv_file:
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