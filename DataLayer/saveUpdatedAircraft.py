def saveUpdatedAircraft(aircraft):
    air=[]
    path="/Users/palinakroyer/github/verklegt_namskeid_1/csvFiles/AircraftTypeCopy.csv"
    with open(path,'r') as File1:
        csv_reader = csv.DictReader(File1)
        for row in csv_reader:
            airc = createStaff(row['planeTypeId'],row['manufacturer'],row['model'],row['capacity'],'emptyWeight',row['maxTakeoffWeight'],row['unitThrust'],row['serviceCeiling'],row['length'],row['height'],row['wingspan'])
            air.append(airc)
    File1.close()

    f=open(path, 'w')

    writer = csv.writer(f)
    writer.writerow( ('planeTypeId','manufacturer','model','capacity','emptyWeight','maxTakeoffWeight','unitThrust','serviceCeiling','length','height','wingspan') )

    for i in range(len(aircraft)):
        if air[i].SSN==aircraft.SSN:
            writer.writerow((aircraft.SSN,aircraft.name,aircraft.role,aircraft.rank,aircraft.licence,aircraft.address,aircraft.phoneNumber))
        else:
            writer.writerow((air[i].SSN,air[i].name,air[i].role,air[i].rank,air[i].licence,air[i].address,air[i].phoneNumber))
