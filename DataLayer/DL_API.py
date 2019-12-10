from DataLayer.saveStaffInFile import*
from DataLayer.saveAircraftInFile import*
from DataLayer.saveNewDestination import*
from DataLayer.saveVoyage import*
from DataLayer.saveUpdatedStaff import*
from DataLayer.saveUpdatedDestination import*

class DL_API:

    def __init__(self):
        pass

    def DLsaveStaff(self, newStaff):
        saveStaffInFile(newStaff)
    #def DLsavePilot(self, newStaff):
    #    savePilotInFile(newStaff)
    def DLsaveAircraft(self,newAircraft):
        saveAircraftInFile(newAircraft)
    def DLsaveDestination(self,newDest):
        saveDestinationInFile(newDest)
    def DLsaveVoyage(self,newVoyage):
        saveVoyageInFile(newVoyage)
    def DLupdateStaff(self,employee):
        saveUpdatedStaff(employee)
    def DLupdatedDestination(self, destination):
        saveUpdatedDest(destination)
    def DLupdateAircraft(self,aircraft):
        saveUpdatedAircraft(aircraft)
