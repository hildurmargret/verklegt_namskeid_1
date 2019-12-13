from ModelClasses.Staff import*
import sys
import os
def saveStaffInFile(newStaff):

    #vista starfsmann í skrá
    ##path="/Users/hildur/Documents/github/verklegt_namskeid_1/csvFiles/CrewCopy.csv"

    absPathFile = os.path.abspath(__file__)
    fileDir = os.path.dirname(os.path.abspath(__file__))
    parentDir = os.path.dirname(fileDir)
    path = parentDir + "/csvFiles/CrewCopy.csv"

    f=open(path, "a")
    f.write(newStaff.SSN+","+newStaff.name+","+newStaff.role+","+newStaff.rank+","+newStaff.licence+","+newStaff.address+","+newStaff.phoneNumber+"\n")
