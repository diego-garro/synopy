
import re
from .utils import station_tools as tools

ERRORS = {
    1 : "Indicator {} for {} is not in {}."
}

class Synoptic:
    
    errors = []
    
    def __init__(self, report: str):
        self.report = report.split(' ')
        self.date = self._set_date()
        self.station_type = self._set_station_type()
        self.station_name = self._set_station_name()
        self.wind_units = self._set_units_wind()
    
    def _set_date(self):
        return tools.str2date(self.report[0])
    
    def _set_station_type(self):
        return tools.STATION_TYPE[self.report[1]]
    
    def _set_units_wind(self):
        indicator = "iw"
        objetive = "source and units of wind speed"
        table = "Table 1855"
        try:
            return tools.extract_wind_units(self.report[2][-1])
        except KeyError:
            self.errors.append(ERRORS[1].format(indicator, objetive, table))
    
    def _set_station_name(self):
        return re.sub(r'\s{2,}', '', tools.extract_station_name(self.report[3]))