class Voyage:

    def __init__(self):
        self.title=""
        self.airplaneName=""
        self.numberOfPilots=0
        self.numberOfCabin=0
        self.flightDuration=0

    def addInfo(self):
        self.title=input("Name: ")
        self.airplaneName=input("Airplane Name: ")
        self.numberOfPilots=input("Number of pilots needed: ")
        self.numberOfCabin=input("Number of cabin crew needed: ")
        self.flightDuration=input("Flighr duration: ")
