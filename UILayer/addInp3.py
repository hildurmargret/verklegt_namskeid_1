from ModelClasses.Staff import*
from ModelClasses.Airplane import*
from LogicLayer.Date import*
class Inp3():


    def addVoyageInp(self,voyage):

        self.flightNumber=input("Flight number: ")
        if self.flightNumber=="CANCEL":
            self.cancel=1
            return 0
        self.departingFrom=input("Departing from: ")
        if self.departingFrom=="CANCEL":
            self.cancel=1
            return 0
        self.arrivingAt=input("Arriving at: ")
        if self.arrivingAt=="CANCEL":
            self.cancel=1
            return 0
        #self.departureDate=input("Departure date: ")
        date=input("Departure date: ")
        if date=="CANCEL":
            self.cancel=1
            return 0
        month=input("Departure month: ")
        if month=="CANCEL":
            self.cancel=1
            return 0
        year=input("Departure year: ")
        if year=="CANCEL":
            self.cancel=1
            return 0
        hour=input("Departure hour: ")
        if hour=="CANCEL":
            self.cancel=1
            return 0
        minute=input("Departure minute: ")
        if minute=="CANCEL":
            self.cancel=1
            return 0
        date=int(date)
        month=int(month)
        year=int(year)
        hour=int(hour)
        minute=int(minute)
        self.departure = getDate(year,month,date,hour,minute)

        hour=hour+2
        if hour >= 24:
            hour=hour-24
            date=date+1

        self.arrival=getDate(year,month,date,hour,minute)

        self.aircraftId=input("Aircraft ID: ")
        if self.aircraftId=="CANCEL":
            self.aircraftId=1
            return 0
        self.numberOfCabin=input("Number of cabin: ")
        if self.numberOfCabin=="CANCEL":
            self.distance=1
            return 0
        self.numberOfPilots=input("Number of pilots: ")
        if self.numberOfPilots=="CANCEL":
            self.airport=1
            return 0

        return self
