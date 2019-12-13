from LogicLayer.LL_API import*
from UILayer.printAirplanes import*
from UILayer.updateStaff_Input import*
from UILayer.chooseEmplFromList import*
from UILayer.updateDestination_input import*
from UILayer.addInp1 import*
from UILayer.addInp3 import*
from UILayer.addInp5 import*
from UILayer.chooseDestinationFromList import*
from LogicLayer.leitaVoyage import*

LL=LL_API()

class UI_Manager:

    def __init__(self):
        pass

    def UIsaveStaff(self,newStaff):
        LL.LLsaveStaff(newStaff)

    def UIgetFlights(self):
        flights = LL.LLgetFlights()
        return flights

    def UIsaveVoyage(self,newVoyage):
        voyageDate=newVoyage.departureFlight.departure
        dateNow=now()
        if voyageDate>dateNow:
            file="UpcomingFlights copy3.csv"
        else:
            file="PastFlights copy.csv"
        LL.LLsaveVoyage(newVoyage,file)


    def UIcopyExistingVoyage(self,voyage,inp,date):
        LL.LLcopyExistingVoyage(voyage,inp,date)
        LL.LLupdateVoyage(voyage)

    def UIsaveAircraft(self,newAircraft):
        LL.LLsaveAircraft(newAircraft)

    def UIsaveDestinationInFile(self, NewDest):
        LL.LLsaveDestination(NewDest)

    def UIgettingAirplanes(self):
        getAircraft = LL.LLgetAircraft()
        return getAircraft

    def UIgettingVoyage(self,input_string):
        voyage=LL.LLleitaVoyage(input_string)
        voyage=chooseVoyage(voyage)
        return voyage

    def UIupdateStaff(self):
        update=Inp1()
        input_string=input("SSN: ")
        employees=LL.LLupdateStaff(input_string)
        employee=pilotsFromList(employees)
        employee=update.addStaffInp1(employee)
        LL.LLupdatingStaff(employee)

    def UIsaveUpdVoyage(self,voyage):
        LL.LLsaveUpdVoyage(voyage)


    # def UIupdateCabin(self):
    #     update=updateStaffInput()
    #     input_string=input("SSN: ")
    #     employees=LL.LLupdateStaff(input_string)
    #     employee=cabinFromList(employees)
    #     employee=update.addStaffInp(employee)
    #     LL.LLupdatingStaff(employee)

    def UIupdateDestination(self):
        #update=updateDestInput()
        dest=LL.LLupdateDestination()
        return dest

    def UIsaveNewDestination(self,destination):
        LL.LLupdatingDestination(destination)

    def UIupdateAircraft(self):
        update=Inp4()
        aircrafts=self.UIgettingAirplanes()
        aircraft=aircraftFromList(aircrafts)
        aircraft=update.addAirplaneInp(aircraft)
        LL.LLupdateAircraft(aircraft)

    def UIupdateVoyage(self):
        update=Inp5()
        input_string = input('Departing flight number: ')
        voyage=self.UIgettingVoyage(input_string)
        [voyage.departureFlight,tick]=update.addRouteInp(voyage.departureFlight)
        voyage.returnFlight.soldTickets=tick



        #voyage.departureFlight=update.addRouteInp(voyage)
        #voyage=update.addVoyageInp(voyage)
        #print(voyage)
        #print(tick)
        LL.LLupdateVoyage(voyage)


    def createNewVoyage(self,print_):
        print_.window7()
        add=Inp3()
        departureFlight=createFlightRoute()
        [departureFlight,soldTick]=add.addRouteInp(departureFlight)
        if departureFlight == 0:
            self.createVoyages(print_)
        else:
            returnFlight = createFlightRoute()
            departureFlight.departingFrom="KEF"
            returnFlight.flightNumber=departureFlight.flightNumber
            returnFlight.departingFrom = departureFlight.arrivingAt
            returnFlight.arrivingAt = departureFlight.departingFrom
            returnFlight.departure = add_hour(departureFlight.arrival,1)
            returnFlight.aircraftId=departureFlight.aircraftId
            returnFlight.soldTickets=soldTick
            depFlArr=int(getHour(departureFlight.arrival))
            # depFlDep=int(getHour(departureFlight.departure))
            # flyingTime=depFlArr-depFlDep
            returnFlight.arrival = add_hour(returnFlight.departure,2)
            voyage=createVoyage(departureFlight,returnFlight)
            UI.UIsaveVoyage(voyage)

    def UIemployeesToVoyage(self,voyage,employee):
    #    print(voyage.departureFlight.aircraftId)
    #    print(voyage.returnFlight.aircraftId)
        LL.LLemployeesToVoyage(voyage,employee)

    def UIgetEmployees(self, input_string):
        employees = LL.LLgettingEmployees(input_string)
        return employees

    # def UIaircraftToVoyage(self):
    #     input_string=input("Flight number: ")
    #     voyages=LL.LLleitaVoyage(input_string)
    #     voyage=chooseVoyage(voyages)
    #     aircraftID=input("AircraftId: ")
    #     LL.LLaircraftToVoyage(voyage)


    def UIaircraftToVoyage(self,voyage):
        LL.LLaircraftToVoyage(voyage)
