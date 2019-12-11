
import csv
from LogicLayer.Date import*
from ModelClasses.Voyage import*
from ModelClasses.flightRoute import*
from LogicLayer.leitaVoyage import*

def voyageByWeek(inpt, inpt_year):

    path='/Users/hildur/Documents/github/verklegt_namskeid_1/csvFiles/'

    daterange = getDateRangeFromWeek(inpt, inpt_year)

    # firstDay = str(getDay(daterange[1]))
    # firstMonth = str(getMonth(daterange[1]))
    # firstYear = str(getYear(daterange[1]))
    #
    # lastDay = str(getDay(daterange[0]))
    # lastMonth = str(getMonth(daterange[0]))
    # lastYear = str(getYear(daterange[0]))

    voyages = []
    retVoyages = []
    # voyRet = []
    # voyDep = []
    # depDay = []
    # depMonth = []
    # depYear = []
    # depMinute = []
    # depHour = []
    # arrDay = []
    # arrMonth = []
    # arrYear = []
    # arrMinute = []
    # arrHour = []
    # tel=0

    today=now()

    if today>daterange[1]:
        file=path+'PastFlights.csv'
    else:
        file=path+'UpcomingFlights copy.csv'

    with open(file,'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:

            if daterange[1] <= row['departure'] and daterange[0] >= row['departure']:
                voyage = leitaVoyage(row['flightNumber'])
                voyages.append(voyage)
                #print(voyage.departureFlight.flightNumber)

    # for i in voyages:
    #     print(type(i))
    #     if i.departureFlight.flightNumber not in retVoyages:
    #         retVoyages.append(i)

    return voyages

            # depDay.append(str(getDay(row['departure'])))
            # depMonth.append(str(getMonth(row['departure'])))
            # depYear.append(str(getYear(row['departure'])))
            # depMinute.append(str(getMinute(row['departure'])))
            # depHour.append(str(getHour(row['departure'])))
            # arrDay.append(str(getDay(row['arrival'])))
            # arrMonth.append(str(getMonth(row['arrival'])))
            # arrYear.append(str(getYear(row['arrival'])))
            # arrMinute.append(str(getMinute(row['arrival'])))
            # arrHour.append(str(getHour(row['arrival'])))


            # flugnr=row['flightNumber']
            # deptDay = str(row['departure'][0:2])
            # deptMonth = str(row['departure'][3:5])
            # deptYear = str(row['departure'][6:10])
            # deptHour = str(row['departure'][11:13])
            # deptMin = str(row['departure'][14:16])
            # arvlDay = str(row['arrival'][0:2])
            # arvlMonth = str(row['arrival'][3:5])
            # arvlYear = str(row['arrival'][6:10])
            # arvlHour = str(row['arrival'][11:13])
            # arvlMin = str(row['arrival'][14:16])

            #no=int(flugnr[4:len(flugnr)])

    #         if daterange[1] <= row['departure'] and daterange[0] >= row['departure']:
    #             deptTime = deptDay + '/' + deptMonth + '/' + deptYear + ' at ' + deptHour + ':' + deptMinute
    #             arvlTime = arvlDay + '/' + arvlMonth + '/' + arvlYear + ' at ' + arvlHour + ':' + arvlMinute
    #
    #         # if firstDay <= depDay[tel] and firstMonth <= depMonth[tel] and firstYear <= depYear[tel] and lastDay >= depDay[tel] and lastMonth >= depMonth[tel] and lastYear >= depYear[tel]:
    #         #     deptTime = depDay[tel] + '/' + depMonth[tel] + '/' + depYear[tel] + ' at ' + depHour[tel] + ':' + depMinute[tel]
    #         #     arvlTime = arrDay[tel] + '/' + arrMonth[tel] + '/' + arrYear[tel] + ' at ' + arrHour[tel] + ':' + arrMinute[tel]
    #
    #             if no%2 == 0:
    #                 flight=createFlightRoute(row['flightNumber'], row['departingFrom'], row['arrivingAt'], deptTime, arvlTime,0,0)
    #                 voyage.departureFlight = flight
    #                 #voyDep.append(voyD)
    #
    #
    #             elif no%2 != 0:
    #                 flight=createFlightRoute(row['flightNumber'], row['departingFrom'], row['arrivingAt'], deptTime, arvlTime,0,0)
    #                 voyage.returnFlight = flight
    #                 #voyRet.append(voyR)
    #
    #         tel=tel+1
    #
    # return voyDep, voyRet
