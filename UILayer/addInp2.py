from ModelClasses.Staff import*
from ModelClasses.Airplane import*
from LogicLayer.Date import*
class Inp2():


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