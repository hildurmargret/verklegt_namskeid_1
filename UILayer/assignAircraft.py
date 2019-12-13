from UILayer.UI_Manager import*
from LogicLayer.Date import*

def assignAircraft(voyage):

    UI = UI_Manager()
    aircraft = UI.UIgettingAirplanes()
    flights = UI.UIgetFlights()

    validID_bool=0
    while not validID_bool:
        IDExists_bool=0
        available_bool=1
        aircraftID=input("AircraftId: ")
        if aircraftID == 'CANCEL':
            validID_bool=1
            return 0
        else:
            for plane in aircraft:
                if plane.planeInsignia == aircraftID:
                    IDExists_bool=1

            if not IDExists_bool:
                print('Invalid input. AircraftId must be one of the following:')
                for plane in aircraft:
                    print(plane.planeInsignia)
            else:
                for flight in flights:
                    if flight.departingFrom == 'KEF' and flight.aircraftId == aircraftID:

                        if voyage.departureFlight.departure < add_hour(flight.departure,5) and add_hour(flight.departure,5) <= voyage.returnFlight.arrival:
                            available_bool=0

                        elif voyage.departureFlight.departure <= flight.departure and flight.departure < voyage.returnFlight.arrival:
                            available_bool=0

                if not available_bool:
                    print('This airplane is unavailable at the time of the voyage. Please choose another one.')
                else:
                    validID_bool = 1

    return aircraftID
