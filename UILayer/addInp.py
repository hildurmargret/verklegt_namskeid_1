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
        self.name=input("Airplane Name: ")
        if self.name=="CANCEL":
            self.cancel=1
            return 0
        self.airplaneModel=input("Airplane model: ")
        if self.airplaneModel=="CANCEL":
            self.cancel=1
            return 0
        self.manufacturer=input("Airplane manufacturer: ")
        if self.name=="CANCEL":
            self.cancel=1
            return 0
        self.seats=input("Number of passenger seats: ")
        if self.seats=="CANCEL":
            self.cancel=1
            return 0
        return self.name,self.airplaneModel,self.manufacturer,self.seats

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
