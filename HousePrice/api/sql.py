from pandas.core.frame import DataFrame
import pyodbc
import pandas as pd
from pandasql import sqldf

data = pd.read_csv('../PPR.csv')
def pysqldf(q): return sqldf(q, globals())


def find_sold_houses(x, y):
    return pysqldf("SELECT * FROM data where lon BETWEEN " + str(x-.0001) + " AND " +
                  str(x+.0001) + " and lat BETWEEN " + str(y-.0001)+" AND " + str(y+.0001) + ";")

