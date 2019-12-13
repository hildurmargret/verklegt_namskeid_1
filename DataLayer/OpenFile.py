import csv
import sys
import os

def OpenFile(fileName):

    ##path='/Users/hildur/Documents/github/verklegt_namskeid_1/csvFiles/'
    absPathFile = os.path.abspath(__file__)
    fileDir = os.path.dirname(os.path.abspath(__file__))
    parentDir = os.path.dirname(fileDir)
    path = parentDir + "/csvFiles/"

    file = path + fileName

    openFile = open(file, "r")
    return openFile
