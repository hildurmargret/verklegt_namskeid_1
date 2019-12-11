import csv
from DataLayer.OpenFile import *

def getAllTypes():

    #path='/Users/hildur/Documents/github/verklegt_namskeid_1/csvFiles/'

    file1='Aircraft.csv'

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
