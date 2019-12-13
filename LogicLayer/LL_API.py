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

DL=DL_API()


class LL_API:

    def __init__(self):
        pass

    def LLsaveStaff(self, newStaff):
        DL.DLsaveStaff(newStaff)

    def LLsaveAircraft(self,newAircraft):
        DL.DLsaveAircraft(newAircraft)
    def LLsaveDestination(self,newDest):
        DL. DLsaveDestination(newDest)
    def LLsaveVoyage(self,newVoyage,file):
        [newVoyList,destinations]=DL.DLairportOccupied(newVoyage)#skilar lista af nyrri vinnuferd, skodar einnig hvort flugvollur se i notkun
        newVoyList=fixFlNo(newVoyList,destinations) #uppfaerir flugnumer
        DL.DLsaveVoyage(newVoyList,file)#vistar vinnuferd
    def LLsaveCopiedVoyage(self,voyage,file):
        flights=DL.DLsaveVoyagesInList(voyage) #byr til lista af flugferdum
        destinations=self.LLupdateDestination() #byr til lista af afangastodum
        flights=fixFlNo(flights,destinations) #lagar flugnumer
        DL.DLsaveVoyage(flights,file) #savear vinnuferd

    def LLgetAircraft(self):
        getAircraft = list_all_aircraft() #seakir lista af flugvelum
        return getAircraft

    def LLcopyExistingVoyage(self,voyage,inp,date):
        voyageDate=voyage.departureFlight.departure
        dateNow=now()#skodar hvada skra a ad vista i
        if voyageDate>dateNow:
            file="UpcomingFlights copy3.csv"
        else:
            file="PastFlights copy.csv"
        if inp==1:
            self.LLsaveCopiedVoyage(voyage,file) #vistar vinnuferd i skra
        elif inp==2:
            iter=int(input("Number of iterations: "))
            for i in range(iter): #vistar vinnuferdina jafn oft og bedid er um, haekkar dagsetningu alltaf eftir
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
        employees=staffInfo(4, input_string) #saekir lista af starfsmonnum sem passa vid input_string
        return employees

    def LLupdatingStaff(self,employee):
        DL.DLupdateStaff(employee)

    def LLupdateDestination(self):
        destination=getDestinations() #saekir alla afangastadi
        return destination

    def LLupdatingDestination(self,destination):
        DL.DLupdatedDestination(destination)

    def LLupdateAircraft(self,aircraft):
        DL.DLupdateAircraft(aircraft)

    def LLupdateVoyage(self,voyage):
        DL.DLupdateVoyage(voyage)

    def LLleitaVoyage(self,input_string):
        voyage=leitaVoyage(input_string) #saekir lista af vinnuferdum sem passa vid input_string
        return voyage

    def LLaircraftToVoyage(self,voyage):
        DL.DLaircraftToVoyage(voyage)

    def LLgetFlights(self):
        flights = DL.DLgetFlights() #saekir lista af ollum flugum
        return flights

    def LLgettingEmployees(self,input_string):
        employees=staffInfo(4,input_string) #saekir lista af starfsmonnum sem passa vid input_string
        return employees

    def LLemployeesToVoyage(self,voyage,employee):
        DL.DLemployeesToVoyage(voyage,employee)

    def LLsaveUpdVoyage(self, voyage):
        DL.DLsaveUpdVoyage(voyage)
