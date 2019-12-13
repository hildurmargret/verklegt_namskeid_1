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
from LogicLayer.Date import*

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
    def LLsaveCopiedVoyage(self,voyage,file):
        flights=DL.DLsaveVoyagesInList(voyage)
        destinations=self.LLupdateDestination()
        flights=fixFlNo(flights,destinations)
        DL.DLsaveVoyage(flights,file)

    def LLgetAircraft(self):
        getAircraft = list_all_aircraft()
        return getAircraft

    def LLcopyExistingVoyage(self,voyage,inp,date):
        voyageDate=voyage.departureFlight.departure
        dateNow=now()
        if voyageDate>dateNow:
            file="UpcomingFlights copy3.csv"
        else:
            file="PastFlights copy.csv"
        if inp==1:
            self.LLsaveCopiedVoyage(voyage,file)
        elif inp==2:
            iter=int(input("Number of iterations: "))
            for i in range(iter):
                self.LLsaveCopiedVoyage(voyage,file)
                date=add_day(date,1)
                voyage.departureFlight.departure=date
                voyage.departureFlight.arrival=add_hour(date,3)
                voyage.returnFlight.departure=add_hour(date,4)
                voyage.returnFlight.arrival=add_hour(date,6)
        elif inp==3:
            iter=int(input("Number of iterations: "))
            for i in range(iter):
                self.LLsaveCopiedVoyage(voyage,file)
                date=add_day(date,7)
                voyage.departureFlight.departure=date
                voyage.departureFlight.arrival=add_hour(date,3)
                voyage.returnFlight.departure=add_hour(date,4)
                voyage.returnFlight.arrival=add_hour(date,6)



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

    def LLsaveUpdVoyage(self, voyage):
        DL.DLsaveUpdVoyage(voyage)
