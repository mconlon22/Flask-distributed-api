from geopy.geocoders import Nominatim
import csv
import pandas as pd


def savedata(locations, range):
    with open('./dataoutput/housedata'+str(range)+'.csv', mode='w') as housedata:
        employee_writer = csv.writer(
            housedata, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        employee_writer.writerow(['address', 'lon', 'lat'])
        for location in locations:
            employee_writer.writerow(location)


geolocator = Nominatim(user_agent="martan")
data = pd.read_csv("PPR-ALL.csv", engine='python')
addresses = data["Address"]
data["Address"].to_csv("./address.csv")
numFound = 0
for i in range(300000, 400000):
    if(i % 10000 == 0):
        savedata(locations, i)
        locations = []
    try:
        location = geolocator.geocode(addresses[i]+", Ireland")
        print(location)
        locations.append([addresses[i], location.latitude, location.longitude])
        numFound += 1
        print("found: "+str(numFound) + "iteration number: " + str(i))
    except:
        locations.append([addresses[i], 0, 0])
        print('error')

with open('housedata.csv', mode='w') as housedata:
    employee_writer = csv.writer(
        housedata, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    employee_writer.writerow(['address', 'lon', 'lat'])
    for location in locations:
        employee_writer.writerow(location)
