#from Date import*
#from getPilotsByAirplanes import*
#from getPilotsByLicence import*

##def PilotsByAirplanes()

from UILayer.Windows import*
from DataLayer.saveStaffInFile import*
from DataLayer.saveAircraftInFile import*
from DataLayer.DL_API import*
from DataLayer.saveUpdatedDestination import*
from LogicLayer.getAircraft import*
from LogicLayer.getStaff1_4 import*
#from UILayer.UI_Manager import*

DL=DL_API()
#UI = UI_Manager()

class LL_API:

    def __init__(self):
        pass

    def LLsaveStaff(self, newStaff):
        DL.DLsaveStaff(newStaff)
    #def LLsavePilot(self, newStaff):
    #    DL.DLsavePilot(newStaff)

    def LLsaveAircraft(self,newAircraft):
        DL.DLsaveAircraft(newAircraft)
    def LLsaveDestination(self,newDest):
        DL. DLsaveDestination(newDest)
    def LLsaveVoyage(self,newVoyage):
        DL.DLsaveVoyage(newVoyage)
    def LLgetAircraft(self):
        getAircraft = list_all_aircraft()
        return getAircraft
        #UI.gettingAirplanes(getAircraft)
    def LLupdateStaff(self,input_string):
        employees=staffInfo(4, input_string)
        return employees

        return employees
    def LLupdatingStaff(self,employee):
        DL.DLupdateStaff(employee)

    def LLupdatingDestination(self,destination):
        DL.DLupdatedDestination(destination)
    def LLupdateAircraft(self,aircraft):
        DL.DLupdateAircraft(aircraft)
