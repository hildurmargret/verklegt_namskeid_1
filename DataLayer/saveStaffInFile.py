from ModelClasses.Staff import*
def savePilotInFile(SSN,name,rank,licence,number):
    path="/Users/palinakroyer/github/verklegt_namskeid_1/Documents/github/Verklegt1/UPDATEDSTUDENTDATA/Crew.csv"
    f=open(path, "a")
    f.write(SSN+","+name+","+rank+","+number)

def saveCabinInFile(SSN,name,rank,number):
    path="/Users/palinakroyer/github/verklegt_namskeid_1/Documents/github/Verklegt1/UPDATEDSTUDENTDATA/Crew.csv"
    f=open(path, "a")
    f.write(SSN+","+name+","+rank+","+number)
