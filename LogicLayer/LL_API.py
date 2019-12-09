#from Date import*
#from getPilotsByAirplanes import*
#from getPilotsByLicence import*

#def PilotsByAirplanes()

from UILayer.Windows import*
from DataLayer.saveStaffInFile import*
from DataLayer.saveAircraftInFile import*
from DataLayer.DL_API import*
DL=DL_API()

class LL_API():
    def LLsaveCabin(self,newStaff):
        DL.DLsaveCabin(newStaff)
    def LLsavePilot(self,newStaff):
        DL.DLsavePilot(newStaff)
    def LLsaveAircraft(self,newAircraft):
        DL.DLsaveAircraft(newAircraft)
    def LLsaveDestination(self,newDestination):
        DL. DLsaveDestination(NewDest)
    def LLsaveVoyage(self,newVoyage):
        DL.DLsaveVoyage(newVoyage)
