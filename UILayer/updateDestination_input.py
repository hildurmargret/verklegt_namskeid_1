class updateDestInput():

    #Fall til að uppfæra destination

    def addDestInp(self,destination):
        self.destination=destination.destination
        self.country=destination.country
        self.distance=destination.distance
        self.id=destination.id

        validCountry_bool=0
        while not validCountry_bool:
            country=input("Country: ")
            if country == 'CANCEL':
                validCountry_bool=1
                return 0
            elif country=="":
                self.country=destination.country
                validCountry_bool=1
            elif not all(x.isalpha() or x.isspace() for x in country):
                print('Invalid input. Name must consist only of letters [a-z]')
            else:
                validCountry_bool=1
                self.country=country.title()

        validDist_bool=0
        while not validDist_bool:
            dist=input("Distance [km]: ")
            if dist == 'CANCEL':
                validDist_bool=1
                return 0
            elif dist=="":
                self.distance=destination.distance
                validDist_bool=1
            elif not dist.isdigit():
                print('Invalid input. Contact number must consist of 7 integers [0-9]')
            else:
                self.distance=dist
                validDist_bool=1

        validName_bool=0
        while not validName_bool:
            contactName=input("Contact name: ")
            if contactName == 'CANCEL':
                validName_bool=1
                return 0
            elif contactName=="":
                self.contactName=destination.contactName
                validName_bool=1
            elif not all(x.isalpha() or x.isspace() for x in contactName):
                print('Invalid input. Name must consist only of letters [a-z]')
            else:
                validName_bool=1
                self.contactName=contactName.title()

        validNumber_bool=0
        while not validNumber_bool:
            contactNumber=input("Contact number: ")
            if contactNumber == 'CANCEL':
                validNumber_bool=1
                return 0
            elif contactNumber=="":
                self.contactNumber=destination.contactNumber
                validNumber_bool=1
            elif not contactNumber.isdigit():
                print('Invalid input. Contact number must consist of integers only [0-9]')
            else:
                self.contactNumber=contactNumber
                validNumber_bool=1

        return self
