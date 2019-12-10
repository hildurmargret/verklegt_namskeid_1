class updateDestInput():

    def addDestInp(self,destination):
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
