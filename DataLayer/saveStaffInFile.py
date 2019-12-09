from ModelClasses.Staff import*
def savePilotInFile(newStaff):
    path="/Users/palinakroyer/github/verklegt_namskeid_1/DataLayer/UPDATEDSTUDENTDATA/CrewCopy.csv"
    f=open(path, "a")
    f.write(newStaff.SSN+","+newStaff.name+","+newStaff.rank+","+newStaff.number)

def saveCabinInFile(newStaff):
    path="/Users/palinakroyer/github/verklegt_namskeid_1/Documents/github/Verklegt1/DataLayer/UPDATEDSTUDENTDATA/CrewCopy.csv"
    f=open(path, "a")
    f.write(newStaff.SSN+","+newStaff.name+","+newStaff.rank+","+newStaff.number)
