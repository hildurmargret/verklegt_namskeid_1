from LogicLayer.LL_API import*
def checkFlightNumberInp():

    #Fall sem athugar hvort innslegið flightnumber sé til eða ekki

    LL = LL_API()
    flights = LL.LLgetFlights()
    singleFlights = []

    seen = set()
    singleFlights = [x for x in flights if x.flightNumber not in seen and not seen.add(x.flightNumber)]

    validFlNo_bool=0
    flNoExists_bool=0
    while not validFlNo_bool:
        flightNumber=input("Flight number: ")
        if flightNumber == 'CANCEL':
            return 0
            validFlNo_bool=1
        else:
            for flight in flights:
                if flightNumber == flight.flightNumber:
                    flNoExists_bool=1
                    break
            if not flNoExists_bool:
                print('Invalid input. Flight number must be one of the following')
                for flight in singleFlights:
                    print(flight.flightNumber)
            else:
                validFlNo_bool= 1
                return flightNumber
