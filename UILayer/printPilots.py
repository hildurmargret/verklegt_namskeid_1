def printPilotList(pilots):

    #fall til að prenta út lista af flugmönnum

    for i in range(len(pilots)):
        print(pilots[i].name + ', ' + pilots[i].SSN + ', ' + pilots[i].address + ', ' + pilots[i].phoneNumber + ', ' + pilots[i].role + ', ' + pilots[i].rank + ', ' + pilots[i].licence)
