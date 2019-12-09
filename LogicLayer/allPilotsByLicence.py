from ModelClasses.Staff import*
from LogicLayer.searchPilotByLicence import*
import csv
def allPilotsByLicence():

    path='/Users/hildur/Documents/github/verklegt_namskeid_1/csvFiles/'

    file1 = path + 'Aircraft.csv'

    tempTypes = []
    retTypes = []
    pilots = []
    komid_bool = 0

    with open(file1,'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            tempTypes.append(row['planeTypeId'])

    for i in tempTypes:
        if i not in retTypes:
            retTypes.append(i)

    for k in range(len(retTypes)):
        pilotByLicence = searchPilotsByLicence(retTypes[k])

    return pilots
