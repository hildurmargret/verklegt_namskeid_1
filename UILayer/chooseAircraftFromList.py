def aircraftFromList(Airplanes):

    #prentar allar flugvélar með lista fyrir notanda til að velja úr
    for i in range(len(Airplanes)):
        print(i+1,end="")
        print(Airplanes[i].planeTypeId + ", " + Airplanes[i].manufacturer + ", "+ Airplanes[i].airplaneModel + ", "  + Airplanes[i].capacity + ", " + Airplanes[i].emptyWeight + ", " + Airplanes[i].maxTakeoffWeight + ", " + Airplanes[i].unitThrust + ", " + Airplanes[i].serviceCeiling + ", " + Airplanes[i].length + ", " + Airplanes[i].height + ", " + Airplanes[i].wingspan)
    inp=int(input("number: "))
    airplane=Airplanes[inp-1]
    return airplane
