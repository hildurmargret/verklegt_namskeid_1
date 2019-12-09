from ModelClasses.Staff import*
from ModelClasses.Airplane import*
class Inp():

    def addStaffInp(self):
        self.name=input("Name: ")
        if self.name=="CANCEL":
            self.cancel=1
            return 0
        self.SSN=input("SSN: ")
        if self.SSN=="CANCEL":
            self.cancel=1
            return 0
        self.address=input("Address: ")
        if self.address=="CANCEL":
            self.cancel=1
            return 0
        self.phoneNumber=input("Phone number: ")
        if self.phoneNumber=="CANCEL":
            self.cancel=1
            return 0
        self.mobileNumber=input("Mobile number: ")
        if self.mobileNumber=="CANCEL":
            self.cancel=1
            return 0
        self.emailAddress=input("Email address: ")
        if self.emailAddress=="CANCEL":
            self.cancel=1
            return 0
        self.rank=input("Rank: ")
        if self.rank=="CANCEL":
            self.cancel=1
            return 0
        return self.name,self.SSN,self.address,self.phoneNumber,self.mobileNumber,self.emailAddress,self.rank


    def addAirplaneInp(self):
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
            self.contactNumber=input("Contact phone number: ")
            if self.contactNumber=="CANCEL":
                self.cancel=1
                return 0
            return self.country, self.distance, self.airport, self.contactName, self.contactNumber


    def addVoyageInp(self):

        # if self.numberOfPilots < 2:
        #     print("Sorry! There must be at least 2 pilots in every voyage. Try again")
        #     self.numberOfPilots = input("Number of Pilots: ")
        #
        # if self.numberOfCabin < 1:
        #     print("Sorry! There must be at least 1 cabin in every voyage. Try again")
        #     self.numberOfCabin = input("Number of cabin: ")

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
        self.departure=input("Departure: ")
        if self.departure=="CANCEL":
            self.cancel=1
            return 0
        self.arrival=input("Arrival: ")
        if self.arrival=="CANCEL":
            self.country=1
            return 0
        self.aircraftId=input("Airport: ")
        if self.aircraftId=="CANCEL":
            self.aircraftId=1
            return 0
        self.numberOfCabin=input("Distance: ")
        if self.numberOfCabin=="CANCEL":
            self.distance=1
            return 0
        self.numberOfPilots=input("Airport: ")
        if self.numberOfPilots=="CANCEL":
            self.airport=1
            return 0

        return self.flightNumber,self.departingFrom,self.arrivingAt,self.departure,self.arrival,self.numberOfCabin,self.numberOfPilots,self.aircraftId
