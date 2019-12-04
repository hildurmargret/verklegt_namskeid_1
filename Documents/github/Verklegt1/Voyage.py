class Voyage:

    def __init__(self):
        self.title=""
        self.airplaneName=""
        self.numberOfPilots=0
        self.numberOfCabin=0
        self.flightDuration=0
        self.cancel=0

    def addInfo(self):
        self.title=input("Voyage title: ")
        if self.title=="CANCEL":
            self.cancel=1
            return 0
        self.airplaneName=input("Airplane Name: ")
        if self.airplaneName=="CANCEL":
            self.cancel=1
            return 0
        self.numberOfPilots=input("Number of pilots needed: ")
        if self.numberOfPilots=="CANCEL":
            self.cancel=1
            return 0
        self.numberOfCabin=input("Number of cabin crew needed: ")
        if self.numberOfCabin=="CANCEL":
            self.cancel=1
            return 0
        self.flightDuration=input("Flight duration: ")
        if self.flightDuration=="CANCEL":
            self.cancel=1
            return 0
