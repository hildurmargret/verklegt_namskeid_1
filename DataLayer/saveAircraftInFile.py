import sys
import os
from DataLayer.getAircraft import*
def saveAircraftInFile(newAircraft):

    #fall sem vistar nýja flugvél í skrá
    aircraft = list_all_aircraft()

    ##path="/Users/valdisbaerings/Documents/github/verklegt_namskeid_1/csvFiles/AircraftCopy.csv"

    absPathFile = os.path.abspath(__file__)
    fileDir = os.path.dirname(os.path.abspath(__file__))
    parentDir = os.path.dirname(fileDir)
    path = parentDir + "/csvFiles/"

    file = path + 'AircraftCopy.csv'

    f=open(file, "a")

    f.write(newAircraft.planeInsignia+","+newAircraft.planeTypeId+"\n")

    exists_bool=0

    for plane in aircraft:
        if plane.planeTypeId == newAircraft.planeTypeId:
            exists_bool=1
            break

    if not exists_bool:
        ##path="/Users/valdisbaerings/Documents/github/verklegt_namskeid_1/csvFiles/AircraftType copy.csv"

        file = path + "AircraftType copy.csv"

        f=open(file, "a")
        f.write(newAircraft.planeTypeId+","+newAircraft.manufacturer+","+newAircraft.airplaneModel+","+newAircraft.capacity+","+newAircraft.emptyWeight+","+newAircraft.maxTakeoffWeight+","+newAircraft.unitThrust+","+newAircraft.serviceCeiling+","+newAircraft.unitThrust+","+newAircraft.length+","+newAircraft.height+","+newAircraft.wingspan+"\n")
