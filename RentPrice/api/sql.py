from pandas.core.frame import DataFrame
import pyodbc
import pandas as pd
from pandasql import sqldf
from geopy.geocoders import Nominatim
import usaddress

data = pd.read_csv('./rentData.csv')
def pysqldf(q): return sqldf(q, globals())


def find_sold_houses(x, y):
    geolocator = Nominatim(user_agent="martin")
    location = geolocator.reverse(x+","+y)
    print(location.raw['address']['suburb'])
    suburb=location.raw['address']['suburb']
    return pysqldf("SELECT * FROM data where Suburb Like  " +"'"+suburb+"'"+";")


print(find_sold_houses("53.3641928", "-6.2398748"))
