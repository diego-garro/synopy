
from .group import Group, Section

class Group_iRixhVV(Group):
    
    def __init__(self, group: str, name: str):
        super().__init__(group, name)

class Section_One(Section):
    
    def __init__(self, section: list):
        super().__init__(section)
        self._iRixhVV = Group_iRixhVV(self.section[0], "iRixhVV")
    
    def __str__(self):
        return ".:SECTION ONE:.\n{}".format(self._iRixhVV)
        
        