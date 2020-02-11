
from .utils import tools

class Synoptic:
    
    def __init__(self, report: str):
        self.report = report.split(' ')
        self.date = self._set_date()
        self.station_type = self._set_station_type()
    
    def _set_date(self):
        return tools.str2date(self.report[0])
    
    def _set_station_type(self):
        return tools.STATION_TYPE[self.report[1]]