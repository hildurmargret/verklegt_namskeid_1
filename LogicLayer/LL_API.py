#from Date import*
#from getPilotsByAirplanes import*
#from getPilotsByLicence import*

##def PilotsByAirplanes()

from UILayer.Windows import*
from DataLayer.saveStaffInFile import*
from DataLayer.saveAircraftInFile import*
from DataLayer.DL_API import*
from LogicLayer.getAircraft import*
#from UILayer.UI_Manager import*

DL=DL_API()
#UI = UI_Manager()

class LL_API:

    def __init__(self):
        pass

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
    def LLgetAircraft(self):
        getAircraft = list_all_aircraft()
        print("HIIII")
        return getAircraft
        #UI.gettingAirplanes(getAircraft)
