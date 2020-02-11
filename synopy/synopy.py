
import re
from .utils import station_tools as tools

ERRORS = {
    1 : "Indicator {} for {} is not in {}."
}

class Synoptic:
    
    errors = []
    _sections = [
        '222',
        '333',
        '444',
        '555'
    ]
    _next_section_index = 4
    
    def __init__(self, report: str):
        self.report = report.replace('\n', '').split(' ')
        self.date = self._set_date()
        self.station_type = self._set_station_type()
        self.station_name = self._set_station_name()
        self.wind_units = self._set_units_wind()
        self.section_one = self._set_section()
        self.section_two = self._set_section(section_separator='222')
        self.section_three = self._set_section(section_separator='333')
        self.section_four = self._set_section(section_separator='444')
    
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
    
    def _set_section(self, section_separator='111'):
        section = []
        if section_separator == '111':
            pass
        else:
            if section_separator not in self.report:
                return section
        
        for group in self.report[self._next_section_index:]:
            if group in self._sections:
                self._next_section_index = self.report.index(group) + 1
                break
            section.append(group)
        return section
    
    