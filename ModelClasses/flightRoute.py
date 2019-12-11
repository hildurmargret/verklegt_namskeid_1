class createFlightRoute:

    def __init__(self,flightNumber="", departingFrom="", arrivingAt="",departure="", arrival="",aircraftId="",captain="",copilot="",fsm="",fa1="",fa2="",tickets=0):
        self.flightNumber=flightNumber
        self.departingFrom=departingFrom
        self.arrivingAt=arrivingAt
        self.departure=departure
        self.arrival=arrival
        self.aircraftId=aircraftId
#        self.numberOfCabin=numberOfCabin
#        self.numberOfPilots=numberOfPilots
        self.captain=captain
        self.copilot=copilot
        self.fsm=fsm
        self.fa1=fa1
        self.fa2=fa2
        self.soldTickets=tickets
        self.cancel=0
