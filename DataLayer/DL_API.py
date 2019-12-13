from DataLayer.saveStaffInFile import*
from DataLayer.saveAircraftInFile import*
from DataLayer.saveNewDestination import*
from DataLayer.saveUpdatedStaff import*
from DataLayer.saveUpdatedDestination import*
from DataLayer.saveEmployeesToVoyage import*
from DataLayer.airportOccupied import*
from DataLayer.getDestinations import*
from DataLayer.saveUpdatedFlights import*
from DataLayer.saveAircraftToVoyage import*
from DataLayer.read_pastFlights import*
from DataLayer.saveVoyInList import*
from DataLayer.saveUpdVoyage import*
from DataLayer.saveUpVoy import*
from DataLayer.saveUpdatedFlights import*

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
    def DLairportOccupied(self,newVoyage):
        newVoyList=airportOccupied(newVoyage)
        destinations = getDestinations()
        return newVoyList,destinations
    def DLsaveVoyage(self,newVoyage,file):
        updateFlights(newVoyage,file)
    def DLupdateStaff(self,employee):
        saveUpdatedStaff(employee)
    def DLupdatedDestination(self, destination):
        saveUpdatedDest(destination)
    def DLupdateAircraft(self,aircraft):
        saveUpdatedAircraft(aircraft)
    def DLupdateVoyage(self,voyage):
        #VALDIS
        flights=self.DLsaveVoy(voyage)
        ###saveUpdatedVoyage(voyage)
        #file="UpcomingFlights copy3.csv"
        #updateFlights(voyage,file)
    def DLaircraftToVoyage(self,voyage):
        flights=aircraftToVoyage(voyage)
        voyageDate=voyage.departureFlight.departure
        dateNow=now()
        if voyageDate>dateNow:
            file="UpcomingFlights copy3.csv"
        else:
            file="PastFlights copy.csv"
        updateFlights(flights,file)

    def DLemployeesToVoyage(self,voyage,employee):
        employeesToVoyage(voyage,employee)

    def DLgetFlights(self):
        flights = read_pastFlights('UpcomingFlights copy3.csv')
        flights.extend(read_pastFlights('PastFlights copy.csv'))
        return flights

    def DLsaveVoyagesInList(self,voyage):
        flights=saveUpdatedVoyage(voyage)
        # for i in range(len(flights)):
        #     print(flights[i].soldTickets)
        return flights

    def DLsaveVoy(self,voyage):
        flights=saveUpVoy(voyage)
        return flights


    def DLsaveUpdVoyage(self, voyage):
        saveUpdVoyage(voyage)
