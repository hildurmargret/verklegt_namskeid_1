import csv

def getAllTypes():

    path='/Users/hildur/Documents/github/verklegt_namskeid_1/csvFiles/'

    file1 = path + 'Aircraft.csv'

    tempTypes = []
    retTypes = []

    with open(file1,'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            tempTypes.append(row['planeTypeId'])

    for i in tempTypes:
        if i not in retTypes:
            retTypes.append(i)

    return retTypes
