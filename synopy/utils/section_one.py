
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

TABLE_1860 = {
    -2 : "Table 1860",
    -1 : "type of station operation and for present and past weather data",
     1 : "\nType of station: Manned.\nGroup 7wwW1W2 or 7wawaWa1Wa2: Included",
     2 : "\nType of station: Manned.\nGroup 7wwW1W2 or 7wawaWa1Wa2: Omitted (no significant phenomenon to report)",
     3 : "\nType of station: Manned.\nGroup 7wwW1W2 or 7wawaWa1Wa2: Omitted (no observation, data not available)",
     4 : "\nType of station: Automatic.\nGroup 7wwW1W2 or 7wawaWa1Wa2: Included using code tables 4677 and 4561",
     5 : "\nType of station: Automatic.\nGroup 7wwW1W2 or 7wawaWa1Wa2: Omitted (no significant phenomenon to report)",
     6 : "\nType of station: Automatic.\nGroup 7wwW1W2 or 7wawaWa1Wa2: Omitted (no observation, data not available)",
     7 : "\nType of station: Automatic.\nGroup 7wwW1W2 or 7wawaWa1Wa2: Included using code tables 4680 and 4531"
}

TABLE_1600 = {
    -2 : "Table 1600",
    -1 : "height above surface of the base of the lowest cloud seen",
     0 : "Feet: 0 - 100. Meters: 0 - 50",
     1 : "Feet: 100 - 300. Meters: 50 - 100",
     2 : "Feet: 300 - 600. Meters: 100 - 200",
     3 : "Feet: 600 - 900. Meters: 200 - 300",
     4 : "Feet: 900 - 1,900. Meters: 300 - 600",
     5 : "Feet: 1,900 - 3,200. Meters: 600 - 1,000",
     6 : "Feet: 3,200 - 4,900. Meters: 1,000 - 1,500",
     7 : "Feet: 4,900 - 6,500. Meters: 1,500 - 2,000",
     8 : "Feet: 3,200 - 4,900. Meters: 1,000 - 1,500",
     9 : "Feet: 8,000 or higher or no clouds. Meters: 2,500 or higher or no clouds",
   "/" : "Height of base of cloudsis not known"
}

TABLE_4377 = {
    -2 : "Table 4377",
    -1 : "horizontal visibility at the surface",
     0 : "<0.1 Km", 1 : "0.1 Km", 2 : "0.2 Km", 3 : "0.3 Km", 4 : "0.4 Km", 5 : "0.5 Km", 6 : "0.6 Km", 7 : "0.7 Km",
     8 : "0.8 Km", 9 : "0.9 Km", 10: "1.0 Km", 11 : "1.1 Km", 12 : "1.2 Km", 13 : "1.3 Km", 14 : "1.4 Km", 15 : "1.5 Km",
     16 : "1.6 Km", 17 : "1.7 Km", 18 : "1.8 Km", 19 : "1.9 Km", 20: "2.0 Km", 21 : "2.1 Km", 22 : "2.2 Km", 23 : "2.3 Km",
     24 : "2.4 Km", 25 : "2.5 Km", 26 : "2.6 Km", 27 : "2.7 Km", 28 : "2.8 Km", 29 : "2.9 Km", 30: "3.0 Km", 31 : "3.1 Km",
     32 : "3.2 Km", 33 : "3.3 Km", 34 : "3.4 Km", 35 : "3.5 Km", 36 : "3.6 Km", 37 : "3.7 Km", 38 : "3.8 Km", 39 : "3.9 Km",
     40 : "4.0 Km", 41 : "4.1 Km", 42 : "4.2 Km", 43 : "4.3 Km", 44 : "4.4 Km", 45 : "4.5 Km", 46 : "4.6 Km", 47 : "4.7 Km",
     48 : "4.8 Km", 49 : "4.9 Km", 50 : "5.0 Km", 56 : "6 Km", 57 : "7 Km", 58 : "8 Km", 59 : "9 Km", 60 : "10 Km", 61 : "11 Km",
     62 : "12 Km", 63 : "13 Km", 64 : "14 Km", 65 : "15 Km", 66 : "16 Km", 67 : "17 Km", 68 : "18 Km", 69 : "19 Km", 70 : "20 Km",
     71 : "21 Km", 72 : "22 Km", 73 : "23 Km", 74 : "24 Km", 75 : "25 Km", 76 : "26 Km", 77 : "27 Km", 78 : "28 Km", 79 : "29 Km",
     80 : "30 Km", 81 : "35 Km", 82 : "40 Km", 83 : "45 Km", 84 : "50 Km", 85 : "55 Km", 86 : "60 Km", 87 : "65 Km", 88 : "70 Km",
     89 : ">70 Km", 90 : "<0.05 Km", 91 : "0.05 Km", 92 : "0.2 Km", 93 : "0.5 Km", 94 : "1 Km", 95 : "2 Km", 96 : "4 Km", 97 : "10 Km",
     98 : "20 Km", 99 : ">=50 Km"
}

class Group_iRixhVV(Group):
    
    def __init__(self, group: str, name: str):
        super().__init__(group, name)
        self._iR = Table_Indicator(self._extract_indicator(0, 1), "iR", TABLE_1819)
        self._ix = Table_Indicator(self._extract_indicator(1, 2), "ix", TABLE_1860)
        self._h = Table_Indicator(self._extract_indicator(2, 3), "h", TABLE_1600)
        self._VV = Table_Indicator(self._extract_indicator(3, 5), "VV", TABLE_4377)
    
    def verify_indicators(self):
        self.verify_table_indicator(self._iR)
        self.verify_table_indicator(self._ix)
        self.verify_table_indicator(self._h)
        self.verify_table_indicator(self._VV)

class Section_One(Section):
    
    def __init__(self, section: list):
        super().__init__(section)
        self._iRixhVV = Group_iRixhVV(self.section[0], "iRixhVV")
        self._iRixhVV.verify_indicators()
        self.copy_group_errors(self._iRixhVV)
    
    def __str__(self):
        return ".:SECTION ONE:.\n{}".format(self._iRixhVV)
        
        