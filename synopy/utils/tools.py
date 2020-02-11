
from datetime import datetime

STATION_TYPE = {
    "AAXX" : "Land station",
    "BBXX" : "Ship",
    "ZZYY" : "Buoy",
    "OOXX" : "Mobile land station"
}

def str2date(date_str: str):
    return datetime.strptime(date_str, '%Y%m%d%H%M')
