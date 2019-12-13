from LogicLayer.LL_API import*
from UILayer.printAirplanes import*
from UILayer.chooseEmplFromList import*
from UILayer.updateDestination_input import*
from UILayer.addInp1 import*
from UILayer.addInp2 import*
from UILayer.addInp3 import*
from UILayer.addInp4 import*
from UILayer.addInp5 import*
from UILayer.chooseDestinationFromList import*
from LogicLayer.leitaVoyage import*
from UILayer.checkFlightNumberInp import*

LL=LL_API()

class UI_Manager:

    def __init__(self):
        pass

    def UIsaveStaff(self,newStaff):
        LL.LLsaveStaff(newStaff)
#Flug sott og vistud i flights
    def UIgetFlights(self):
        flights = LL.LLgetFlights()
        return flights

    def UIsaveVoyage(self,newVoyage):
        voyageDate=newVoyage.departureFlight.departure
        dateNow=now()#Skoda hvor skranna a ad savea i
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
#Saekir aircraft og skilar lista af aircraft
    def UIgettingAirplanes(self):
        getAircraft = LL.LLgetAircraft()
        return getAircraft

    def UIgettingVoyage(self,input_string):
        voyage=LL.LLleitaVoyage(input_string)#leitar af voyage,faer lista af vinnuferdum sem passa vid input
        voyage=chooseVoyage(voyage)#prentar ut lista af vinnuferdunum og leatur notenda velja eina
        return voyage

    def UIupdateStaff(self):
        update=Inp1()

        valid_input = 0
        while not valid_input:
            input_string=input("SSN: ")
            if input_string == 'CANCEL': #fer til baka ef slegid er inn CANCEL
                return 0
            else:
                employees=LL.LLupdateStaff(input_string)#saekir lista af starfsmonnum sem passa vid input_string
                employee=emplFromList(employees)#prentar ut lista af starfsmonnum, laetur notenda velja einn akvedinn starfsmann

                if employee != 0:
                    valid_input = 1
                employee=update.addStaffInp1(employee)

                if employee == 0:
                    return 0
                else:
                    LL.LLupdatingStaff(employee)
                    return 1

    def UIsaveUpdVoyage(self,voyage):
        LL.LLsaveUpdVoyage(voyage)
#saekir lista af ollum afangastodum
    def UIupdateDestination(self):
        #update=updateDestInput()
        dest=LL.LLupdateDestination()
        return dest
#vistar updated afangastadi
    def UIsaveNewDestination(self,destination):
        LL.LLupdatingDestination(destination)


    def UIupdateVoyage(self):
        update=Inp5()
        flightNumber = checkFlightNumberInp() #Skodar hvort flugnumer er til
        if flightNumber == 0:
            return 0
        else:
            voyage=self.UIgettingVoyage(flightNumber)#saekir lista af vinnuferdum, prentar ut thann lista og laetur notenda velja eina vinnuferd sem hann vill updatea
            [voyage.departureFlight,tick]=update.addUpdRouteInp(voyage.departureFlight)#tekur input fra notenda um breytingar
            voyage.returnFlight.soldTickets=tick

            LL.LLupdateVoyage(voyage) #vistar vinnuferd a ny
            return 1


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
            #Flug tilbaka er buid til utfra upplysingum um flug ut
            returnFlight.flightNumber=departureFlight.flightNumber
            returnFlight.departingFrom = departureFlight.arrivingAt
            returnFlight.arrivingAt = departureFlight.departingFrom
            returnFlight.departure = add_hour(departureFlight.arrival,1)
            returnFlight.aircraftId=departureFlight.aircraftId
            returnFlight.soldTickets=soldTick
            depFlArr=int(getHour(departureFlight.arrival))
            returnFlight.arrival = add_hour(returnFlight.departure,2)
            voyage=createVoyage(departureFlight,returnFlight)
            UI.UIsaveVoyage(voyage) #vistar vinnuferd

    def UIemployeesToVoyage(self,voyage,employee):#Starfsmenn vistadir i skra
        LL.LLemployeesToVoyage(voyage,employee)

    def UIgetEmployees(self, input_string): #sottur listi af starfsmonnum sem passa vid input
        employees = LL.LLgettingEmployees(input_string)
        return employees

    def UIaircraftToVoyage(self,voyage): #flugferd vistud i vinnuferd
        LL.LLaircraftToVoyage(voyage)
