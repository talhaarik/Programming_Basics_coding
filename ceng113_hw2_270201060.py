with open("provinces.txt", "r") as file:
    myList = [(line.strip()).split(",") for line in file]

cityName = []
lat = []
lon = []

for i in range(len(myList)):
    cityName.append(myList[i][0])
    lat.append(myList[i][1])
    lon.append(myList[i][2])

cityFound = False
exactCityFound = False
exactCity = ""
while (not exactCityFound):
    Departure_province = input("Departure province:\n").upper()
    retList = []

    for i in range(len(myList)):
        if(Departure_province == myList[i][0][:len(Departure_province)]):
            cityFound = True
            retList.append(myList[i][0])
        if(Departure_province == myList[i][0]):
            exactCityFound = True
            exactCity = myList[i][0]
            break

    if(not exactCityFound):
        if (cityFound and (not exactCityFound)):
            retList = sorted(retList)
            if len(retList) == 1:
                for i in range(len(retList)):
                    print("Province not found!")
                    print("Possible province:"+str((retList[i])))
            else:
                print("Possible provinces:", end="")
                for i in range(len(retList)-1):
                    print(retList[i], end=",")
                print(retList[-1])
        if ((not cityFound)):
            print("Province not found!")

        cityFound = False
        exactCityFound = False

cityFound2 = False
exactCityFound2 = False
exactCity2 = ""
while (not exactCityFound2):
    Arrival_province = input("Arrival province:\n").upper()
    if(Arrival_province == Departure_province):
        print("Enter a different province!")
        continue
    retList2 = []

    for i in range(len(myList)):
        if (Arrival_province == myList[i][0][:len(Arrival_province)]):
            cityFound2 = True
            retList2.append(myList[i][0])
        if (Arrival_province == myList[i][0]):
            exactCityFound2 = True
            exactCity2 = myList[i][0]
            break

    if (not exactCityFound2):
        if (cityFound2 and (not exactCityFound2)):
            if len(retList2) == 1:
                for i in range(len(retList2)):
                    print("Province not found!")
                    print("Possible province:"+str((retList2[i])))
            else:
                print("Province not found!")
                print("Possible provinces:", end="")
                retList2 = sorted(retList2)
                for i in range(len(retList2)-1):
                    print(retList2[i], end=",")
                print(retList2[-1])
        if ((not cityFound2)):
            print("Province not found!")

        cityFound2 = False
        exactCityFound2 = False

vehicle = {"car": 90, "motorcycle": 80, "bicycle": 25}
travelType = ""
vehicleFound = False
while(not vehicleFound):
    travelType = input("Enter travel type:\n").lower()

    if(travelType in vehicle.keys()):
        vehicleFound = True
    if(travelType not in vehicle.keys()):
        vehicleFound = False

with open("provinces.txt", "r") as file:
    myList2 = [(line.strip()).split(",") for line in file]
for i in range(len(myList2)):
    if (Departure_province == myList2[i][0]):
        x1 = myList2[i][1]
        y1 = myList2[i][2]
    if (Arrival_province == myList2[i][0]):
         x2 = myList2[i][1]
         y2 = myList2[i][2]

dx = float(x2) - float(x1)
dy = float(y2) - float(y1)
print("\nI am calculating the distance between {} and {} ...\n".format(Departure_province, Arrival_province) )
a = abs((dx**2 + dy**2)**(1/2)*100)
print("Distance:", "{:.2f}".format(a), "km")

time = a / int(vehicle.get(travelType))
print("Approximate travel time with",str(travelType.upper())+":",int(time), "hours", int((time - int(time))*60), "minutes")

# Getting selected starting city's name, lat and long information
indexDep = cityName.index(exactCity)
currentLat = lat[indexDep]
currentLon = lon[indexDep]

dictionary = {}
closeCities = []

# Calculating all distances from starting point to all cities
for i in range(len(cityName)):
    dx = float(lat[i]) - float(currentLat)
    dy = float(lon[i]) - float(currentLon)
    distance = abs((dx**2 + dy**2)**(1 / 2)*100)
    dictionary[cityName[i]] = distance


# Sorting calculated distances from lower values to upper values
sorted_values = sorted(dictionary.values())  # Sort the values
sorted_dict = {}

for i in sorted_values:
    for k in dictionary.keys():
        if dictionary[k] == i:
            sorted_dict[k] = dictionary[k]
            break


key_list = list(sorted_dict.keys())
val_list = list(sorted_dict.values())

# To print closer cities in alphabetical order
alphabetical = []
alphabetical.append(key_list[1])
alphabetical.append(key_list[2])
alphabetical.append(key_list[3])

alphabetical.sort()

print("Recommended places close to " + str(exactCity) + ":"+alphabetical[0]+","+alphabetical[1]+","+alphabetical[2])