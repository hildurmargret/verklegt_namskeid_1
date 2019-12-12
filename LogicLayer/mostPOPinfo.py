from ModelClasses.Destination import*

def mostPOPinfo(mostpop, destList):

    info=[]

    for i in range(len(destList)):
        if destList[i].id == mostpop:
            info=CreateDestination(destList[i].id, destList[i].destination, destList[i].country, destList[i].distance, destList[i].contactName, destList[i].contactNumber)

    return info
