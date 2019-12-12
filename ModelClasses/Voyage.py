from LogicLayer.Date import*
from ModelClasses.flightRoute import*
class createVoyage:

    def __init__(self, departureFlight="",returnFlight=""):

        self.returnFlight=returnFlight
        self.departureFlight=departureFlight
        self.departureFlight.captain=""
        self.departureFlight.copilot=""
        self.departureFlight.fsm=""
        self.departureFlight.fa1=""
        self.departureFlight.fa2=""
        self.returnFlight.captain=""
        self.returnFlight.copilot=""
        self.returnFlight.fsm=""
        self.returnFlight.fa1=""
        self.returnFlight.fa2=""
