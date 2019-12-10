from ModelClasses.Staff import*
def saveStaffInFile(newStaff):
    path="/Users/hildur/Documents/github/verklegt_namskeid_1/csvFiles/CrewCopy.csv"
    f=open(path, "a")
    f.write(newStaff.SSN+","+newStaff.name+","+newStaff.role+","+newStaff.rank+","+newStaff.licence+","+newStaff.address+","+newStaff.phoneNumber+"\n")

# def saveCabinInFile(newStaff):
#     path="/Users/palinakroyer/github/verklegt_namskeid_1/csvFiles/CrewCopy.csv"
#     f=open(path, "a")
#     f.write(newStaff.SSN+","+newStaff.name+","+newStaff.role+","+newStaff.rank+","+"N/A"+newStaff.address+","+newStaff.phoneNumber+"\n")
