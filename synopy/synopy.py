
import re
from .utils import station_tools as tools
from .utils.section_one import Section_One
from .utils.section_two import Section_Two
from datetime import datetime

ERRORS = {
    1 : "Indicator {} for {} is not in {}."
}

class Synoptic:

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
        self.errors = []
        self.station_type = self._set_station_type()
        self.station_name = self._set_station_name()
        self.wind_units = self._set_wind_units()
        self.section_one = Section_One(self._set_section(), self.report[2][-1])
        self.section_two = Section_Two(self._set_section(section_separator='222'))
        self.section_three = self._set_section(section_separator='333')
        self.section_four = self._set_section(section_separator='444')
        self._copy_errors()
    
    def _set_date(self):
        return tools.str2date(self.report[0])
    
    def _set_station_type(self):
        return tools.STATION_TYPE[self.report[1]]
    
    def _set_wind_units(self):
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
    
    def _copy_errors(self):
        sections = [self.section_one, self.section_two]
        for section in sections:
            for err in section.errors:
                self.errors.append(err)
    
    def _write_report_characteristics(self):
        container = []
        date = datetime.strftime(self.date, "Date: %Y/%m/%d %H:%M:00.")
        container.append(date)
        container.append("Station type: {}.".format(self.station_type))
        container.append("Station name: {}.".format(self.station_name))
        container.append("Wind units: {}".format(self.wind_units))
        container.append(str(self.section_one))
        return "\n".join(container)
    
    def __str__(self):
        return self._write_report_characteristics()
    
    