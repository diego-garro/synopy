
from .templates import Group, Section, Group_Indicator, Table_Indicator, Value_Indicator

TABLE_1819 = {
    -2 : "Table 1819",
    -1 : "inclusion or omission of precipitacion data",
     0 : "In sections 1 and 3, included",
     1 : "In section 1, included",
     2 : "In section 3, included",
     3 : "In neither section 1 or 3, ommited (precipitation amount = 0)",
     4 : "In neither section 1 or 3, ommited (precipitation amount not available)"
}

class Group_iRixhVV(Group):
    
    def __init__(self, group: str, name: str):
        super().__init__(group, name)
        self._iR = Table_Indicator(self._extract_indicator(0, 1), "iR", TABLE_1819)
        self._ix = self._extract_indicator(1, 2)
        self._h = self._extract_indicator(2, 3)
        self._VV = self._extract_indicator(3, 5)
    
    def verify_indicators(self):
        self.verify_table_indicator(self._iR)

class Section_One(Section):
    
    def __init__(self, section: list):
        super().__init__(section)
        self._iRixhVV = Group_iRixhVV(self.section[0], "iRixhVV")
        self._iRixhVV.verify_indicators()
        self.copy_group_errors(self._iRixhVV)
    
    def __str__(self):
        return ".:SECTION ONE:.\n{}".format(self._iRixhVV)
        
        