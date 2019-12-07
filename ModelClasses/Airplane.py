class Airplane:
    def __init__(self):
        self.Name=""
        self.airplaneModel=""
        self.manufacturer=""
        self.seats=0
        self.cancel=0

    def __init__(self, name, model, manufacturer, seats):
        self.Name = name
        self.airplaneModel = model
        self.manufacturer = manufacturer
        self.seats = seats
        self.cancel=0

    def addInfo(self):
        self.Name=input("Airplane Name: ")
        if self.Name=="CANCEL":
            self.cancel=1
            return 0
        self.airplaneModel=input("Airplane model: ")
        if self.airplaneModel=="CANCEL":
            self.cancel=1
            return 0
        self.manufacturer=input("Airplane manufacturer: ")
        if self.name=="CANCEL":
            self.cancel=1
            return 0
        self.seats=input("Number of passenger seats: ")
        if self.seats=="CANCEL":
            self.cancel=1
            return 0
