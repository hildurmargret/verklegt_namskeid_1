import csv

def OpenFile(fileName):

    path='/Users/SaraLind/github/verklegt_namskeid_1/Documents/github/Verklegt1/UPDATEDSTUDENTDATA/'
    #fileName = 'Destinations.csv'

    file = path + fileName

    openFile = open(file, "r")
    return openFile
