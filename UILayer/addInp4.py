from ModelClasses.Staff import*
from ModelClasses.Airplane import*
from LogicLayer.Date import*
class Inp3():


def addAirplaneInp(self):
    self.planeTypeId=input("Plane type ID: ")
    if self.planeTypeId=="CANCEL":
        self.cancel=1
        return 0
    self.manufacturer=input("Airplane manufacturer: ")
    if self.manufacturer=="CANCEL":
        self.cancel=1
        return 0
    self.airplaneModel=input("Airplane model: ")
    if self.airplaneModel=="CANCEL":
        self.cancel=1
        return 0
    self.capacity=input("Number of passenger seats: ")
    if self.capacity=="CANCEL":
        self.cancel=1
        return 0
    self.emptyWeight=input("Airplane manufacturer: ")
    if self.emptyWeight=="CANCEL":
        self.cancel=1
        return 0
    self.maxTakeoffWeight=input("Airplane model: ")
    if self.maxTakeoffWeight=="CANCEL":
        self.cancel=1
        return 0
    self.unitThrust=input("Number of passenger seats: ")
    if self.unitThrust=="CANCEL":
        self.cancel=1
        return 0
    self.serviceCeiling=input("Airplane manufacturer: ")
    if self.serviceCeiling=="CANCEL":
        self.cancel=1
        return 0
    self.length=input("Airplane model: ")
    if self.length=="CANCEL":
        self.cancel=1
        return 0
    self.height=input("Number of passenger seats: ")
    if self.height=="CANCEL":
        self.cancel=1
        return 0
    self.wingspan=input("Number of passenger seats: ")
    if self.wingspan=="CANCEL":
        self.cancel=1
        return 0
    return self.planeTypeId,self.manufacturer,self.airplaneModel,self.capacity,self.emptyWeight,self.maxTakeoffWeight,self.unitThrust,self.serviceCeiling,self.length,self.height,self.wingspa
