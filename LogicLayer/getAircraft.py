import csv
from ModelClasses.Airplane import*

def list_all_aircraft():

    path="/Users/SaraLind/github/verklegt_namskeid_1/csvFiles/"
    skra1='AircraftType.csv'
    skra2='Aircraft.csv'
    skra3='Crew.csv'

    file1 = path + skra1
    file2 = path + skra2

    line1 = []
    line2 = []


    with open(file2,'r') as csv_file:
        csv_reader2 = csv.DictReader(csv_file)
        for row1 in csv_reader2:
            insignia= row1["planeInsignia"]
            planeType = row1["planeTypeId"]
            with open(file1,'r') as csv_file:
                csv_reader1 = csv.DictReader(csv_file)
                for row in csv_reader1:
                    if row['planeTypeId']==planeType:
                        air1 = createAirplane(row['planeTypeId'], row['manufacturer'], row['model'], row['capacity'], row['emptyWeight'], row['maxTakeoffWeight'], row['unitThrust'], row['serviceCeiling'], row['length'], row['height'], row['wingspan'])
                        air1.planeInsignia=insignia
                        line2.append(air1)
        #    for line in csv_reader2:
        #        line1.append(line)
        #    print(line1)
        #    print(len(line1))
    #    print(line2)
    #         line1.append(air2)
    #
    # with open(file1,'r') as csv_file:
    #     csv_reader1 = csv.DictReader(csv_file)
    #     for row in csv_reader1:
    #         air1 = createAirplane(row['planeTypeId'], row['manufacturer'], row['model'], row['capacity'], row['emptyWeight'], row['maxTakeoffWeight'], row['unitThrust'], row['serviceCeiling'], row['length'], row['height'], row['wingspan'])
    #         line2.append(air1)

#for row1 in line1:
#    for row2 in line2:
            #if row1["planeInsignia"]==



    return line2

    #list_all_aircraft()
