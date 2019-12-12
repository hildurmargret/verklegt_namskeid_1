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
from LogicLayer.fixFlightNumbers import*

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
    def LLsaveVoyage(self,newVoyage,file):
        [newVoyList,destinations]=DL.DLairportOccupied(newVoyage)
        newVoyList=fixFlNo(newVoyList,destinations)
        DL.DLsaveVoyage(newVoyList,file)

    def LLgetAircraft(self):
        getAircraft = list_all_aircraft()
        return getAircraft

    def LLcopyExistingVoyage(self,voyage,inp,date):
        voyageDate=voyage.departureFlight.departure
        dateNow=now()
        if voyageDate>dateNow:
            file="UpcomingFlights copy.csv"
        else:
            file="PastFlights copy.csv"
        if inp==1:
            self.LLsaveVoyage(voyage)
            self.LLsaveVoyage(voyage,file)
        elif inp==2:
            iter=int(input("Number of iterations: "))
            for i in range(iter):
                self.LLsaveVoyage(voyage)
                self.LLsaveVoyage(voyage,file)
                date=add_day(date,1)
                voyage.departureFlight.departure=date
                voyage.departureFlight.arrival=add_hour(date,3)
        elif inp==3:
            iter=int(input("Number of iterations: "))
            for i in range(iter):
                self.LLsaveVoyage(voyage)
                self.LLsaveVoyage(voyage,file)
                date=add_day(date,7)
                voyage.departureFlight.departure=date
                voyage.departureFlight.arrival=add_hour(date,3)




    def LLgettingVoyage(self,input_string):
        voyage=leitaVoyage(input_string)
        #print(voyage.departureFlight.soldTickets)
        return voyage
        #UI.gettingAirplanes(getAircraft)
    def LLupdateStaff(self,input_string):
        employees=staffInfo(4, input_string)
        return employees

    def LLupdatingStaff(self,employee):
        DL.DLupdateStaff(employee)

    def LLupdateDestination(self):
        destination=getDestinations()
        return destination

    def LLupdatingDestination(self,destination):
        DL.DLupdatedDestination(destination)

    def LLupdateAircraft(self,aircraft):
        DL.DLupdateAircraft(aircraft)

    def LLupdateVoyage(self,voyage):
        DL.DLupdateVoyage(voyage)

    def LLleitaVoyage(self,input_string):
        voyage=leitaVoyage(input_string)
        return voyage

    def LLaircraftToVoyage(self,voyage):
        DL.DLaircraftToVoyage(voyage)

    def LLgetFlights(self):
        flights = DL.DLgetFlights()
        return flights

    def LLgettingEmployees(self,input_string):
        employees=staffInfo(4,input_string)
        return employees

    def LLemployeesToVoyage(self,voyage,employee):
        DL.DLemployeesToVoyage(voyage,employee)
