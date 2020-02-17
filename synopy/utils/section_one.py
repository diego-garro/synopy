
from .templates import Group, Section

class Group_iRixhVV(Group):
    
    def __init__(self, group: str, name: str):
        super().__init__(group, name)
        self._iR = self._extract_indicator(0, 1)
        self._ix = self._extract_indicator(1, 2)
        self._h = self._extract_indicator(2, 3)
        self._VV = self._extract_indicator(3, 5)

class Section_One(Section):
    
    def __init__(self, section: list):
        super().__init__(section)
        self._iRixhVV = Group_iRixhVV(self.section[0], "iRixhVV")
    
    def __str__(self):
        return ".:SECTION ONE:.\n{}".format(self._iRixhVV)
        
        