from simulacion import simulacion_coordenadas
from utils import*
def exportarSimulacion(simulacion_coordenadas): # !NO MODIFICAR ESTE CODIGO!
    ruta1=simulacion_coordenadas[0]
    ruta2=simulacion_coordenadas[1]
    ruta3=simulacion_coordenadas[2]
    fr1=formatearRuta(ruta1)
    fr2=formatearRuta(ruta2)
    fr3=formatearRuta(ruta3)
    exportarJSON(fr1,"ruta1")
    exportarJSON(fr2,"ruta2")
    exportarJSON(fr3,"ruta3")
    exportarCSV("ruta1.json",1)
    exportarCSV("ruta2.json",2)
    exportarCSV("ruta3.json",3)
exportarSimulacion(simulacion_coordenadas) #cada vez que se ejecuta el valor de las rutas cambia dado que es aleatorio
# TODO : ejecutar el codigo las veces que sea requerido para llegar al numero de muestras(374)
#exportarJSON(fr1,"ruta1")
#exportarCSV("ruta1.json")
