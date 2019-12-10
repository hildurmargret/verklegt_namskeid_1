from ModelClasses.Staff import*
from ModelClasses.Airplane import*
from LogicLayer.Date import*
from DataLayer.getAllPlaneTypes import*
class Inp1():

    def addStaffInp1(self, employee):

        validName_bool = 0
        while not validName_bool:
            if employee.name != '':
                validName_bool = 1
                self.name = employee.name
                print('Name: ' + employee.name)
            else:
                self.name=input("Name: ")

                if self.name=="CANCEL":
                    validName_bool=1
                    self.cancel=1
                    return 0
                elif self.name == '':
                    validName_bool = 1
                    self.name = employee.name
                elif not all(x.isalpha() or x.isspace() for x in self.name):
                    print('Invalid input. Name must consist of letters only [a-z]')
                else:
                    validName_bool=1

        validSSN_bool = 0
        while not validSSN_bool:
            if employee.SSN != '':
                validSSN_bool = 1
                self.SSN = employee.SSN
                print('SSN: ' + employee.SSN)
            else:
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
            elif self.phoneNumber == '':
                validPno_bool = 1
                self.phoneNumber = employee.phoneNumber
            elif not self.phoneNumber.isdigit() or (len(self.phoneNumber) != 7):
                print('Invalid input. Phone number must consist of 7 integers [0-9]')
            else:
                validPno_bool = 1


        # validMno_bool = 0
        # while not validMno_bool:
        #     self.mobileNumber=input("Mobile number: ")
        #     if self.mobileNumber=="CANCEL":
        #         validMno_bool = 1
        #         self.cancel=1
        #         return 0
        #     elif self.mobileNumber == '':
        #         validMno_bool = 1
        #         self.mobileNumber = employee.mobileNumber
        #     elif not self.mobileNumber.isdigit() or (len(self.mobileNumber) != 7):
        #         print('Invalid input. Mobile number must consist of 7 integers [0-9]')
        #     else:
        #         validMno_bool = 1

        validEmail_bool = 0
        while not validEmail_bool:
            self.emailAddress=input("Email address: ")
            if self.emailAddress=="CANCEL":
                validEmail_bool = 1
                self.cancel=1
                return 0
            elif self.emailAddress == '':
                self.emailAddress = employee.emailAddress
                validEmail_bool = 1
            elif not '@' in self.emailAddress:
                print("Invalid input, email address must contain '@' sign")
            else:
                validEmail_bool = 1

        validRole_bool = 0
        while not validRole_bool:
            self.role=input("Role: ")
            if self.role=="CANCEL":
                validRole_bool=1
                self.cancel=1
                return 0
            elif self.role == '':
                validRole_bool = 1
                self.role = employee.role
            elif self.role != 'Pilot' and self.role != 'Cabincrew':
                print("Invalid input. Role must be either 'Pilot' or 'Cabincrew'")
            else:
                validRole_bool = 1

        validRank_bool = 0
        while not validRank_bool:
            self.rank=input("Rank: ")
            if self.rank=="CANCEL":
                validRank_bool = 1
                self.cancel=1
                return 0
            elif self.rank == '':
                validRank_bool = 1
                self.rank = employee.rank
            elif self.role == 'Pilot' and (self.rank != 'Captain' and self.rank != 'Copilot'):
                print("Invalid input. Pilot role must be either 'Captain' or 'Copilot'")
            elif self.role == 'Cabincrew' and (self.rank != 'Flight Attendant' and self.rank != 'Flight Service Manager'):
                print("Invalid input. Cabincrew role must be either 'Flight Attendant' or 'Flight Service Manager'")
            else:
                validRank_bool = 1

        validLicence_bool = 0
        correctType_bool = 0
        types = getAllTypes()
        while not validLicence_bool:
            if self.role == 'Pilot':
                self.licence=input("Licence: ")
                for i in range(len(types)):
                    if types[i] == self.licence:
                        correctType_bool = 1

                if self.licence=="CANCEL":
                    validLicence_bool=1
                    self.cancel=1
                    return 0
                elif self.licence == '':
                    validLicence_bool=1
                    self.licence = employee.licence
                elif not correctType_bool:
                    print('Invalid input. Licence must be one of the types below:')
                    for i in range(len(types)):
                        print(types[i])
                else:
                    validLicence_bool=1
            else:
                validLicence_bool=1
                self.licence = 'N/A'
                print('Licence: ' + self.licence)

        return self
