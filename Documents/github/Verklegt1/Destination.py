class Destination:

    def __init__(self):
        self.country=""
        self.distance=0
        self.airport=""
        self.contactName=""
        self.contactNumber=0

    def addInfo(self):
        self.country=input("Country: ")
        self.distance=input("Distance: ")
        self.airport=input("Airport: ")
        self.contactName=input("Contact name: ")
        self.contactNumber=input("Contact number: ")
