# every train of the trip must be trainType for this to return something
def filterByTrainType(trainType, trips):
    filteredList = []
    for trip in trips:
        boo = True
        for connection in trip.connections:
            if connection.train_type != trainType:
                boo = False
                break
        if boo:
            filteredList.append(trip)
    return filteredList

# every corresponding dayOfWeek of the trip must be true for this to return something
def filterByDayOfWeek(dayOfWeek, trips):
    filteredList = []
    for trip in trips:
        boo = True
        for connection in trip.connections:
            if connection.days[dayOfWeek] == False:
                boo = False
                break
        if boo:
            filteredList.append(trip)
    return filteredList