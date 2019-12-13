import csv
from ModelClasses.Airplane import*
from DataLayer.OpenFile import *

def list_all_aircraft():

    #fall sem nær i allar flugvelar

    skra1='AircraftType copy.csv'
    skra2='AircraftCopy.csv'

    file2=OpenFile(skra2)

    aircraft = []

    with file2 as csv_file:
        csv_reader2 = csv.DictReader(csv_file)
        for row1 in csv_reader2:
            insignia= row1["planeInsignia"]
            planeType = row1["planeTypeId"]
            file1=OpenFile(skra1)
            with file1 as csv_file:
                csv_reader1 = csv.DictReader(csv_file)
                for row in csv_reader1:
                    if row['planeTypeId']==planeType:
                        air1 = createAirplane(row['planeTypeId'], row['manufacturer'], row['model'], row['capacity'], row['emptyWeight'], row['maxTakeoffWeight'], row['unitThrust'], row['serviceCeiling'], row['length'], row['height'], row['wingspan'])
                        air1.planeInsignia=insignia
                        aircraft.append(air1)

    return aircraft
