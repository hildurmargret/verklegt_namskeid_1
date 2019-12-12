def DestinationFromList(dest):
    
    for i in range(len(dest)):
        print(i+1,end=" ")
        print(dest[i].id + ", " + dest[i].destination + ", "+ dest[i].country + ", "  + dest[i].distance + ", " + dest[i].contactName + ", " + dest[i].contactNumber)
    inp=int(input("destination: "))
    dest=dest[inp-1]
    return dest
