from ModelClasses.Destination import*

def mostPOPinfo(mostpop, destList):

    info=[]

    #tek inn lista af dest og id a vinsælasta staðnum
    #fer i gegnum dest listann og finn hvaða dest passar við mostpop
    #by til klasatilvik af þeim stað sem passar við og skila þeim ut
    for i in range(len(destList)):
        if destList[i].id == mostpop:
            info=CreateDestination(destList[i].id, destList[i].destination, destList[i].country, destList[i].distance, destList[i].contactName, destList[i].contactNumber)

    return info
