from Date import*
def printWS(pastDest,pastDept,pastDeptTime,pastArvlTime,upcDest,upcDept,upcDeptTime,upcArvlTime,pastFlNo,employees):

    for k in range(len(employees)):
        print employees[k]
        print
        print('PAST FLIGHTS')
        for j in range(len(pastFlNo)):
            print('Flight number: ' + pastFlNo[j] + ', From ' + pastDept[j] + ' to ' + pastDest[j] + ','),
            print('Departure: ' + str(getDay(pastDeptTime[j])) + '/' + str(getMonth(pastDeptTime[j])) + '/' + str(getYear(pastDeptTime[j])) + ' at ' + str(getHour(pastDeptTime[j])) + ':' + str(getMinute(pastDeptTime[j])) + ','),
            print('Arrival: ' + str(getDay(pastArvlTime[j])) + '/' + str(getMonth(pastArvlTime[j])) + '/' + str(getYear(pastArvlTime[j])) + ' at ' + str(getHour(pastArvlTime[j])) + ':' + str(getMinute(pastArvlTime[j])))
        print

        print('UPCOMING FLIGHTS')
        for j in range(len(pastFlNo)):
            print('Flight number: ' + pastFlNo[j] + ', From ' + pastDept[j] + ' to ' + pastDest[j] + ','),
            print('Departure: ' + str(getDay(pastDeptTime[j])) + '/' + str(getMonth(pastDeptTime[j])) + '/' + str(getYear(pastDeptTime[j])) + ' at ' + str(getHour(pastDeptTime[j])) + ':' + str(getMinute(pastDeptTime[j])) + ','),
            print('Arrival: ' + str(getDay(pastArvlTime[j])) + '/' + str(getMonth(pastArvlTime[j])) + '/' + str(getYear(pastArvlTime[j])) + ' at ' + str(getHour(pastArvlTime[j])) + ':' + str(getMinute(pastArvlTime[j])))
            """print('Flight number: ' + upcFlNo[j] + ', From ' + upcDept[j] + ' to ' + upcDest[j] + ','),
            print('Departure: ' + str(getDay(upcDeptTime[j])) + '/' + str(getMonth(upcDeptTime[j])) + '/' + str(getYear(upcDeptTime[j])) + ' at ' + str(getHour(upcDeptTime[j])) + ':' + str(getMinute(upcDeptTime[j])) + ','),
            print('Arrival: ' + str(getDay(upcArvlTime[j])) + '/' + str(getMonth(upcArvlTime[j])) + '/' + str(getYear(upcArvlTime[j])) + ' at ' + str(getHour(upcArvlTime[j])) + ':' + str(getMinute(upcArvlTime[j])))"""
        print
        print('-----------------------------------------------------------------------------------------------------')
        print

        #PALINA input('Choose y to save')
    inpt = 1

    return inpt
