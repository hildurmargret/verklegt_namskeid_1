from DataLayer.saveStaffInFile import*
from DataLayer.saveAircraftInFile import*
from DataLayer.saveNewDestination import*
from DataLayer.saveVoyage import*
from DataLayer.saveUpdatedStaff import*
from DataLayer.saveUpdatedDestination import*
from DataLayer.saveEmployeesToVoyage import*
from DataLayer.saveUpdatedVoyage import*

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
    def DLcopyExistingVoyage(voyage):
        saveVoyage(voyage)
    def DLupdateStaff(self,employee):
        saveUpdatedStaff(employee)
    def DLupdatedDestination(self, destination):
        saveUpdatedDest(destination)
    def DLupdateAircraft(self,aircraft):
        saveUpdatedAircraft(aircraft)
    def DLupdateVoyage(self,voyage):
        saveUpdatedVoyage(voyage)
    def DLemployeesToVoyage(self,voyage,employee):
        employeesToVoyage(voyage,employee)
