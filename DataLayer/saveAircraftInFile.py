def saveAircraftInFile(newAircraft):
    path="/Users/palinakroyer/github/verklegt_namskeid_1/csvFiles/AircraftCopy.csv"
    f=open(path, "a")
    f.write(newAircraft.planeTypeId+","+newAircraft.manufacturer+","+newAircraft.airplaneModel+","+newAircraft.capacity+","+newAircraft.emptyWeight+","+newAircraft.maxTakeoffWeight+","+newAircraft.unitThrust+","+newAircraft.maxTakeoffWeight+","+newAircraft.unitThrust+","+newAircraft.length+","+newAircraft.height+","+newAircraft.wingspan+"\n")
