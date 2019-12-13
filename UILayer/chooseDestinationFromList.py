def DestinationFromList(dest):

    #fall sem býr til lista af destination fyrir notanda til að velja úr
    for i in range(len(dest)):
        print(i+1,end=" ")
        print(dest[i].id + ", " + dest[i].destination) # + ", "+ dest[i].country + ", "  + dest[i].distance + ", " + dest[i].contactName + ", " + dest[i].contactNumber)
    inp=int(input("Destination: "))
    if inp == 0:
        return 0
    else:
        dest=dest[inp-1]
        return dest
