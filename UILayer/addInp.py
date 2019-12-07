from ModelClasses.Staff import*
class Inp():

    def addInp(self):
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
