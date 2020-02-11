
from synopy.synopy import Synoptic

# Leemos el archivo synops.txt
f = open('datos/synops.txt', 'r')
data = f.readlines()

for line in data:
    synoptic_report = Synoptic(line)
    
    print("Año del mensaje: {}/{:02d}".format(synoptic_report.date.year, synoptic_report.date.month))
    print("Tipo de estación: {}".format(synoptic_report.station_type))