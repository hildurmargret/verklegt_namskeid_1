from ModelClasses.Staff import*
from LogicLayer.searchPilotByLicence import*
from DataLayer.getAllPlaneTypes import*
import csv
def allPilotsByLicence():

    pilots = []
    komid_bool = 0

    #fæ allar typur flugvela
    types = getAllTypes()

    #fer gegnum allar typur og finn hvaða pilots hafa leyfi a hverja vel
    for k in range(len(types)):
        pilotByLicence = searchPilotsByLicence(types[k])
        pilots.append(pilotByLicence)

    return pilots
