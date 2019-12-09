from DataLayer.saveStaffInFile import*
from DataLayer.saveAircraftInFile import*
from DataLayer.saveNewDestination import*

class DL_API():

    def DLsaveCabin(self,newStaff):
        saveCabinInFile(newStaff)
    def DLsavePilot(self,newStaff):
        savePilotInFile(newStaff)
    def DLsaveAircraft(self,newAircraft):
        saveAircraftInFile(newAircraft)
    def DLsaveDestination(NewDest):
        saveDestinationInFile(newDest)
