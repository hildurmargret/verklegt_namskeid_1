def saveAircraftInFile(newAircraft):
    path="/Users/palinakroyer/github/verklegt_namskeid_1/csvFiles/AircraftCopy.csv"
    f=open(path, "a")
    f.write(newAircraft.name+","+newAircraft.airplaneModel+","+newAircraft.manufacturer+","+newAircraft.seats+"\n")
