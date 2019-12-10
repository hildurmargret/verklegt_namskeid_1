import csv
from ModelClasses.Destination import*
def saveUpdatedDest(destination):

    Dest=[]
    path="/Users/SaraLind/github/verklegt_namskeid_1 /csvFiles/DestinationsCopy.csv"
    with open(path,'r') as File1:
        csv_reader = csv.DictReader(File1)
        for row in csv_reader:
            Destination = createDest(row['id'],row['destination'])
            Dest.append(Destination)
    File1.close()

    f=open(path, 'w')

    writer = csv.writer(f)
    writer.writerow( ('id', 'destination' ))

    for i in range(len(Dest)):
        if Dest[i].contactName==destination.contactName:
            writer.writerow((destination.contactName))
        elif Dest[i].contactNumber==destination.contactNumber:
            writer.writerow((destination.contactNumber))
        else:
            writer.writerow((destination[i].contactName,destination[i].contactNumber))
