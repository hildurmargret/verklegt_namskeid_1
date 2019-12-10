import csv

def OpenFile(fileName):

    path='/Users/hildur/Documents/github/verklegt_namskeid_1/csvFiles/'
    #fileName = 'Destinations.csv'

    file = path + fileName

    openFile = open(file, "r")
    return openFile
