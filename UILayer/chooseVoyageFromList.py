from LogicLayer.Date import*
def chooseVoyage(voyages):

    #fall sem býr til lista af voyages til að velja úr
    for j in range(len(voyages)):
        deptTime = str(getDay(voyages[j].departureFlight.departure)) + '/' + str(getMonth(voyages[j].departureFlight.departure)) + '/' + str(getYear(voyages[j].departureFlight.departure))
        arvlTime = str(getDay(voyages[j].departureFlight.arrival)) + '/' + str(getMonth(voyages[j].departureFlight.arrival)) + '/' + str(getYear(voyages[j].departureFlight.arrival))

        print(j+1,end="")
        print(' Voyage from KEF to ' + voyages[j].departureFlight.arrivingAt + ", Departure date:  " + deptTime)
    inp=int(input("Number: "))
    voyage=voyages[inp-1]
    return voyage
