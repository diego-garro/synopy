
from .templates import Group, Section, Group_Indicator, Table_Indicator, Value_Indicator
from datetime import datetime
from .section_one import TABLE_0877

ERRORS = {
    1 : "Indicator {} for {} group, only can take 0 or 1 as value.",
}

class Group_0snTwTwTw(Group):
    
    def __init__(self, group: str, name: str):
        super().__init__(group, name, "Sea-surface Temperature Group")
        self.group_indicator = Group_Indicator(self._extract_indicator(0, 1), "0")
        self._sn = Value_Indicator(self._extract_indicator(1, 2), "sn", "sign of the sea-surface temperature")
        self._TwTwTw = Value_Indicator(self._extract_indicator(2, 5), "TwTwTw", "sea-surface water temperature in tenths of degrees Celcius")
    
    def verify_indicators(self):
        self.verify_group_indicator(value=0)
        if self.found:
            self.verify_value_indicator(self._sn)
            self.verify_value_indicator(self._TwTwTw)
            if self._sn.indicator > 1:
                self._errors.append(ERRORS[1].format(self._sn.name, self.name))
    
    def _show_characteristics(self):
        characteristics = [".:{}:.".format(self._group_objective)]
        if self._sn.indicator == 0:
            characteristics.append("\nSea-surface water temperature: {:.1f}°C".format(self._TwTwTw.indicator / 10))
        elif self._sn.indicator == 1:
            characteristics.append("\nSea-surface water temperature: -{:.1f}°C".format(self._TwTwTw.indicator / 10))
        else:
            characteristics.append("\nSea-surface water temperature: {:.1f}°C, sign not valid".format(self._TwTwTw.indicator / 10))
        return ''.join(characteristics)

TABLE_wave_height = {
    -2 : "Wave Height HwaHwa Table",
    -1 : "Wave Height",
     0 : "<0.25 meters (<0.8 feet)",
     1 : "0.25 - <0.75 meters (0.8 - <2.5 feet)",
     2 : "0.75 - <1.25 meters (0.8 - <2.5 feet)",
     3 : "1.25 - <1.75 meters (4.1 - <5.7 feet)",
     4 : "1.75 - <2.25 meters (5.7 - <7.4 feet)",
     5 : "2.25 - <2.75 meters (7.4 - <9.0 feet)",
     6 : "2.75 - <3.25 meters (9.0 - <10.7 feet)",
     7 : "3.25 - <3.75 meters (10.7 - <12.3 feet)",
     8 : "3.75 - <4.25 meters (12.3 - <13.9 feet)",
     9 : "4.25 - <4.75 meters (13.9 - <15.6 feet)",
    10 : "4.75 - <5.25 meters (15.6 - <17.2 feet)",
    11 : "5.25 - <5.75 meters (17.2 - <18.9 feet)",
    12 : "5.75 - <6.25 meters (18.9 - <20.5 feet)",
    13 : "6.25 - <6.75 meters (20.5 - <22.1 feet)",
    14 : "6.75 - <7.25 meters (22.1 - <23.8 feet)",
    15 : "7.25 - <7.75 meters (23.8 - <25.4 feet)",
    16 : "7.75 - <8.25 meters (25.4 - <27.1 feet)",
    17 : "8.25 - <8.75 meters (27.1 - <28.7 feet)",
    18 : "8.75 - <9.25 meters (28.7 - <30.3 feet)",
    19 : "9.25 - <9.75 meters (30.3 - <32.0 feet)",
    20 : "9.75 - <10.25 meters (32.0 - <33.6 feet)"
}

