import csv
from DataLayer.OpenFile import *

def getAllTypes():

    #fall sem nær í allar flugvélatýpur

    file1='AircraftCopy.csv'

    file_=OpenFile(file1)

    tempTypes = []
    retTypes = []

    with file_ as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            tempTypes.append(row['planeTypeId'])

    for i in tempTypes:
        if i not in retTypes:
            retTypes.append(i)

    return retTypes
