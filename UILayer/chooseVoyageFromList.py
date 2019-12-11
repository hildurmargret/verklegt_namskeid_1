
def chooseVoyage(voyages):
    for i in range(len(voyages)):
        print(i+1,end="")
        print(' Voyage from KEF to ' + voyages[i].departureFlight.arrivingAt + ", Date:  " + voyages[i].departureFlight.departure)
    inp=int(input("Number: "))
    voyage=voyages[inp-1]
    return voyage
