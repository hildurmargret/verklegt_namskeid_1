from ModelClasses.Staff import*
from ModelClasses.Airplane import*
from LogicLayer.Date import*
class Inp4():


    def addAirplaneInp(self,airplane):
        # self.planeTypeId=input("Plane type ID: ")
        # if self.planeTypeId=="CANCEL":
        #     self.cancel=1
        #     return 0
        # self.manufacturer=input("Airplane manufacturer: ")
        # if self.manufacturer=="CANCEL":
        #     self.cancel=1
        #     return 0
        # self.airplaneModel=input("Airplane model: ")
        # if self.airplaneModel=="CANCEL":
        #     self.cancel=1
        #     return 0
        # self.capacity=input("Number of passenger seats: ")
        # if self.capacity=="CANCEL":
        #     self.cancel=1
        #     return 0
        # self.emptyWeight=input("Airplane manufacturer: ")
        # if self.emptyWeight=="CANCEL":
        #     self.cancel=1
        #     return 0
        # self.maxTakeoffWeight=input("Airplane model: ")
        # if self.maxTakeoffWeight=="CANCEL":
        #     self.cancel=1
        #     return 0
        # self.unitThrust=input("Number of passenger seats: ")
        # if self.unitThrust=="CANCEL":
        #     self.cancel=1
        #     return 0
        # self.serviceCeiling=input("Airplane manufacturer: ")
        # if self.serviceCeiling=="CANCEL":
        #     self.cancel=1
        #     return 0
        # self.length=input("Airplane model: ")
        # if self.length=="CANCEL":
        #     self.cancel=1
        #     return 0
        # self.height=input("Number of passenger seats: ")
        # if self.height=="CANCEL":
        #     self.cancel=1
        #     return 0
        # self.wingspan=input("Number of passenger seats: ")
        # if self.wingspan=="CANCEL":
        #     self.cancel=1
        #     return 0
        # return self.planeTypeId,self.manufacturer,self.airplaneModel,self.capacity,self.emptyWeight,self.maxTakeoffWeight,self.unitThrust,self.serviceCeiling,self.length,self.height,self.wingspa

        planeTypeId=input("Plane type ID: ")
        if planeTypeId=="":
            self.planeTypeId=airplane.planeTypeId
        else:
            self.planeTypeId=planeTypeId
        manufacturer=input("Manufacturer: ")
        if manufacturer=="":
            self.manufacturer=airplane.manufacturer
        else:
            self.manufacturer=manufacturer
        airplaneModel=input("Airplane model: ")
        if airplaneModel=="":
            self.airplaneModel=airplane.airplaneModel
        else:
            self.airplaneModel=airplaneModel
        capacity=input("Capacity: ")
        if capacity=="":
            self.capacity=airplane.capacity
        else:
            self.capacity=capacity
        emptyWeight=input("Empty weight: ")
        if emptyWeight=="":
            self.emptyWeight=airplane.emptyWeight
        else:
            self.emptyWeight=emptyWeight
        maxTakeoffWeight=input("Max take off weight: ")
        if maxTakeoffWeight=="":
            self.maxTakeoffWeight=airplane.maxTakeoffWeight
        else:
            self.maxTakeoffWeight=maxTakeoffWeight
        unitThrust=input("Unit thrus: ")
        if unitThrust=="":
            self.unitThrust=airplane.unitThrust
        else:
            self.unitThrust=unitThrust
        serviceCeiling=input("Service ceiling : ")
        if serviceCeiling=="":
            self.serviceCeiling=airplane.serviceCeiling
        else:
            self.serviceCeiling=serviceCeiling
        length=input("Length: ")
        if length=="":
            self.length=airplane.length
        else:
            self.length=length
        height=input("Height: ")
        if height=="":
            self.height=airplane.height
        else:
            self.height=height
        wingspan=input("Wingspan: ")
        if wingspan=="":
            self.wingspan=airplane.wingspan
        else:
            self.wingspan=wingspan
        return self
