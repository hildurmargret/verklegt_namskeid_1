from ModelClasses.Staff import*
from ModelClasses.Airplane import*
from ModelClasses.flightRoute import*
from LogicLayer.Date import*
from DataLayer.getDestinations import*
from DataLayer.getAircraft import*

class Inp5():

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

        #print(self.aircraftId)

        for plane in aircraft:
            if plane.planeInsignia == self.aircraftId:
                capacity = plane.capacity

        #print(capacity)

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

        #print(outTick)

        return self, outTick
