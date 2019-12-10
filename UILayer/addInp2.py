from ModelClasses.Staff import*
from ModelClasses.Airplane import*
from LogicLayer.Date import*
class Inp2():


    def addAirplaneInp2(self):
        self.planeTypeId=input("Plane type ID: ")
        if self.planeTypeId=="CANCEL":
            self.cancel=1
            return 0
        self.manufacturer=input("Airplane manufacturer: ")
        if self.manufacturer=="CANCEL":
            self.cancel=1
            return 0
        self.airplaneModel=input("Airplane model: ")
        if self.airplaneModel=="CANCEL":
            self.cancel=1
            return 0
        self.capacity=input("Number of passenger seats: ")
        if self.capacity=="CANCEL":
            self.cancel=1
            return 0
        self.emptyWeight=input("Airplane manufacturer: ")
        if self.emptyWeight=="CANCEL":
            self.cancel=1
            return 0
        self.maxTakeoffWeight=input("Airplane model: ")
        if self.maxTakeoffWeight=="CANCEL":
            self.cancel=1
            return 0
        self.unitThrust=input("Number of passenger seats: ")
        if self.unitThrust=="CANCEL":
            self.cancel=1
            return 0
        self.serviceCeiling=input("Airplane manufacturer: ")
        if self.serviceCeiling=="CANCEL":
            self.cancel=1
            return 0
        self.length=input("Airplane model: ")
        if self.length=="CANCEL":
            self.cancel=1
            return 0
        self.height=input("Number of passenger seats: ")
        if self.height=="CANCEL":
            self.cancel=1
            return 0
        self.wingspan=input("Number of passenger seats: ")
        if self.wingspan=="CANCEL":
            self.cancel=1
            return 0
        return self.planeTypeId,self.manufacturer,self.airplaneModel,self.capacity,self.emptyWeight,self.maxTakeoffWeight,self.unitThrust,self.serviceCeiling,self.length,self.height,self.wingspan

    def addDestinationInp(self):
            self.country=input("Country: ")
            if self.country=="CANCEL":
                self.country=1
                return 0
            self.distance=input("Distance: ")
            if self.distance=="CANCEL":
                self.distance=1
                return 0
            self.airport=input("Airport: ")
            if self.airport=="CANCEL":
                self.airport=1
                return 0
            self.contactName=input("Contact name: ")
            if self.contactName=="CANCEL":
                self.contactName=1
                return 0
            self.contactNumber=input("Contact phone number: ")
            if self.contactNumber=="CANCEL":
                self.cancel=1
                return 0
            return self.country, self.distance, self.airport, self.contactName, self.contactNumber


    def addVoyageInp(self):

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

        return self.flightNumber,self.departingFrom,self.arrivingAt,self.departure,self.arrival,self.numberOfCabin,self.numberOfPilots,self.aircraftId
