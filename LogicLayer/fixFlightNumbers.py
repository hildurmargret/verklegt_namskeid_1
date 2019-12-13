from DataLayer.getDestinations import*
from ModelClasses.flightRoute import*
import operator


def fixFlNo(flights, destinations):
    #Fall sem tekur inn lista af flugum asamt ollum mogulegum afangastodum og skilar flugum med rettum flugnumerum

    #Buum til lista af ollum afangastodum nan air
    for dest in destinations:
        if dest.id == 'KEF':
            destinations.remove(dest)

    retFlights = []
    #Forum i gegnum oll flugin
    for flight in flights:
        #Oll flugnumer byrja a NA
        new_flNo = 'NA'

        #Forum i gegnum alla afangastadina. Hver afangastadur hefur sitt eigid einkennisnumer.
        for i in range(len(destinations)):
            #Ef flug er a leid til afangastadarins sem vid erum ad skoda eda a leid fra honum baetist
            #einkennisnumer afangastadarins aftan vid NA i flugnumeri flugsins
            if flight.departingFrom == destinations[i].id or flight.arrivingAt == destinations[i].id:
                if (i+1) < 10: #einkennisnumerin eiga ad vera tveggja stafa tolur, 0 baett framan vid tolur < 10
                    new_flNo = new_flNo + '0' + str(i+1)
                else:
                    new_flNo = new_flNo + str(i+1)

        #flugum gefin halfklarud ny flugnumer
        flight.flightNumber = new_flNo

    #forum aftur i gegnum alla afangastadina og oll flugin
    for dest in destinations:
        #gerum greinarmun a milli theirra fluga sem eru a leid ut og a leid heim
        flightsToDest_i = []
        flightsFromDest_i = []

        for flight in flights:
            if flight.departingFrom == dest.id:
                flightsFromDest_i.append(flight)
            elif flight.arrivingAt == dest.id:
                flightsToDest_i.append(flight)

        #rodum flugum i rod eftir brottfarartima
        flightsFromDest_i.sort(key=lambda flight: flight.departure)
        flightsToDest_i.sort(key=lambda flight: flight.departure)

    #Sidasti stafur flugnumersins fer eftir tvi hversu morg flug eru til sama afangastadar
    #hvern dag numer hvad i rodinni thann daginn thetta flug er
        #Viljum ad counter byrji i 0
        counter = -1
        if len(flightsFromDest_i) != 0:
            #geymum dagsetningu fyrsta flugsins, til ad geta borid saman vid hin flugin
            day = str(flightsFromDest_i[0].departure[0:10]) + '00:00:00'

        #fer i gegnum oll flugin a leidinni ut
        for k in range(len(flightsFromDest_i)):

            #geymum dagsetningu thessa tiltekna flugs
            date = str(flightsFromDest_i[k].departure[0:10]) + '00:00:00'
            #Ef flugid er komid yfir a nyjan dag nullast counter annars baetist einn vid counter
            if day != date:
                counter = 0
            else:
                counter = counter + 1

            #flug a leid fra afangastad, til Islands, fa oddatolunumer
            flightsFromDest_i[k].flightNumber = flightsFromDest_i[k].flightNumber + str(counter*2 + 1)
            #flug a leid a afangastad, fra Islandi, fa sletttolunumer
            flightsToDest_i[k].flightNumber = flightsToDest_i[k].flightNumber + str(counter*2)
            #set oll flugin i listann retFlights, listanum sem eg skila
            retFlights.append(flightsToDest_i[k])
            retFlights.append(flightsFromDest_i[k])
            #uppfaeri gildid a day sem notad er til ad bera naesta flug saman vid
            day = str(flightsFromDest_i[k].departure[0:10]) + '00:00:00'

    return retFlights
