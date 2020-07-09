
from synopy.synopy import Synoptic

# Leemos el archivo synops.txt
f = open('datos/synops.txt', 'r')
data = f.readlines()

# mensaje = '202002172100 AAXX 17214 78774 32970 00725 10334 20194 39951 40043 57015 333 30/// 59015'
# synop = Synoptic(mensaje)
# print("ERRORES DE PRUEBA")
# print(synop.section_one.errors)

for line in data:
    print("###################################################################################")
    synoptic_report = Synoptic(line)
    
    print("Año del mensaje: {}/{:02d}".format(synoptic_report.date.year, synoptic_report.date.month))
    print("Tipo de estación: {}".format(synoptic_report.station_type))
    print("Nombre de la estación: {}".format(synoptic_report.station_name))
    print("Unidades del viento: {}".format(synoptic_report.wind_units))
    #print(synoptic_report.report)
    print("\nSection One: {}".format(synoptic_report.section_one))
    print("\nSection Two: {}".format(synoptic_report.section_two))
    print("\nSection Three: {}".format(synoptic_report.section_three))
    print("\nSection Four: {}".format(synoptic_report.section_four))
    print("Errores sección 1: {}".format(synoptic_report.section_one.errors))
    print("Errores sección 2: {}".format(synoptic_report.section_two.errors))
    print("Errores del sinóptico: {}".format(synoptic_report.errors))
    print("###################################################################################")