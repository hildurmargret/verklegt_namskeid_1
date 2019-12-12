from DataLayer.getAircraft import*
def saveAircraftInFile(newAircraft):
    aircraft = list_all_aircraft()

    path="/Users/hildur/Documents/github/verklegt_namskeid_1/csvFiles/AircraftCopy.csv"
    f=open(path, "a")

    f.write(newAircraft.planeInsignia+","+newAircraft.planeTypeId+"\n")

    exists_bool=0

    for plane in aircraft:
        if plane.planeTypeId == newAircraft.planeTypeId:
            exists_bool=1
            break

    if not exists_bool:
        path="/Users/hildur/Documents/github/verklegt_namskeid_1/csvFiles/AircraftType copy.csv"
        f=open(path, "a")
        f.write(newAircraft.planeTypeId+","+newAircraft.manufacturer+","+newAircraft.airplaneModel+","+newAircraft.capacity+","+newAircraft.emptyWeight+","+newAircraft.maxTakeoffWeight+","+newAircraft.unitThrust+","+newAircraft.serviceCeiling+","+newAircraft.unitThrust+","+newAircraft.length+","+newAircraft.height+","+newAircraft.wingspan+"\n")
