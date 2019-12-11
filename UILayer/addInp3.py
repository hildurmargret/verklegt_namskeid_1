from ModelClasses.Staff import*
from ModelClasses.Airplane import*
from LogicLayer.Date import*
class Inp3():


    def addVoyageInp(self,voyage):
        departRoute=voyage.departureFlight
        retRoute=voyage.returnFlight
        self.departRoute.flightNumber=input("Flight number: ")
        if self.departRoute.flightNumber=="CANCEL":
            self.departRoute.cancel=1
            return 0
        self.departRoute.departingFrom=input("Departing from: ")
        if self.departRoute.departingFrom=="CANCEL":
            self.departRoute.cancel=1
            return 0
        self.departRoute.arrivingAt=input("Arriving at: ")
        if self.departRoute.arrivingAt=="CANCEL":
            self.departRoute.cancel=1
            return 0
        #self.departureDate=input("Departure date: ")
        date=input("Departure date: ")
        if date=="CANCEL":
            self.departRoute.cancel=1
            return 0
        month=input("Departure month: ")
        if month=="CANCEL":
            self.departRoute.cancel=1
            return 0
        year=input("Departure year: ")
        if year=="CANCEL":
            self.departRoute.cancel=1
            return 0
        hour=input("Departure hour: ")
        if hour=="CANCEL":
            self.departRoute.cancel=1
            return 0
        minute=input("Departure minute: ")
        if minute=="CANCEL":
            self.departRoute.cancel=1
            return 0
        date=int(date)
        month=int(month)
        year=int(year)
        hour=int(hour)
        minute=int(minute)
        self.departRoute.departure = getDate(year,month,date,hour,minute)

        hour=hour+2
        if hour >= 24:
            hour=hour-24
            date=date+1

        self.departRoute.arrival=getDate(year,month,date,hour,minute)

        self.departRoute.aircraftId=input("Aircraft ID: ")
        if self.departRoute.aircraftId=="CANCEL":
            self.departRoute.aircraftId=1
            return 0
        voyage
        return self
