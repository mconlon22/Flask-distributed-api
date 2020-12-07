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
for i in range(0, len(addresses),2500):
    if i>0:
        num=i-2500
    else:
        num=0
    data["Address"].iloc[num:i].to_csv("./splitaddresses/address"+str(i)+".csv")
