import pandas as pd
import datetime as dt
from sklearn import preprocessing


def dummies_labelEncoder(columna):
    le = preprocessing.LabelEncoder()

    return le.fit_transform(columna)




def time_to_ordinal(to_convert):
    # el formato de to_convert tiene que ser: basededatos['columna_fecha']
    # EJM: data_df['Date'] = pd.to_datetime(data_df['Date'])

    to_convert = pd.to_datetime(to_convert)
    to_convert = to_convert.map(dt.datetime.toordinal)
    return to_convert
