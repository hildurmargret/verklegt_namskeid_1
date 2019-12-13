from ModelClasses.Staff import*
from ModelClasses.Airplane import*
from LogicLayer.Date import*
from LogicLayer.LL_API import*

LL=LL_API()

class Inp4():
    def addAirplaneInp(self,airplane):

        aircraft = LL.LLgetAircraft()

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
