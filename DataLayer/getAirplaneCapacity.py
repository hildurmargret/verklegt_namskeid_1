from DataLayer.OpenFile import*
import csv

def airplaneCapacity(planeInsigniaIn):

    #fall sem nær í sætisfjölda fljugvélar eftir typu hennar

    insignia=[]
    planeType=[]
    planeType2=[]
    capacityRow=[]

    fileName1='AircraftCopy.csv'
    fileName2='AircraftType copy.csv'
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
                #print(TypeOut)
            # else:
            #     TypeOut=0
    csvfile.close()

    with file2 as csvfile2:
        reader2 = csv.DictReader(csvfile2)
        for row in reader2:
            planeType2.append(row['planeTypeId'])
            capacityRow.append(row['capacity'])
        for i in range (len(planeType2)):
            if planeType2[i]==TypeOut:
                capacityOut=int(capacityRow[i])
            # else:
            #     capacityOut='UNKNOWN'
        csvfile2.close()

    return capacityOut
