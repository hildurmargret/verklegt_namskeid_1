#
def printAircraft(Airplanes):
    print(Airplanes)
    print("planeTypeId, manufacturer, airplaneModel, capacity, emptyWeight, maxTakeoffWeight, unitThrust, serviceCeiling, length, height, wingspan")
    for i in range(len(Airplanes)):
        print(Airplanes[i].planeTypeId + ", " + Airplanes[i].manufacturer + ", "+ Airplanes[i].airplaneModel + ", "  + Airplanes[i].capacity + ", " + Airplanes[i].emptyWeight + ", " + Airplanes[i].maxTakeoffWeight + ", " + Airplanes[i].unitThrust + ", " + Airplanes[i].serviceCeiling + ", " + Airplanes[i].length + ", " + Airplanes[i].height + ", " + Airplanes[i].wingspan)
#     print(Airplanes)
