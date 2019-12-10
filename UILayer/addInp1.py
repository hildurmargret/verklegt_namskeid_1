from ModelClasses.Staff import*
from ModelClasses.Airplane import*
from LogicLayer.Date import*
class Inp():

    def addStaffInp(self):
        validName_bool = 0
        while not validName_bool:
            self.name=input("Name: ")
            if self.name=="CANCEL":
                validName_bool=1
                self.cancel=1
                return 0
            elif not self.name.isalpha():
                print('Invalid input. Name must consist of letters only [a-z]')
            else:
                validName_bool=1

        validSSN_bool = 0
        while not validSSN_bool:
            self.SSN=input("SSN: ")
            if self.SSN=="CANCEL":
                validSSN_bool = 1
                self.cancel=1
                return 0
            elif not self.SSN.isdigit() or (len(self.SSN) != 10):
                print('Invalid input. SSN must consist of 10 integers [0-9]')
            else:
                validSSN_bool = 1


        self.address=input("Address: ")
        if self.address=="CANCEL":
            self.cancel=1
            return 0

        validPno_bool = 0
        while not validPno_bool:
            self.phoneNumber=input("Phone number: ")
            if self.phoneNumber=="CANCEL":
                validPno_bool = 1
                self.cancel=1
                return 0
            elif not self.phoneNumber.isdigit() or (len(self.phoneNumber) != 7):
                print('Invalid input. Phone number must consist of 7 integers [0-9]')
            else:
                validPno_bool = 1


        validMno_bool = 0
        while not validMno_bool:
            self.mobileNumber=input("Mobile number: ")
            if self.mobileNumber=="CANCEL":
                validMno_bool = 1
                self.cancel=1
                return 0
            elif not self.mobileNumber.isdigit() or (len(self.mobileNumber) != 7):
                print('Invalid input. Mobile number must consist of 7 integers [0-9]')
            else:
                validMno_bool = 1

        validEmail_bool = 0
        while not validEmail_bool:
            self.emailAddress=input("Email address: ")
            if self.emailAddress=="CANCEL":
                validEmail_bool = 1
                self.cancel=1
                return 0
            elif not '@' in self.emailAddress:
                print("Invalid input, email address must contain '@' sign")
            else:
                validEmail_bool = 1

        self.rank=input("Rank: ")
        if self.rank=="CANCEL":
            self.cancel=1
            return 0
        return self.name,self.SSN,self.address,self.phoneNumber,self.mobileNumber,self.emailAddress,self.rank
