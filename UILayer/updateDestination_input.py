class updateDestInput():

    def addDestInp(self,destination):
        self.destination=destination.destination
        self.country=destination.country
        self.distance=destination.distance
        self.airport=destination.airport
        self.id=destination.id
        contactName=input("Contact name: ")
        if contactName=="":
            self.contactName=destination.contactName
        else:
            self.contactName=contactName
        contactNumber=input("Contact number: ")
        if contactNumber=="":
            self.contactNumber=destination.contactNumber
        else:
            self.contactNumber=contactNumber
            return self
