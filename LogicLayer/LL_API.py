#from Date import*
#from getPilotsByAirplanes import*
#from getPilotsByLicence import*

##def PilotsByAirplanes()

from UILayer.Windows import*
from DataLayer.saveStaffInFile import*
from DataLayer.saveAircraftInFile import*
from DataLayer.DL_API import*
from DataLayer.saveUpdatedDestination import*
from DataLayer.getAircraft import*
from LogicLayer.getStaff1_4nytt import*
from DataLayer.getDestinations import*
from LogicLayer.leitaVoyage import*
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
    def LLcopyExistingVoyage(self,voyage,inp,iter):
        if inp==1:
            self.LLsaveVoyage(voyage)

        elif inp==2:
            for i in range(iter):
                pass




    def LLgettingVoyage(self,input_string):
        voyage=leitaVoyage(input_string)
        return voyage
        #UI.gettingAirplanes(getAircraft)
    def LLupdateStaff(self,input_string):
        employees=staffInfo(4, input_string)
        return employees

        return employees
    def LLupdatingStaff(self,employee):
        DL.DLupdateStaff(employee)

    def LLupdateDestination(self):
        destination=getAllDestinations()
        return destination

    def LLupdatingDestination(self,destination):
        DL.DLupdatedDestination(destination)

    def LLupdateAircraft(self,aircraft):
        DL.DLupdateAircraft(aircraft)

    def LLupdateVoyage(self,voyage):
        DL.DLupdateVoyage(voyage)

    def LLgettingEmployees(self,input_string):
        employees=staffInfo(4,input_string)
        return employees

    def LLemployeesToVoyage(self,voyage,employee):
        DL.DLemployeesToVoyage(voyage,employee)
