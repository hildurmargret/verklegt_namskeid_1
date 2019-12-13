def printDestList(numOfDest, pastFlights, employees):

    #fall til að prenta lista af áfangastoðum

    counter = 0

    for j in range(len(numOfDest)):

        for i in range(numOfDest[j]-counter):
            if pastFlights[i+counter].arrivingAt!='KEF':
                print(pastFlights[i].departure + ' to ' + pastFlights[i+counter].arrivingAt)

        counter=numOfDest[j]
        print('\n', end = '')

    return
