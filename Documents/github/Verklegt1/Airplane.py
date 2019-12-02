class Airplane:
    def __init__(self):
        self.Name=""
        self.airplaneModel=""
        self.manufacturer=""
        self.seats=0

    def addInfo(self):
        self.Name=input("Airplane Name: ")
        self.airplaneModel=input("Airplane model: ")
        self.manufacturer=input("Airplane manufacturer: ")
        self.seats=int(input("Number of passenger seats: "))
#Komment
#komment
