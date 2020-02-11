
from datetime import datetime
import pandas as pd

STATION_TYPE = {
    "AAXX" : "Land station",
    "BBXX" : "Ship",
    "ZZYY" : "Buoy",
    "OOXX" : "Mobile land station"
}

TABLE_1855 = {
    "0" : "Wind speed estimated, reported in meters per second.",
    "1" : "Wind speed obteined from anemometer, reported in meters per second.",
    "3" : "Wind speed estimated, reported in knots.",
    "4" : "Wind speed obteined from anemometer, reported in knots.",
    "/" : "Wind speed not available."
}

station_data = pd.read_csv('synopy/utils/data/stations.csv')

def str2date(date_str: str):
    return datetime.strptime(date_str, '%Y%m%d%H%M')

def extract_station_name(synop_code: str):
    station = station_data[(station_data["SYNOP"] == synop_code)]
    return station["NAME"].values[0]

def extract_wind_units(code: str):
    return TABLE_1855[code]

