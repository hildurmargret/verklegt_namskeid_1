from DataLayer.OpenFile import*
import csv

def airplaineCapacity(planeInsigniaIn):

    insignia=[]
    planeType=[]
    planeType2=[]
    capacityRow=[]

    fileName1='Aircraft.csv'
    fileName2='AircraftType.csv'
    file1=OpenFile(fileName1)
    file2=OpenFile(fileName2)

    with file1 as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            planeType.append(row['planeTypeId'])
            insignia.append(row['planeInsignia'])
        for i in range (len(insignia)):
            if insignia[i]==planeInsigniaIn:
                TypeOut=planeType[i]
                print(TypeOut)
    csvfile.close()

    with file2 as csvfile2:
        reader2 = csv.DictReader(csvfile2)
        for row in reader2:
            planeType2.append(row['planeTypeId'])
            capacityRow.append(row['capacity'])
        for i in range (len(planeType2)):
            if planeType2[i]==TypeOut:
                capacityOut=capacityRow[i]
        csvfile2.close

    return capacityOut
