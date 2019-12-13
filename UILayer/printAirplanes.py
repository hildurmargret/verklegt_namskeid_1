
def printAircraft(Airplanes):

    #prentar ut lista af flugvelum
    for i in range(len(Airplanes)):
        print(Airplanes[i].planeInsignia)
        print('Plane Type ID: ' + Airplanes[i].planeTypeId + '\n' + 'Manufacturer: ' + Airplanes[i].manufacturer + '\n' + 'Airplane Model: ' + Airplanes[i].airplaneModel + '\n' + 'Capacity: ' + Airplanes[i].capacity + '\n' + 'Empty weight: ' + Airplanes[i].emptyWeight + '\n' + 'Max take off weight: ' + Airplanes[i].maxTakeoffWeight + '\n' + 'Unit thrust: ' + Airplanes[i].unitThrust + '\n' + 'Service ceiling: ' + Airplanes[i].serviceCeiling + '\n' + 'Length: ' + Airplanes[i].length + '\n' + 'Heigth: ' + Airplanes[i].height + '\n' + 'Wingspan: ' + Airplanes[i].wingspan)
        print('')
