def printDestList(numOfDest, pastFlights, employees):

    counter = 0

    for j in range(len(numOfDest)):
        print(employees[j].name)

        for i in range(numOfDest[j]-counter):
            if pastFlights[i+counter].arrivingAt!='KEF':
                print(pastFlights[i].departure + ' to ' + pastFlights[i+counter].arrivingAt)

        counter=numOfDest[j]
        print('\n', end = '')

    return
