
from .templates import Group, Section, Group_Indicator, Table_Indicator, Value_Indicator

ERRORS = {
    1 : "Indicator {} for {} group, only can take 0 or 1 as value.",
    2 : "Indicator {} for {} can't be 000.",
    3 : "Indicator {} indicates precipitation data will be included, but group {} not included.",
    4 : "Indicator {} indicates not precipitation data will be included, but group {} included.",
    5 : "Indicator {} indicates no clouds over the station, but group {} included.",
    6 : "Indicator {} indicates clouds over the station, but group {} not included."
}

TABLE_1819 = {
    -2 : "Table 1819",
    -1 : "inclusion or omission of precipitacion data",
     0 : "Precipitation data are reported: In sections 1 and 3.\nGroup 6RRRtR: Included.",
     1 : "Precipitation data are reported: In section 1.\nGroup 6RRRtR: Included.",
     2 : "Precipitation data are reported: In section 3.\nGroup 6RRRtR: Included.",
     3 : "Precipitation data are reported: In neither section 1 or 3.\nGroup 6RRRtR: Ommited (precipitation amount = 0).",
     4 : "Precipitation data are reported: In neither section 1 or 3.\nGroup 6RRRtR: Ommited (precipitation amount not available)."
}

TABLE_1860 = {
    -2 : "Table 1860",
    -1 : "type of station operation and for present and past weather data",
     1 : "Type of station: Manned.\nGroup 7wwW1W2 or 7wawaWa1Wa2: Included.",
     2 : "Type of station: Manned.\nGroup 7wwW1W2 or 7wawaWa1Wa2: Omitted (no significant phenomenon to report).",
     3 : "Type of station: Manned.\nGroup 7wwW1W2 or 7wawaWa1Wa2: Omitted (no observation, data not available).",
     4 : "Type of station: Automatic.\nGroup 7wwW1W2 or 7wawaWa1Wa2: Included using code tables 4677 and 4561.",
     5 : "Type of station: Automatic.\nGroup 7wwW1W2 or 7wawaWa1Wa2: Omitted (no significant phenomenon to report).",
     6 : "Type of station: Automatic.\nGroup 7wwW1W2 or 7wawaWa1Wa2: Omitted (no observation, data not available).",
     7 : "Type of station: Automatic.\nGroup 7wwW1W2 or 7wawaWa1Wa2: Included using code tables 4680 and 4531."
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
        super().__init__(group, name, "Precipitation inclusion/exclusion / Type operation / Cloud height / Visibility Group")
        self._iR = Table_Indicator(self._extract_indicator(0, 1), "iR", TABLE_1819)
        self._ix = Table_Indicator(self._extract_indicator(1, 2), "ix", TABLE_1860)
        self._h = Table_Indicator(self._extract_indicator(2, 3), "h", TABLE_1600)
        self._VV = Table_Indicator(self._extract_indicator(3, 5), "VV", TABLE_4377)
        self._save_indicators(self._iR)
    
    def verify_indicators(self):
        self.verify_table_indicator(self._iR)
        self.verify_table_indicator(self._ix)
        self.verify_table_indicator(self._h)
        self.verify_table_indicator(self._VV)
    
    def _show_characteristics(self):
        characteristics = [".:{}:.".format(self._group_objective)]
        characteristics.append("\n{}".format(self._iR.__str__()))
        characteristics.append("\n{}".format(self._ix.__str__()))
        characteristics.append("\nCloud base height: {}".format(self._h.__str__()))
        characteristics.append("\nVisibility: {}".format(self._VV.__str__()))
        return ''.join(characteristics)

TABLE_2700 = {
    -2 : "Table 2700",
    -1 : "amount of cloud cover",
     0 : "Cloud amount (oktas): 0",
     1 : "Cloud amount (oktas): 1/8 or less, not zero",
     2 : "Cloud amount (oktas): 2/8",
     3 : "Cloud amount (oktas): 3/8",
     4 : "Cloud amount (oktas): 4/8",
     5 : "Cloud amount (oktas): 5/8",
     6 : "Cloud amount (oktas): 6/8",
     7 : "Cloud amount (oktas): 7/8 or more, but not 8/8",
     8 : "Cloud amount (oktas): 8/8",
     9 : "Cloud amount (oktas): Sky obscured, or cannot be estimated"
}

TABLE_0877 = {
    -2 : "Table 0877",
    -1 : "true directions, in tens of degrees",
     0 : "Calm, no motion or no waves",
     1 : "5°-14°", 2 : "15°-24°", 3 : "25°-34°", 4 : "35°-44°", 5 : "45°-54°", 6 : "55°-64°", 7 : "65°-74°",
     8 : "75°-84°", 9 : "85°-94°", 10 : "95°-104°", 11 : "105°-114°", 12 : "115°-124°", 13 : "125°-134°",
     14 : "135°-144°", 15 : "145°-154°", 16 : "155°-164°", 17 : "165°-174°", 18 : "175°-184°", 19 : "185°-194°",
     20 : "195°-204°", 21 : "205°-214°", 22 : "215°-224°", 23 : "225°-234°", 24 : "235°-244°", 25 : "245°-254°",
     26 : "255°-264°", 27 : "265°-274°", 28 : "275°-284°", 29 : "285°-294°", 30 : "295°-304°", 31 : "305°-314°",
     32 : "315°-324°", 33 : "325°-334°", 34 : "335°-344°", 35 : "345°-354°", 36 : "355°-4°",
     99 : "Variable or all directions, or unknown, or waves confused, direction indeterminate"
}

class Group_Nddff(Group):
    
    def __init__(self, group: str, name: str, wind_units: str):
        super().__init__(group, name, "Total Cloud Cover and Wind Group")
        self.wind_units = self._set_wind_units(wind_units)
        self._N = Table_Indicator(self._extract_indicator(0, 1), "N", TABLE_2700)
        self._dd = Table_Indicator(self._extract_indicator(1, 3), "dd", TABLE_0877)
        self._ff = Value_Indicator(self._extract_indicator(3, 5), "ff", "wind speed")
        self._save_indicators(self._N, self._dd, self._ff)
    
    def _set_wind_units(self, wind_units: str):
        if wind_units == "0" or wind_units == "1":
            return "meters per second"
        elif wind_units == "3" or wind_units == "4":
            return "knots"
        else:
            return "unknown"
    
    def verify_indicators(self):
        self.verify_table_indicator(self._N)
        self.verify_table_indicator(self._dd)
        self.verify_value_indicator(self._ff)

    def _show_characteristics(self):
        characteristics = [".:{}:.".format(self._group_objective)]
        characteristics.append("\n{}".format(self._N.__str__()))
        characteristics.append("\nWind direction: {}".format(self._dd.__str__()))
        if self._ff.indicator == 99:
            characteristics.append("\nWind speed: 99 {} or more".format(self.wind_units))
        else:
            characteristics.append("\nWind speed: {} {}".format(self._ff.__str__(), self.wind_units))
        return ''.join(characteristics)

class Group_00fff(Group_Nddff):
    
    def __init__(self, group: str, name: str, wind_units: str):
        super().__init__(group, name, wind_units)
        self._group_objective = "Dew Point Temperature Group"
        self.group_indicator = Group_Indicator(self._extract_indicator(0, 2), "00")
        self._fff = Value_Indicator(self._extract_indicator(2, 5), "fff", "wind speed")
    
    def verify_indicators(self):
        self.verify_group_indicator(value=0)
        self.verify_value_indicator(self._fff)
    
    def _show_characteristics(self):
        return "Wind speed: {} {}".format(self._fff.indicator, self.wind_units)

class Group_1snTTT(Group):
    
    def __init__(self, group: str, name: str):
        super().__init__(group, name, "Air Temperature Group")
        self.group_indicator = Group_Indicator(self._extract_indicator(0, 1), "1")
        self._sn = Value_Indicator(self._extract_indicator(1, 2), "sn", "sign of the temperature")
        self._TTT = Value_Indicator(self._extract_indicator(2, 5), "TTT", "air temperature in tenths of degrees Celcius")
    
    def verify_indicators(self):
        self.verify_group_indicator()
        if self.found:
            self.verify_value_indicator(self._sn)
            self.verify_value_indicator(self._TTT)
            if self._sn.indicator > 1:
                self._errors.append(ERRORS[1].format(self._sn.name, self.name))
    
    def _show_characteristics(self):
        characteristics = [".:{}:.".format(self._group_objective)]
        if self._sn.indicator == 0:
            characteristics.append("\nAir temperature: {:.1f}°C".format(self._TTT.indicator / 10))
        elif self._sn.indicator == 1:
            characteristics.append("\nAir temperature: -{:.1f}°C".format(self._TTT.indicator / 10))
        else:
            characteristics.append("\nAir temperature: {:.1f}°C, sign not valid".format(self._TTT.indicator / 10))
        return ''.join(characteristics)

class Group_2snTdTdTd(Group):
    
    def __init__(self, group: str, name: str):
        super().__init__(group, name, "Dew Point Temperature Group")
        self.group_indicator = Group_Indicator(self._extract_indicator(0, 1), "2")
        self._sn = Value_Indicator(self._extract_indicator(1, 2), "sn", "sign of the dew point temperature")
        self._TdTdTd = Value_Indicator(self._extract_indicator(2, 5), "TdTdTd", "dew point temperature in tenths of degrees Celcius")
    
    def verify_indicators(self):
        self.verify_group_indicator(value=2)
        if self.found:
            self.verify_value_indicator(self._sn)
            self.verify_value_indicator(self._TdTdTd)
            if self._sn.indicator > 1:
                self._errors.append(ERRORS[1].format(self._sn.name, self.name))
    
    def _show_characteristics(self):
        characteristics = [".:{}:.".format(self._group_objective)]
        if self._sn.indicator == 0:
            characteristics.append("\nDew Point temperature: {:.1f}°C".format(self._TdTdTd.indicator / 10))
        elif self._sn.indicator == 1:
            characteristics.append("\nDew Point temperature: -{:.1f}°C".format(self._TdTdTd.indicator / 10))
        else:
            characteristics.append("\nDew Point temperature: {:.1f}°C, sign not valid".format(self._TdTdTd.indicator / 10))
        return ''.join(characteristics)

class Group_3PoPoPoPo(Group):
    
    def __init__(self, group: str, name: str):
        super().__init__(group, name, "Station Pressure Group")
        self.group_indicator = Group_Indicator(self._extract_indicator(0, 1), "3")
        self._PoPoPoPo = Value_Indicator(self._extract_indicator(1, 5), "PoPoPoPo", "pressure at station level, in tenths of a hectopascal")
    
    def verify_indicators(self):
        self.verify_group_indicator(value=3)
        if self.found:
            self.verify_value_indicator(self._PoPoPoPo)
    
    def _show_characteristics(self):
        characteristics = [".:{}:.".format(self._group_objective)]
        if self._PoPoPoPo.indicator < 150:
            characteristics.append("\nPressure at station level: {:.1f} hPa".format(self._PoPoPoPo.indicator / 10 + 1000))
        else:
            characteristics.append("\nPressure at station level: {:.1f} hPa".format(self._PoPoPoPo.indicator / 10))
        return ''.join(characteristics)

class Group_4PPPP(Group):
    
    def __init__(self, group: str, name: str):
        super().__init__(group, name, "Sea Level Pressure Group")
        self.group_indicator = Group_Indicator(self._extract_indicator(0, 1), "4")
        self._PPPP = Value_Indicator(self._extract_indicator(1, 5), "PPPP", "sea level pressure, in tenths of a hectopascal")
    
    def verify_indicators(self):
        self.verify_group_indicator(value=4)
        if self.found:
            self.verify_value_indicator(self._PPPP)
    
    def _show_characteristics(self):
        characteristics = [".:{}:.".format(self._group_objective)]
        if self._PPPP.indicator < 150:
            characteristics.append("\nSea level pressure: {:.1f} hPa".format(self._PPPP.indicator / 10 + 1000))
        else:
            characteristics.append("\nSea level pressure: {:.1f} hPa".format(self._PPPP.indicator / 10))
        return ''.join(characteristics)

TABLE_0200 = {
    -2 : "Table 0200",
    -1 : "characteristics of pressure tendency",
     0 : "Increasing, then decreasing; atmospheric pressure the same or higher tha 3 hours ago",
     1 : "Increasing, then steady; or increasing, then increasing more slowly",
     2 : "Increasing (stadily or unsteadily)",
     3 : "Dedreasing or steady, then increasing; or increasing, then increasing more rapidly",
     4 : "Steady, the atmospheric pressure the same than 3 hours ago",
     5 : "Decreasing, then increasing; atmospheric pressure the same or lower than 3 hours ago",
     6 : "Decreasing, then steady; or decreasing, then decreasing more slowly",
     7 : "Decreasing (steadily or unsteadily)",
     8 : "Steady or incresing, then decreasing; or decreasing, then decreasing more rapidly"
}

class Group_5appp(Group):
    
    def __init__(self, group: str, name: str):
        super().__init__(group, name, "3-Hour Pressure Tendency Group")
        self.group_indicator = Group_Indicator(self._extract_indicator(0, 1), "5")
        self._a = Table_Indicator(self._extract_indicator(1, 2), "a", TABLE_0200)
        self._ppp = Value_Indicator(self._extract_indicator(2, 5), "ppp", "actual change in the pressure")
    
    def verify_indicators(self):
        self.verify_group_indicator(value=5)
        if self.found:
            self.verify_table_indicator(self._a)
            self.verify_value_indicator(self._ppp)
    
    def _show_characteristics(self):
        characteristics = [".:{}:.".format(self._group_objective)]
        characteristics.append("\n{}: {}".format(TABLE_0200[-1].capitalize(), self._a.__str__()))
        if self._a.indicator > 4:
            characteristics.append("\nChange: -{:.1f}".format(self._ppp.indicator / 10))
        else:
            characteristics.append("\nChange: {:.1f}".format(self._ppp.indicator / 10))
        return ''.join(characteristics)

TABLE_4019 = {
    -2 : "Table 4019",
    -1 : "duration of period of precipitation",
     1 : "6 hours preceding time of observation",
     2 : "12 hours preceding time of observation",
     3 : "18 hours preceding time of observation",
     4 : "24 hours preceding time of observation",
     5 : "1 hour preceding time of observation",
     6 : "2 hours preceding time of observation",
     7 : "3 hours preceding time of observation",
     8 : "9 hours preceding time of observation",
     9 : "15 hours preceding time of observation",
}

class Group_6RRRtR(Group):
    
    def __init__(self, group: str, name: str):
        super().__init__(group, name, "Amount of Precipitation Group", requared=False)
        self.group_indicator = Group_Indicator(self._extract_indicator(0, 1), "6")
        self._RRR = Value_Indicator(self._extract_indicator(1, 4), "RRR",
                                    "total amount of precipitation fallen during the period preceding the observation")
        self._tR = Table_Indicator(self._extract_indicator(4, 5), "tR", TABLE_4019)
    
    def verify_indicators(self):
        self.verify_group_indicator(value=6)
        if self.found:
            self.verify_value_indicator(self._RRR)
            if self._RRR.indicator == 0:
                self._errors.append(ERRORS[2].format(self._RRR.name, self._RRR.objective))
            self.verify_table_indicator(self._tR)
    
    def _show_characteristics(self):
        characteristics = [".:{}:.".format(self._group_objective)]
        if self._RRR.indicator < 990:
            characteristics.append("\nAmount of precipitation: {} mm, {}".format(self._RRR.indicator, self._tR.__str__()))
        elif self._RRR.indicator > 990:
            characteristics.append("\nAmount of precipitation: {:.1f} mm, {}".format((self._RRR.indicator - 990) / 10, self._tR.__str__()))
        else:
            characteristics.append("\nAmount of precipitation: Trace, {}".format(self._tR.__str__()))
        return ''.join(characteristics)

TABLE_4561 = {
    -2 : "Table 4561",
    -1 : "past weather",
     0 : "Cloud covering 1/2 or less of the sky throughout the appropriate period",
     1 : "Cloud covering more than 1/2 of the sky during part of the appropriate period and covering 1/2 or less during part of the period",
     2 : "Cloud covering more than 1/2 of the sky throughout the appropriate period",
     3 : "Sandstorm, duststorm, or blowing snow",
     4 : "Fog or ice fog or thick haze",
     5 : "Drizzle",
     6 : "Rain",
     7 : "Snow, or rain and snow mixed",
     8 : "Shower(s)",
     9 : "Thunderstorm(s) with or without precipitation"
}

COMMON_TABLE_4677 = {
    10 : """shallow fog or ice fog at the station, whether on land or sea, not deeper
than about  2 meters on land or 10 meters at sea""",
    18 : """at or within sight of the station during the preceding hour or at the time
of obervation""",
    20 : "not falling as shower(s)",
    30 : "Slight or moderate duststorm or sandstorm",
    33 : "Severe duststorm or sandstorm",
    36 : "generally low (below eye level)",
    38 : "generally high (above eye level)",
    42 : "Fog or ice fog, sky visible",
    43 : "Fog or ice fog, sky invisible",
    50 : "Drizzle, not freezing, intermittent",
    51 : "Drizzle, not freezing, continuous",
    60 : "Rain, not freezing, intermittent",
    61 : "Rain, not freezing, continuous",
    70 : "Intermittent fall or snowflakes",
    71 : "Continuous fall of snowflakes",
    87 : "Shower(s) of snow pellets or small hail, with or without rain or rain and snow mixed",
    89 : "Shower(s) of hail, with or without rain or rain and snow mixed, not associate with thunder",
    91 : "thunderstorm during the preceding hour but not at time of observation"
}

TABLE_4677 = {
    # ww = 00 - 49 No precipitation at the station at the time of observation
    # ww = 00 - 19 No precipitation, fog, ice fog (except for 11 and 12), duststorm, sandstorm, drifting
    #              or blowing snow at the station at the time of observation or, except for 09 and 17,
    #              during the preceding hour.
    -2 : "Table 4677",
    -1 : "present wheather reported from a manned weather station",
     0 : "Cloud development not observed or not observable",
     1 : "Clouds generally dissolving or becoming less developed",
     2 : "State of the sky on the whole unchanged",
     3 : "Clouds generally forming or developing",
     4 : """Visibility reduced by smoke, e. g. veldt or forest fires, industrial smokes or
volcanic ashes""",
     5 : "Haze",
     6 : """Widespread dust in suspension in the air, not raised by wind at or near the
station at the time of observation""",
     7 : """Dust or sand raised by wind at or near the station at the time of observation,
but no well-developed dust whirl(s) or sand whirl(s), and no duststorm or
sandstorm seen; or, in the case of ships, blowing spray at the station""",
     8 : """Well-developed dust whirl(s) or sand whirl(s) seen at or near the station
during the preceding hour or at the time of observation, but no duststorm or sandstorm""",
     9 : """Duststorm or sandstorm within sight at the time of obervation, or at the
station during the preceding hour""",
    10 : f"Mist {COMMON_TABLE_4677[10]}",
    11 : f"Patches {COMMON_TABLE_4677[10]}",
    12 : f"More or less continuous {COMMON_TABLE_4677[10]}",
    13 : "Lightning visible, no thunder heard",
    14 : "Precipitation within sight, not reaching the ground or surface of the sea",
    15 : """Precipitation within sight, reaching the ground or the surface of the sea, but
distant, i.e. estimated to be more than 5 km from the station""",
    16 : """Precipitation within sight, reaching the ground or the surface of the sea, near to,
but not at the station""",
    17 : "Thunderstorm, but no precipitation at the time of observation",
    18 : f"Squalls {COMMON_TABLE_4677[18]}",
    19 : f"Funnel cloud(s), tornado cloud or {COMMON_TABLE_4677[18]}",
    # ww = 20 - 29 Precipitation, fog, ice fog or thinderstorm at the station during the preceding hour
    #              but not at the time of observation
    20 : f"Drizzle (not freezing)vor snow grains {COMMON_TABLE_4677[20]}",
    21 : f"Rain (not freezing {COMMON_TABLE_4677[20]}",
    22 : f"Snow {COMMON_TABLE_4677[20]}",
    23 : f"Rain and snow or ice pellets {COMMON_TABLE_4677[20]}",
    24 : f"Freezing drizzle or freezing rain {COMMON_TABLE_4677[20]}",
    25 : f"Shower(s) of rain {COMMON_TABLE_4677[20]}",
    26 : f"Shower(s) of snow, or of rain and snow {COMMON_TABLE_4677[20]}",
    27 : f"Shower(s) of hail, or of rain and hail {COMMON_TABLE_4677[20]}",
    28 : f"Fog or ice fog {COMMON_TABLE_4677[20]}",
    29 : f"Thunderstorm (with or without precipitation) {COMMON_TABLE_4677[20]}",
    # ww = 30 - 39 Duststorm, sandstorm, drifting or blowing snow
    30 : f"{COMMON_TABLE_4677[30]} has decreased during the time preceding hour",
    31 : f"{COMMON_TABLE_4677[30]} no appreciable change during the preceding hour",
    32 : f"{COMMON_TABLE_4677[30]} has begun or has increased during the preceding hour",
    33 : f"{COMMON_TABLE_4677[33]} has decreased during the time preceding hour",
    34 : f"{COMMON_TABLE_4677[33]} no appreciable change during the preceding hour",
    35 : f"{COMMON_TABLE_4677[33]} has begun or has increased during the preceding hour",
    36 : f"Slight or moderate drifting snow {COMMON_TABLE_4677[36]}",
    37 : f"Heavy drifting snow {COMMON_TABLE_4677[36]}",
    38 : f"Slight or moderate drifting snow {COMMON_TABLE_4677[38]}",
    39 : f"Heavy drifting snow {COMMON_TABLE_4677[38]}",
    # ww = 40 - 49 Fog or ice fog at the time of observation
    40 : """Fog or ice fog at a distance at the time of observation, but not at the station
during the preceding hour, the fog or ice fog extending to a level above that of
the oberver""",
    41 : "Fog or ice fog in patches",
    42 : f"{COMMON_TABLE_4677[42]}, has become thinner during the preceding hour",
    43 : f"{COMMON_TABLE_4677[43]}, has become thinner during the preceding hour",
    44 : f"{COMMON_TABLE_4677[42]}, no appreciable change during the preceding hour",
    45 : f"{COMMON_TABLE_4677[43]}, no appreciable change during the preceding hour",
    46 : f"{COMMON_TABLE_4677[42]}, has begun or has become thicker during the preceding hour",
    47 : f"{COMMON_TABLE_4677[43]}, has begun or has become thicker during the preceding hour",
    48 : "Fog, depositing rime, sky visible",
    49 : "Fog, depositing rime, sky invisible",
    # ww = 50 - 99 Precipitation at the station at the time of observation
    # ww = 50 - 59 Drizzle
    50 : f"{COMMON_TABLE_4677[50]} slight at time of observation",
    51 : f"{COMMON_TABLE_4677[51]} slight at time of observation",
    52 : f"{COMMON_TABLE_4677[50]} moderate at time of observation",
    53 : f"{COMMON_TABLE_4677[51]} moderate at time of observation",
    54 : f"{COMMON_TABLE_4677[50]} heavy (dense) at time of observation",
    55 : f"{COMMON_TABLE_4677[51]} heavy (dense) at time of observation",
    56 : "Drizzle, freezing, slight",
    57 : "Drizzle, freezing, moderate or heavy (dense)",
    58 : "Drizzle and rain, slight",
    59 : "Drizzle and rain, moderate or heavy (dense)",
    # ww = 60 - 69 Rain
    60 : f"{COMMON_TABLE_4677[60]} slight at time of obervation",
    61 : f"{COMMON_TABLE_4677[61]} slight at time of obervation",
    62 : f"{COMMON_TABLE_4677[60]} moderate at time of obervation",
    63 : f"{COMMON_TABLE_4677[61]} moderate at time of obervation",
    64 : f"{COMMON_TABLE_4677[60]} heavy at time of obervation",
    65 : f"{COMMON_TABLE_4677[61]} heavy at time of obervation",
    66 : "Rain, freezing, slight",
    67 : "Rain, freezing, moderate or heavy",
    68 : "Rain or drizzle and snow, slight",
    69 : "Rain or drizzle and snow, moderate or heavy",
    # ww = 70 - 79 Solid precipitation not in showers
    70 : f"{COMMON_TABLE_4677[70]} slight at time of obervation",
    71 : f"{COMMON_TABLE_4677[71]} slight at time of obervation",
    72 : f"{COMMON_TABLE_4677[70]} moderate at time of obervation",
    73 : f"{COMMON_TABLE_4677[71]} moderate at time of obervation",
    74 : f"{COMMON_TABLE_4677[70]} heavy at time of obervation",
    75 : f"{COMMON_TABLE_4677[71]} heavy at time of obervation",
    76 : "Diamond dust (with or without fog)",
    77 : "Snow grains (with or whitout fog)",
    78 : "Isolated star-like snow crystals (with or without fog)",
    79 : "Ice pellets",
    # ww = 80 - 99 Showery precipitation, or precipitation with current or recent thunderstorm
    80 : "Rain shower(s), slight",
    81 : "Rain shower(s), moderate or heavy",
    82 : "Rain shower(s), violent",
    83 : "Shower(s) of rain and snow mixed, slight",
    84 : "Shower(s) of rain and snow mixed, moderate or heavy",
    85 : "Snow shower(s), slight",
    86 : "Snow shower(s), moderate or heavy",
    87 : f"{COMMON_TABLE_4677[87]} slight",
    88 : f"{COMMON_TABLE_4677[87]} moderate or heavy",
    89 : f"{COMMON_TABLE_4677[89]} slight",
    90 : f"{COMMON_TABLE_4677[89]} moderate or heavy",
    91 : f"Slight rain at the time of observation, {COMMON_TABLE_4677[91]}",
    92 : f"Moderate or heavy rain at time of observation, {COMMON_TABLE_4677[91]}",
    93 : f"""Slight snow, or rain and snow mixed or hail at time of observation,
{COMMON_TABLE_4677[91]}""",
    94 : f"""Moderate or heavy snow, or rain and snow mixed or hail at time of observation,
{COMMON_TABLE_4677[91]}""",
    95 : """Thunderstorm, slight or moderate, without hail, but with rain and/or snow at
time of observation""",
    96 : "Thunderstorm, slight or moderate, with hail at time ob observation",
    97 : """Thunderstorm, heavy, without hail, but with rain and/or snow at time of
observation""",
    98 : "Thunderstorm combined with duststorm or sandstorm at time of observation",
    99 : "Thunderstorm, heavy, with hail at time of observation"
}

class Group_7wwW1W2(Group):
    
    def __init__(self, group: str, name: str):
        super().__init__(group, name,
                         "Present and Past Weather Group reported from a manned weather station",
                         requared=False)
        self.group_indicator = Group_Indicator(self._extract_indicator(0, 1), "7")
        self._ww = Table_Indicator(self._extract_indicator(1, 3), "ww", TABLE_4677)
        self._W1 = Table_Indicator(self._extract_indicator(3, 4), "W1", TABLE_4561)
        self._W2 = Table_Indicator(self._extract_indicator(4, 5), "W2", TABLE_4561)
    
    def verify_indicators(self):
        self.verify_group_indicator(value=7)
        if self.found:
            self.verify_table_indicator(self._ww)
            self.verify_table_indicator(self._W1)
            self.verify_table_indicator(self._W2)
    
    def _show_characteristics(self):
        characteristics = [".:{}:.".format(self._group_objective)]
        characteristics.append("\nPresent weather: {}".format(self._ww.__str__()))
        characteristics.append("\nPast weather 1: {}".format(self._W1.__str__()))
        characteristics.append("\nPast weather 2: {}".format(self._W2.__str__()))
        return ''.join(characteristics)

TABLE_0513 = {
    -2 : "Table 0513",
    -1 : "Clouds of the genera stratocumulus, stratus, cumulus and cumulonimbus",
     0 : "No CL clouds",
     1 : "Cumulus humilis or cumulus fractus other than of bad weather, or both",
     2 : """Cumulus mediocris or congestus, with or without cumulus of species fractus or humilis
or stratocumulus, all having their bases at the same level""",
     3 : "Cumulonimbus calvus, with or without cumulus, stratocumulus or stratus",
     4 : "Stratocumulus cumulogenitus",
     5 : "Stratocumulus other than stratocumulus cumulogenitus",
     6 : "Stratus nebulosus or stratus fractus other than or bad weather, or both",
     7 : """Stratus fractus or cumulus fractus of bad weather, or both (pannus), usually below
altostratus or nimbostratus""",
     8 : """Cumulus or stratocumulus other than stratocumulus cumulogenitus, with bases at
different levels""",
     9 : """Cumulonimbus capilatus (often with an anvil), with or without cumulonimbus calvus,
cumulus, stratocumulus, stratus or pannus""",
    "/": """CL clouds invisible owing to darkness, fog, blowing dust or sand, or other similar
phenomena"""
    # * "Bad weather" denotes the conditions which generally exists during precipitation and a short
    #   time before and after
}

TABLE_0515 = {
    -2 : "Table 0515",
    -1 : "Clouds of the genera altocumulus, altostratus and nimbostratus",
     0 : "No CM clouds",
     1 : "Altocumulus translucidus",
     2 : "Altocumulus opacus or nimbostratus",
     3 : "Altocumulus translucidus at a same level",
     4 : """Patches (often lenticular) of altocumulus translucidus, continuanly changing
and ocurring at one or more levels""",
     5 : """Altocumulus translucidus in bands, or one or more layers of altocumulus translucidus  or
opacus, progressively invading the sky; these altocumulus clouds generally thicken
as a whole""",
     6 : "Altocumulus cumulogenitus (or cumulonimbogenitus)",
     7 : """Altocumulus translucidus or opacus in two or more layers, or altocumulus opacus in a
single layer, not progressively invading the sky, or altocumulus with altostratus or
nimbostraus""",
     8 : "Altocumulus castellanus or floccus",
     9 : "Altocumulus of a chaotic sky, generally at several levels",
    "/": """CM clouds invisible owing to darkness, fog, blowing dust or sand, or other similar
phenomena, or because of continuous layer of lower clouds"""
}

TABLE_0509 = {
    -2 : "Table 0509",
    -1 : "Clouds of the genera cirrus, cirrucumulus and cirrustratus",
     0 : "No CH clouds",
     1 : "Cirrus fibratus, sometimes uncinus, not progressively invading the sky",
     2 : """Cirrus spissatus, in patches or entangled sheaves, which usually do not increase and
sometimes seem to be the remains of the upper part of cumulonimbus; or cirrus
castellanus or floccus""",
     3 : "Cirrus spissatus cumulonimbogenitus",
     4 : """Cirrus uncinos o fibratus, or both, progressively invading the sky, they generally
thicken as a whole""",
     5 : """Cirrus (often in bands) and cirrustratus, or cirrustratus alone, progressively invading the
sky; they generally thicken as a whole, but the continuous veil does not reach 45
degrees above the horizon""",
     6 : """Cirrus (often in bands) and cirrustratus, or cirrustratus alone, progressively invading the
sky; they generally thicken as a whole, the continuous veil extends more than 45
degrees above the horizon, without the sky being totally covered""",
     7 : "Cirrostratus covering the whole sky",
     8 : "Cirrostratus not progressively invading the sky and not entirely covering it",
     9 : "Cirrocumulus alone, or cirrocumulus predominant among the CH clouds",
    "/": """CH clouds invisible owing to darkness, fog, blowing dust or sand, or other similar
phenomena, or because of continuous layer of lower clouds"""
}

class Group_8NhCLCMCH(Group):
    
    def __init__(self, group: str, name: str):
        super().__init__(group, name, "Cloud Type Group", requared=False)
        self.group_indicator = Group_Indicator(self._extract_indicator(0, 1), "8")
        self._Nh = Table_Indicator(self._extract_indicator(1, 2), "Nh", TABLE_2700)
        self._CL = Table_Indicator(self._extract_indicator(2, 3), "CL", TABLE_0513)
        self._CM = Table_Indicator(self._extract_indicator(3, 4), "CM", TABLE_0515)
        self._CH = Table_Indicator(self._extract_indicator(4, 5), "CH", TABLE_0509)
    
    def verify_indicators(self):
        self.verify_group_indicator(value=8)
        if self.found:
            self.verify_table_indicator(self._Nh)
            self.verify_table_indicator(self._CL)
            self.verify_table_indicator(self._CM)
            self.verify_table_indicator(self._CH)
    
    def _show_characteristics(self):
        characteristics = [".:{}:.".format(self._group_objective)]
        characteristics.append("\nAmount of low clouds or all CM clouds: {}".format(self._Nh.__str__()))
        characteristics.append("\nCL type of clouds: {}".format(self._CL.__str__()))
        characteristics.append("\nCM type of clouds: {}".format(self._CM.__str__()))
        characteristics.append("\nCH type of clouds: {}".format(self._CH.__str__()))
        return ''.join(characteristics)

class Group_9GGgg(Group):
    
    def __init__(self, group: str, name: str):
        super().__init__(group, name, "Actual Time of Observation Group", requared=False)
        self.group_indicator = Group_Indicator(self._extract_indicator(0, 1), "9")
        self._GG = Value_Indicator(self._extract_indicator(1, 3), "GG", "hour of observation")
        self._gg = Value_Indicator(self._extract_indicator(3, 5), "gg", "minute of observation")
    
    def verify_indicators(self):
        self.verify_group_indicator(value=9)
        if self.found:
            self.verify_value_indicator(self._GG)
            self.verify_value_indicator(self._gg)
    
    def _show_characteristics(self):
        characteristics = [".:{}:.".format(self._group_objective)]
        characteristics.append("\nActual time: {:02d}:{:02d}Z".format(self._GG.indicator, self._gg.indicator))
        return ''.join(characteristics)

class Section_One(Section):
    
    def __init__(self, section: list, wind_units: str, index=2):
        super().__init__(section, index)
        self.wind_units = wind_units
        
        # Group iRixhVV
        self._iRixhVV = Group_iRixhVV(self.section[0], "iRixhVV")
        self._verify_indicators_and_copy_errors(self._iRixhVV)
        self.iR = self._iRixhVV.get_indicator("iR")
        self._include_group_to_groups(self._iRixhVV)
        
        #Group Nddff
        self._Nddff = Group_Nddff(self.section[1], "Nddff", self.wind_units)
        self._verify_indicators_and_copy_errors(self._Nddff)
        self.N = self._Nddff.get_indicator("N")
        self.ff = self._Nddff.get_indicator("ff")
        self._include_group_to_groups(self._Nddff)
        
        # Group 00fff
        if self.ff == 99:
            self._00fff = Group_00fff(self.section[self.group_index], "00fff", self.wind_units)
            self._verify_indicators_and_copy_errors(self._00fff)
            self._increment_group_index(self._00fff)
        else:
            self._00fff = ""
        
        # Group 1snTTT
        self._1snTTT = Group_1snTTT(self.section[self.group_index], "1snTTT")
        self._verify_indicators_and_copy_errors(self._1snTTT)
        self._increment_group_index(self._1snTTT)
    
        # Group 2snTdTdTd
        self._2snTdTdTd = Group_2snTdTdTd(self.section[self.group_index], "2snTdTdTd")
        self._verify_indicators_and_copy_errors(self._2snTdTdTd)
        self._increment_group_index(self._2snTdTdTd)
        
        # Group 3PoPoPoPo
        self._3PoPoPoPo = Group_3PoPoPoPo(self.section[self.group_index], "3PoPoPoPo")
        self._verify_indicators_and_copy_errors(self._3PoPoPoPo)
        self._increment_group_index(self._3PoPoPoPo)
        
        # Group 4PPPP
        self._4PPPP = Group_4PPPP(self.section[self.group_index], "4PPPP")
        self._verify_indicators_and_copy_errors(self._4PPPP)
        self._increment_group_index(self._4PPPP)
        
        # Group 5appp
        self._5appp = Group_5appp(self.section[self.group_index], "5appp")
        self._verify_indicators_and_copy_errors(self._5appp)
        self._increment_group_index(self._5appp)
        
        # Group 6RRRtR
        try:
            self._6RRRtR = Group_6RRRtR(self.section[self.group_index], "6RRRtR")
            self._verify_indicators_and_copy_errors(self._6RRRtR)
            self._increment_group_index(self._6RRRtR)
            if self.iR < 3 and not self._6RRRtR.found:
                self.errors.append(ERRORS[3].format("iR", self._6RRRtR.name))
            elif self.iR >= 3 and self._6RRRtR.found:
                self.errors.append(ERRORS[4].format("iR", self._6RRRtR.name))
            else:
                pass
        except IndexError:
            if self.iR < 3:
                self.errors.append(ERRORS[3].format("iR", "6RRRtR"))
        
        # Group 7wwW1W2
        try:
            self._7wwW1W2 = Group_7wwW1W2(self.section[self.group_index], "7wwW1W2")
            self._verify_indicators_and_copy_errors(self._7wwW1W2)
            self._increment_group_index(self._7wwW1W2)
            if self.iR < 3 and not self._7wwW1W2.found:
                self.errors.append(ERRORS[3].format("iR", self._7wwW1W2.name))
            elif self.iR >= 3 and self._7wwW1W2.found:
                self.errors.append(ERRORS[4].format("iR", self._7wwW1W2.name))
            else:
                pass
        except IndexError:
            if self.iR < 3:
                self.errors.append(ERRORS[3].format("iR", "7wwW1W2"))
        
        # Group 8NhCLCMCH
        try:
            self._8NhCLCMCH = Group_8NhCLCMCH(self.section[self.group_index], "8NhCLCMCH")
            self._verify_indicators_and_copy_errors(self._8NhCLCMCH)
            self._increment_group_index(self._8NhCLCMCH)
            if self.N == 0 and self._8NhCLCMCH.found:
                self.errors.append(ERRORS[5].format("N", self._8NhCLCMCH.name))
            elif self.N != 0 and not self._8NhCLCMCH:
                self.errors.append(ERRORS[6].format("N", self._8NhCLCMCH.name))
            else:
                pass
        except IndexError:
            if self.N != 0:
                self.errors.append(ERRORS[6].format("N", self._8NhCLCMCH.name))
        
        # Group 9GGgg
        try:
            self._9GGgg = Group_9GGgg(self.section[self.group_index], "9GGgg")
            self._verify_indicators_and_copy_errors(self._9GGgg)
            self._increment_group_index(self._9GGgg)
        except IndexError:
            pass