from ModelClasses.Staff import*
from ModelClasses.Airplane import*
from LogicLayer.Date import*
class Inp2():

    def addDestinationInp(self,destination):

        if destination.id != '':
            self.id = destination.id
        else:
            validID_bool = 0
            while not validID_bool:
                self.id=input("ID: ")
                if self.id=="CANCEL":
                    validID_bool=1
                    self.cancel=1
                    return 0
                elif self.id == '':
                    print('Please enter destination ID')
                elif not self.id.isalpha() or len(self.id)!=3:
                    print('Invalid input. ID must consist of three letters [a-z]')
                else:
                    self.id = self.id.upper()
                    validID_bool = 1

            if destination.destination != '':
                self.destination = destination.destination
                print('Destination: ' + self.destination)
            else:
                validDest_bool = 0
                while not validDest_bool:
                    self.destination=input("Destination: ")
                    if self.destination=="CANCEL":
                        validDest_bool=1
                        self.cancel=1
                        return 0
                    elif self.destination == '':
                        print('Please enter destination')
                    elif not all(x.isalpha() or x.isspace() for x in self.destination):
                        print('Invalid input. Destination must consist of letters only [a-z]')
                    else:
                        self.destination = self.destination.title()
                        validDest_bool=1

            if destination.country != '':
                self.country = destination.country
                print('Country: ' + self.country)
            else:
                validCountry_bool=0
                while not validCountry_bool:
                    self.country=input("Country: ")
                    if self.country=="CANCEL":
                        validCountry_bool = 1
                        self.cancel=1
                        return 0
                    elif self.country == '':
                        print('Please enter destination country')
                    elif not all(x.isalpha() or x.isspace() for x in self.destination):
                        print('Invalid input. Country must consist of letters only [a-z]')
                    else:
                        self.country = self.country.title()
                        validCountry_bool=1

            if destination.distance != '':
                self.distance = destination.distance
                print('Distance: ' + self.distance)
            else:
                validDistance_bool=0
                while not validDistance_bool:
                    self.distance=input("Distance [km]: ")
                    if self.distance=="CANCEL":
                        validDistance_bool = 1
                        self.cancel=1
                        return 0
                    elif self.distance == '':
                        validDistance_bool = 1
                    elif not self.distance.isdigit():
                        print('Invalid input. Distance must consist of integers only [0-9]')
                    elif int(self.distance) <= 0:
                        print('Invalid input. Distance must be greater than zero')
                    else:
                        validDistance_bool = 1

            validConName_bool=0
            while not validConName_bool:
                self.contactName=input("Contact name: ")
                if self.contactName=="CANCEL":
                    validConName_bool=1
                    self.cancel=1
                    return 0
                elif self.contactName == '':
                    self.contactName = destination.contactName
                    print('Contact name: ' + self.contactName)
                    validConName_bool=1
                elif not all(x.isalpha() or x.isspace() for x in self.destination):
                    print('Invalid input. Contact name must consist of letters only [a-z]')
                else:
                    self.contactName = self.contactName.title()
                    validConName_bool=1

            validConNum_bool=0
            while not validConNum_bool:
                self.contactNumber=input("Contact phone number: ")
                if self.contactNumber=="CANCEL":
                    validConNum_bool=1
                    self.cancel=1
                    return 0
                elif self.contactNumber == '':
                    self.contactNumber = destination.contactNumber
                    print('Contact number: ' + self.contactNumber)
                    validConNum_bool=1
                elif not self.contactNumber.isdigit() or (len(self.contactNumber) != 7):
                    print('Invalid input. Phone number must consist of 7 integers [0-9]')
                else:
                    validConNum_bool=1

            return self
