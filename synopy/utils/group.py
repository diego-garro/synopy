
ERRORS = {
    1 : "The group {} has more than five digits.",
    2 : "The group {} has less than five digits.",
    3 : "The group {} for {} is not found.",
    4 : "The indicator {} for {} is not in {}.",
}

class Group:
    
    errors = []
    _found = True
    _group_objetive = ''
    
    def __init__(self, group: str, name: str):
        self.group = group
        self.name = name
        self.length = len(group)
        if self.length > 5:
            self.errors.append(ERRORS[1].format(self.name))
        elif self.length < 5:
            self.errors.append(ERRORS[2].format(self.name))
        else:
            pass
    
    def _extract_indicator(self, start, end):
        return self.group[start:end]
    
    def _verify_group_indicator(self, indicator, value=1):
        indicator = int(indicator)
        if indicator != value:
            self._found = False
            self.errors.append(ERRORS[3].format(self.name, self._group_objetive))
            
    
    def _verify_indicator(self, indicator, indicator_name, indicator_objetive, table, values=1):
        indicator = int(indicator)
        if isinstance(values, list) or isinstance(values, tuple):
            if indicator not in values:
                self.errors.append(ERRORS[4].format(indicator_name, indicator_objetive, table))
        if isinstance(values, int):
            if indicator != values:
                self.errors.append(ERRORS[4].format(indicator_name, indicator_objetive, table))
    
    def __str__(self):
        return "Group name: {}.".format(self.name)

class Section:
    
    def __init__(self, section: list):
        self.section = section
        self.length = len(section)
        