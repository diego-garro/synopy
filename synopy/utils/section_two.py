
from .templates import Group, Section, Group_Indicator, Table_Indicator, Value_Indicator
from datetime import datetime

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

class Section_Two(Section):
    
    def __init__(self, section: list, index=0):
        super().__init__(section, index)
        
        if len(self.section) > 0:
            # Group 0snTwTwTw
            self._0snTwTwTw = Group_0snTwTwTw(self.section[0], "0snTwTwTw")
            self._verify_indicators_and_copy_errors(self._0snTwTwTw)
            self._include_group_to_groups(self._0snTwTwTw)