class Group_1PwaPwaHwaHwa(Group):
    
    def __init__(self, group: str, name: str):
        super().__init__(group, name, "Instrumental Wave Data Group")
        self.group_indicator = Group_Indicator(self._extract_indicator(0, 1), "1")
        self._PwaPwa = Value_Indicator(self._extract_indicator(1, 3), "PwaPwa", "period of the waves obtained by instrumental methods, in whole seconds")
        self._HwaHwa = Table_Indicator(self._extract_indicator(3, 5), "HwaHwa", TABLE_wave_height)
    
    def verify_indicators(self):
        self.verify_group_indicator(value=1)
        if self.found:
            self.verify_value_indicator(self._PwaPwa)
            self.verify_table_indicator(self._HwaHwa)
    
    def _show_characteristics(self):
        characteristics = [".:{}:.".format(self._group_objective)]
        characteristics.append("\nPeriod of the waves: {} seconds".format(self._PwaPwa.indicator))
        characteristics.append("\nHeight of waves: {}".format(self._HwaHwa.__str__()))
        return ''.join(characteristics)

class Group_2PwPwHwHw(Group):
    
    def __init__(self, group: str, name: str):
        super().__init__(group, name, "Wind Wave Group")
        self.group_indicator = Group_Indicator(self._extract_indicator(0, 1), "2")
        self._PwPw = Value_Indicator(self._extract_indicator(1, 3), "PwPw", "estimated period of the wind wave in whole seconds")
        self._HwHw = Value_Indicator(self._extract_indicator(3, 5), "HwHw", "estimated height of the wind waves in units of half-meters")

    def verify_indicators(self):
        self.verify_group_indicator(value=2)
        if self.found:
            self.verify_value_indicator(self._PwPw)
            self.verify_value_indicator(self._HwHw)
    
    def _show_characteristics(self):
        characteristics = [".:{}:.".format(self._group_objective)]
        characteristics.append("\nPeriod of the wind wave: {} seconds".format(self._PwPw.indicator))
        characteristics.append("\nHeight of wind waves: {} half-meters".format(self._HwHw.indicator))
        return ''.join(characteristics)

class Group_3dw1dw1dw2dw2(Group):
    
    def __init__(self, group: str, name: str):
        super().__init__(group, name, "Swell Wave Direction Group")
        self.group_indicator = Group_Indicator(self._extract_indicator(0, 1), "3")
        self._dw1dw1 = Table_Indicator(self._extract_indicator(1, 3), "dw1dw1", TABLE_0877)
        self._dw2dw2 = Table_Indicator(self._extract_indicator(3, 5), "dw2dw2", TABLE_0877)
    
    def verify_indicators(self):
        self.verify_group_indicator(value=3)
        if self.found:
            self.verify_table_indicator(self._dw1dw1)
            self.verify_table_indicator(self._dw2dw2)
    
    def _show_characteristics(self):
        characteristics = [".:{}:.".format(self._group_objective)]
        characteristics.append("\nTrue direction, from which first swell wave is moving: {}".format(self._dw1dw1.__str__()))
        characteristics.append("\nTrue direction, from which second swell wave is moving: {}".format(self._dw2dw2.__str__()))
        return ''.join(characteristics)

class Section_Two(Section):
    
    def __init__(self, section: list, index=0):
        super().__init__(section, index)
        
        if len(self.section) > 0:
            # Group 0snTwTwTw
            self._0snTwTwTw = Group_0snTwTwTw(self.section[0], "0snTwTwTw")
            self._verify_indicators_and_copy_errors(self._0snTwTwTw)
            self._include_group_to_groups(self._0snTwTwTw)

            # Group 1PwaPwaHwaHwa
            self._1PwaPwaHwaHwa = Group_1PwaPwaHwaHwa(self.section[1], "1PwaPwaHwaHwa")
            self._verify_indicators_and_copy_errors(self._1PwaPwaHwaHwa)
            self._include_group_to_groups(self._1PwaPwaHwaHwa)

            # Group 2PwPwHwHw
            self._2PwPwHwHw = Group_2PwPwHwHw(self.section[2], "2PwPwHwHw")
            self._verify_indicators_and_copy_errors(self._2PwPwHwHw)
            self._include_group_to_groups(self._2PwPwHwHw)

            # Group 3dw1dw1dw2dw2
            self._3dw1dw1dw2dw2 = Group_3dw1dw1dw2dw2(self.section[3], "3dw1dw1dw2dw2")
            self._verify_indicators_and_copy_errors(self._3dw1dw1dw2dw2)
            self._include_group_to_groups(self._3dw1dw1dw2dw2)