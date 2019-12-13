from ModelClasses.Staff import*
from ModelClasses.Airplane import*
from LogicLayer.Date import*
from DataLayer.getAllPlaneTypes import*
from ModelClasses.Staff import*
from DataLayer.getDestinations import*
from DataLayer.getAircraft import*
from UILayer.UI_Manager import*
from ModelClasses.flightRoute import*

class Inp():

    def addStaffInp(self, employee):

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
                    return 0
                elif self.name == '':
                    print("Please enter employee's name")
                elif not all(x.isalpha() or x.isspace() for x in self.name):
                    print('Invalid input. Name must consist of letters only [a-z]')
                else:
                    self.name = self.name.title()
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
                    return 0
                elif self.SSN == '':
                    print("Please enter employee's SSN")
                elif not self.SSN.isdigit() or (len(self.SSN) != 10):
                    print('Invalid input. SSN must consist of 10 integers [0-9]')
                else:
                    validSSN_bool = 1

        self.address=input("Address: ")
        if self.address=="CANCEL":
            return 0
        elif self.address == '' and employee.address != '':
            self.address = employee.address
        elif self.address == '' and employee.address == '':
            print("Please enter employee's address")
        else:
            self.address = self.address.capitalize()

        validPno_bool = 0
        while not validPno_bool:
            self.phoneNumber=input("Phone number: ")
            if self.phoneNumber=="CANCEL":
                validPno_bool = 1
                return 0
            elif self.phoneNumber == '' and employee.phoneNumber != '':
                validPno_bool = 1
                self.phoneNumber = employee.phoneNumber
            elif self.phoneNumber == '' and employee.phoneNumber == '':
                print("Please enter employee's phone number")
            elif not self.phoneNumber.isdigit() or (len(self.phoneNumber) != 7):
                print('Invalid input. Phone number must consist of 7 integers [0-9]')
            else:
                validPno_bool = 1

        validEmail_bool = 0
        while not validEmail_bool:
            self.emailAddress=input("Email address: ")
            if self.emailAddress=="CANCEL":
                validEmail_bool = 1
                return 0
            elif self.emailAddress == '' and employee.emailAddress != '':
                self.emailAddress = employee.emailAddress
                validEmail_bool = 1
            elif self.emailAddress == '' and employee.emailAddress == '':
                print("Please enter employee's email address")
            elif not '@' in self.emailAddress:
                print("Invalid input, email address must contain '@' sign")
            else:
                validEmail_bool = 1

        validRole_bool = 0
        while not validRole_bool:
            self.role=input("Role: ")
            if self.role=="CANCEL":
                validRole_bool=1
                return 0
            elif self.role == '' and employee.role != '':
                validRole_bool = 1
                self.role = employee.role
            elif self.role == '' and employee.role == '':
                print("Please enter employee's role")
            elif self.role != 'Pilot' and self.role != 'Cabincrew':
                print("Invalid input. Role must be either 'Pilot' or 'Cabincrew'")
            else:
                validRole_bool = 1

        validRank_bool = 0
        while not validRank_bool:
            self.rank=input("Rank: ")
            if self.rank=="CANCEL":
                validRank_bool = 1
                return 0
            elif self.rank == '' and employee.rank != '':
                validRank_bool = 1
                self.rank = employee.rank
            elif self.rank == '' and employee.rank == '':
                print("Please enter employee's rank")
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
                    return 0
                elif self.licence == '' and employee.licence != '':
                    validLicence_bool=1
                    self.licence = employee.licence
                elif self.licence == '' and employee.licence == '':
                    print("Please enter employee's airplane licence")
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


    def addDestinationInp(self,destination):

        if destination.id != '':
            self.id = destination.id
        else:
            validID_bool = 0
            while not validID_bool:
                self.id=input("ID: ")
                if self.id=="CANCEL":
                    validID_bool=1
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
                    return 0
                elif self.contactNumber == '':
                    self.contactNumber = destination.contactNumber
                    print('Contact number: ' + self.contactNumber)
                    validConNum_bool=1
                elif not self.contactNumber.isdigit():
                    print('Invalid input. Phone number must consist of integers only [0-9]')
                else:
                    validConNum_bool=1

            return self


    def addRouteInp(self,voyage):
        destinations = getDestinations()
        aircraft = list_all_aircraft()
        self.flightNumber = voyage.flightNumber
        self.captain=voyage.captain
        self.copilot=voyage.copilot
        self.fsm=voyage.fsm
        self.fa1=voyage.fa1
        self.fa2=voyage.fa2

        validDest_bool = 0
        correctDest_bool=0
        while not validDest_bool:
            self.arrivingAt=input("Destination: ")
            for dest in destinations:
                if self.arrivingAt == dest.id and dest.id != 'KEF':
                    correctDest_bool=1
            if self.arrivingAt=="CANCEL":
                validDest_bool = 1
                return 0
            elif not correctDest_bool:
                print('Invalid input. Destination must be one of the following:')
                for dest in destinations:
                    if dest.id != 'KEF':
                        print(dest.id)
            else:
                validDest_bool = 1

        validDate_bool = 0
        while not validDate_bool:
            date=input("Departure day [dd]: ")
            if date=="CANCEL":
                validDate_bool=1
                return 0
            elif not date.isdigit() or (len(date) != 2):
                print('Invalid input. Departure day must consist of two integers [0-9]')
            elif int(date)<1 or int(date)>31:
                print('Invalid input. Departure day must be in the range 1-31')
            else:
                validDate_bool=1

        validMonth_bool=0
        while not validMonth_bool:
            month=input("Departure month [mm]: ")
            if month=="CANCEL":
                validMonth_bool=1
                return 0
            elif not month.isdigit() or (len(month) != 2):
                print('Invalid input. Departure month must consist of two integers [0-9]')
            elif int(month)<1 or int(month)>12:
                print('Invalid input. Departure month must be in the range 1-12')
            else:
                validMonth_bool=1

        validYear_bool=0
        while not validYear_bool:
            year=input("Departure year [yyyy]: ")
            if year=="CANCEL":
                validYear_bool=1
                return 0
            elif not year.isdigit() or (len(year) != 4):
                print('Invalid input. Departure year must consist of four integers [0-9]')
            elif int(year)<2000 or int(year)>2050:
                print('Invalid input. Departure year must be in the range 2000-2050')
            else:
                validYear_bool=1

        validHour_bool = 0
        while not validHour_bool:
            hour=input("Departure hour [hh]: ")
            if hour=="CANCEL":
                validHour_bool = 1
                return 0
            elif not hour.isdigit() or (len(hour) != 2):
                print('Invalid input. Departure hour must consist of two integers [0-9]')
            elif int(hour)<0 or int(hour)>23:
                print('Invalid input. Departure hour must be in the range 0-23')
            else:
                validHour_bool=1

        validMin_bool = 0
        while not validMin_bool:
            minute=input("Departure minute [mm]: ")
            if minute=="CANCEL":
                validMin_bool = 1
                return 0
            elif not minute.isdigit() or (len(minute) != 2):
                print('Invalid input. Departure minute must consist of two integers [0-9]')
            elif int(minute)<0 or int(minute)>59:
                print('Invalid input. Departure minute must be in the range 0-59')
            else:
                validMin_bool=1

        date=int(date)
        month=int(month)
        year=int(year)
        hour=int(hour)
        minute=int(minute)

        self.departure = getDate(year,month,date,hour,minute)
        self.arrival=add_hour(self.departure,2)

        validAirID_bool = 0
        correctAirID_bool=0
        while not validAirID_bool:
            self.aircraftId=input("Aircraft ID: ")
            for plane in aircraft:
                if self.aircraftId == plane.planeInsignia:
                    correctAirID_bool=1
            if self.aircraftId=="CANCEL":
                validAirID_bool=1
                return 0
            elif not correctAirID_bool:
                print('Invalid input. Aircraft ID must be one of the following:')
                for plane in aircraft:
                    print(plane.planeInsignia)
            else:
                validAirID_bool = 1

        for plane in aircraft:
            if plane.planeInsignia == self.aircraftId:
                capacity = plane.capacity

        validSold_bool=0
        while not validSold_bool:
            self.soldTickets=input("Amount of sold seats outbound: ")
            if self.soldTickets=="CANCEL":
                validSold_bool=1
                return 0
            elif int(self.soldTickets) > int(capacity):
                print('Invalid input. Amount of sold seats exceeds plane capacity')
                print('Airplane capacity: ' + capacity)
            elif int(self.soldTickets) < 0 or self.soldTickets=='':
                print('Please enter an amount in the range 0-' + capacity)
            elif not self.soldTickets.isdigit():
                print('Invalid input. Amount must consist of integers only [0-9]')
            else:
                validSold_bool=1

        validSold2_bool=0
        while not validSold2_bool:
            outTick=input("Amount of sold seats homebound: ")
            if outTick=="CANCEL":
                validSold2_bool=1
                return 0
            elif int(outTick) > int(capacity):
                print('Invalid input. Amount of sold seats exceeds plane capacity')
                print('Airplane capacity: ' + capacity)
            elif int(outTick) < 0 or outTick=='':
                print('Please enter an amount in the range 0-' + capacity)
            elif not outTick.isdigit():
                print('Invalid input. Amount must consist of integers only [0-9]')
            else:
                validSold2_bool=1

        return self,outTick


    def addAirplaneInp(self,airplane):
        UI = UI_Manager()
        aircraft = UI.UIgettingAirplanes()

        validInsig_bool = 0
        while not validInsig_bool:
            self.planeInsignia=input("Plane insignia: ")
            if self.planeInsignia == 'CANCEL':
                validInsig_bool=1
                return 0
            elif not self.planeInsignia[3:6].isalpha() or (self.planeInsignia[0:3] != 'TF-' and self.planeInsignia[0:3] != 'tf-') or len(self.planeInsignia) != 6:
                print("Invalid input. Plane insignia must be on the format 'TF-XXX'")
                print("where XXX represents three letters [a-z]")
            else:
                self.planeInsignia = self.planeInsignia.upper()
                validInsig_bool=1

        typeIDMatch_bool = 0

        while not typeIDMatch_bool:

            validTypeID_bool = 0
            while not validTypeID_bool:
                self.planeTypeId=input("Plane type ID: ")
                if self.planeTypeId == 'CANCEL':
                    return 0
                elif self.planeTypeId=="":
                    print('Please enter plane type ID')
                elif self.planeTypeId[0:2] != 'NA' or len(self.planeTypeId)<=2:
                    print('Invalid input. Plane type ID must start with NA followed by manufacturer and model')
                else:
                    validTypeID_bool=1

            alreadyExists_bool = 0

            for plane in aircraft:
                if plane.planeTypeId == self.planeTypeId:
                    print('Airplane information is already in the system.')
                    alreadyExists_bool = 1
                    self.manufacturer = plane.manufacturer
                    self.airplaneModel = plane.airplaneModel
                    self.capacity = plane.capacity
                    self.emptyWeight = plane.emptyWeight
                    self.maxTakeoffWeight = plane.maxTakeoffWeight
                    self.unitThrust = plane.unitThrust
                    self.serviceCeiling = plane.serviceCeiling
                    self.length = plane.length
                    self.height = plane.height
                    self.wingspan = plane.wingspan
                    break

            if alreadyExists_bool:
                return self
            else:
                print('Airplane information is not in the system.')
                print('Please fill out the remaining information')

                validMan_bool = 0
                while not validMan_bool:
                    self.manufacturer=input("Manufacturer: ")
                    if self.manufacturer == 'CANCEL':
                        validMan_bool=1
                        return 0
                    elif self.manufacturer=="":
                        print('Please enter airplane manufacturer')
                    elif not self.manufacturer.isalpha():
                        print('Invalid input. Input must only consist of letters [a-z]')
                    else:
                        if len(self.manufacturer)<=3:
                            self.manufacturer = self.manufacturer.upper()
                        else:
                            self.manufacturer = self.manufacturer.capitalize()
                        validMan_bool=1

                validModel_bool = 0
                while not validModel_bool:
                    self.airplaneModel=input("Airplane model: ")
                    if self.airplaneModel == 'CANCEL':
                        validModel_bool = 1
                        return 0
                    elif self.airplaneModel=="":
                        print('Please enter airplane model')
                    elif self.airplaneModel[0] != 'F' and self.manufacturer == 'Fokker':
                        print('Invalid input. Airplane model from manufacturer: ' + self.manufacturer)
                        print('must start with F followed by integers [0-9]')
                    elif not self.airplaneModel[1:len(self.airplaneModel)].isdigit() and self.manufacturer == 'Fokker':
                        print('Invalid input. Airplane model from manufacturer: ' + self.manufacturer)
                        print('must start with F followed by integers [0-9]')
                    else:
                        validModel_bool=1

                typeID = 'NA'+self.manufacturer+self.airplaneModel

                if typeID.upper() != self.planeTypeId.upper():
                    print('Plane type ID does not match manufacturer and airplane model.')
                    print('Hint: Acceptable plane type ID for your input: ' + 'NA'+self.manufacturer+self.airplaneModel)
                    print('Please try again')
                else:
                    typeIDMatch_bool = 1

        validCap_bool = 0
        while not validCap_bool:
            self.capacity=input("Capacity: ")
            if self.capacity == 'CANCEL':
                validCap_bool=1
                return 0
            elif self.capacity=="":
                print('Please enter airplane seat capacity')
            elif not self.capacity.isdigit():
                print('Invalid input. Capacity must consist of integers only [0-9]')
            elif int(self.capacity) <=0:
                print('Capacity must be greater than zero')
            elif int(self.capacity)> 1000:
                print('Capacity is too high. Maximum capacity: 1000 seats')
            else:
                validCap_bool=1

        validEmpWeight_bool=0
        while not validEmpWeight_bool:
            self.emptyWeight=input("Empty weight [kg]: ")
            if self.emptyWeight == 'CANCEL':
                validEmpWeight_bool = 1
                return 0
            elif self.emptyWeight=="":
                print('Please enter weight')
            elif not self.emptyWeight.isdigit():
                print('Invalid input. Weight must consist of integers only [0-9]')
            elif int(self.emptyWeight) < 10000:
                print('Weight is too low. Minimum weight: 10.000kg')
            else:
                validEmpWeight_bool=1

        validTakWeight_bool=0
        while not validTakWeight_bool:
            self.maxTakeoffWeight=input("Max take off weight [kg]: ")
            if self.maxTakeoffWeight == 'CANCEL':
                validTakWeight_bool=1
                return 0
            elif self.maxTakeoffWeight=="":
                print('Please enter weight')
            elif not self.maxTakeoffWeight.isdigit():
                print('Invalid input. Weight must consist of integers only [0-9]')
            elif int(self.emptyWeight) > int(self.maxTakeoffWeight):
                print('Invalid input. Empty weight cannot be greater than max take off weight')
            else:
                validTakWeight_bool=1

        validThrust_bool = 0
        while not validThrust_bool:
            self.unitThrust=input("Unit thrust: ")
            if self.unitThrust == 'CANCEL':
                validThrust_bool=1
                return 0
            elif self.unitThrust=="":
                print('Please enter unit thrust')
            elif not self.unitThrust.replace('.','',1).isdigit():
                print('Invalid input. Unit thrust must be either an integer or double')
            else:
                validThrust_bool=1

        validCeil_bool=0
        while not validCeil_bool:
            self.serviceCeiling=input("Service ceiling : ")
            if self.serviceCeiling == 'CANCEL':
                validCeil_bool=1
                return 0
            elif self.serviceCeiling=="":
                print('Please enter service ceiling information')
            elif not self.serviceCeiling.isdigit():
                print('Invalid input. Service ceiling must consist of integers only [0-9]')
            else:
                validCeil_bool=1

        validLength_bool=0
        while not validLength_bool:
            self.length=input("Length [m]: ")
            if self.length == 'CANCEL':
                validLength_bool=1
                return 0
            elif self.length=="":
                print('Please enter length information')
            elif not self.length.replace('.','',1).isdigit():
                print('Invalid input. Length must be either an integer or double')
            elif float(self.length) < 15:
                print('Length is too small. Minimum length: 15m')
            else:
                validLength_bool=1

        validHeight_bool=0
        while not validHeight_bool:
            self.height=input("Height [m]: ")
            if self.height == 'CANCEL':
                validHeight_bool=1
                return 0
            elif self.height=="":
                print('Please enter height information')
            elif not self.height.replace('.','',1).isdigit():
                print('Invalid input. Height must be either an integer or double')
            elif float(self.height) < 6:
                print('Height is too low. Minimum height: 6m')
            else:
                validHeight_bool=1

        validWing_bool=0
        while not validWing_bool:
            self.wingspan=input("Wingspan [m]: ")
            if self.wingspan == 'CANCEL':
                validWing_bool=1
                return 0
            elif self.wingspan=="":
                print('Please enter wingspan information')
            elif not self.wingspan.replace('.','',1).isdigit():
                print('Invalid input. Wingspan must be either an integer or double')
            elif float(self.wingspan) < 6:
                print('Wingspan is too low. Minimum height: 6m')
            else:
                validWing_bool=1

        return self


    def addUpdRouteInp(self,voyage):
        destinations = getDestinations()
        aircraft = list_all_aircraft()
        self.flightNumber = voyage.flightNumber
        self.captain=voyage.captain
        self.copilot=voyage.copilot
        self.fsm=voyage.fsm
        self.fa1=voyage.fa1
        self.fa2=voyage.fa2
        self.departingFrom = voyage.departingFrom
        self.arrivingAt = voyage.arrivingAt
        self.departure = voyage.departure
        self.arrival = voyage.arrival
        self.aircraftId = voyage.aircraftId

        for plane in aircraft:
            if plane.planeInsignia == self.aircraftId:
                capacity = plane.capacity

        validSold_bool=0
        while not validSold_bool:
            self.soldTickets=input("Amount of sold seats outbound: ")
            if self.soldTickets=="CANCEL":
                validSold_bool=1
                return 0
            elif int(self.soldTickets) > int(capacity):
                print('Invalid input. Amount of sold seats exceeds plane capacity')
                print('Airplane capacity: ' + capacity)
            elif int(self.soldTickets) < 0 or self.soldTickets=='':
                print('Please enter an amount in the range 0-' + capacity)
            elif not self.soldTickets.isdigit():
                print('Invalid input. Amount must consist of integers only [0-9]')
            else:
                validSold_bool=1

        validSold2_bool=0
        while not validSold2_bool:
            outTick=input("Amount of sold seats homebound: ")
            if outTick=="CANCEL":
                validSold2_bool=1
                return 0
            elif int(outTick) > int(capacity):
                print('Invalid input. Amount of sold seats exceeds plane capacity')
                print('Airplane capacity: ' + capacity)
            elif int(outTick) < 0 or outTick=='':
                print('Please enter an amount in the range 0-' + capacity)
            elif not outTick.isdigit():
                print('Invalid input. Amount must consist of integers only [0-9]')
            else:
                validSold2_bool=1

        return self, outTick
