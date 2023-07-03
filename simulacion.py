import numpy as np
import random
from coordenadas import*
DISTRITOS = ["SAN BORJA",	"CARABAYLLO",	"SAN LUIS",	"LURÍN",	"RIMAC",	"LA VICTORIA",	"AGUSTINO",	"INDEPENDENCIA",	"BARRANCO",	"BREÑA",	"SMP",	"ATE",	"LINCE",	"VMT",	"CALLAO",	"LA MOLINA",	"SURQUILLO",	"LOS OLIVOS",	"MAGDALENA",	"SAN MIGUEL",	"SJM",	"VES",	"CERCADO",	"MIRAFLORES",	"SJL",	"CHORRILLOS",	"JESUS MARIA",	"PUEBLO LIBRE",	"SAN ISIDRO",	"COMAS",	"SURCO"]
PROBABILIDADES =[0.00060,	0.00119,	0.00120,	0.00240,	0.00361,	0.006010,	0.00721,	0.00962,	0.00962,	0.01202,	0.01442,	0.01683,	0.01803,	0.02404,	0.025240,	0.02825,	0.02825,	0.03005,	0.04627,	0.03426,	0.03426,	0.04026,	0.04447,	0.04447,	0.04507,	0.04567,	0.049880,	0.05228,	0.05289,	0.06370,	0.20793]
def crearDiccionarioCoordenadas(coordenadas_puntos_sur,coordenadas_puntos_norte,coordenadas_puntos_este,coordenadas_puntos_oeste,lista_distritos):
  coordenadas_distritos={}
  for i in range(len(coordenadas_puntos_sur)):
    coordenadas_distritos[lista_distritos[i]]={
        "punto_sur":{"lat":coordenadas_puntos_sur[i][0],"lon":coordenadas_puntos_sur[i][1]},
        "punto_norte":{"lat":coordenadas_puntos_norte[i][0],"lon":coordenadas_puntos_norte[i][1]},
        "punto_este":{"lat":coordenadas_puntos_este[i][0],"lon":coordenadas_puntos_este[i][1]},
        "punto_oeste":{"lat":coordenadas_puntos_oeste[i][0],"lon":coordenadas_puntos_oeste[i][1]}
    }
  return coordenadas_distritos
def ubicacionAleatoriaDistrito(distrito,diccionario_distrito):
  coordenada_aleatoria=[]
  coordenada_aleatoria.append({
      "distrito":distrito,
      "lat":random.uniform(diccionario_distrito[distrito]["punto_sur"]["lat"],diccionario_distrito[distrito]["punto_norte"]["lat"]),
      "lon":random.uniform(diccionario_distrito[distrito]["punto_oeste"]["lon"],diccionario_distrito[distrito]["punto_este"]["lon"]),})
  return coordenada_aleatoria
def redondeoPuntos(lista_puntos):
  nueva_lista=[]
  for m in lista_puntos:
    nueva_lista.append(round(m))
  return nueva_lista
def Simulacion_puntos(lista_distritos,lista_prob):
  media=11.8
  sd=1.86
  hoja_ruta=3
  rutas=[]
  puntos_por_ruta=np.random.normal(media, sd, size=hoja_ruta)#estos valores salen decimales
  puntos_por_ruta_enteros=redondeoPuntos(puntos_por_ruta)#valores de cantidad de puntos en enteros
  for _ in range(hoja_ruta):
    arr_aux=[]
    rutas.append(arr_aux)
  for i in range(len(puntos_por_ruta_enteros)): #[12,10,9]
    ruta_distritos=0
    for j in range(puntos_por_ruta_enteros[i]): #cuando j = 12,10,...
      ruta_distritos=np.random.choice(lista_distritos, size=j, p=lista_prob)
    rutas[i].extend(ruta_distritos)
   # rutas.extend(ruta)
  return rutas
def Simulacion_puntos_coordenadas(lista_distritos,lista_prob,lista_coordenadas):
  ruta_aleatoria=Simulacion_puntos(lista_distritos,lista_prob)
  coordenadas_simuladas=[]
  for _ in range(len(ruta_aleatoria)):
    arr_aux=[]
    coordenadas_simuladas.append(arr_aux)
  for i in range(len(ruta_aleatoria)):
    for j in range(len(ruta_aleatoria[i])):
      coordenadas_simuladas[i].append(ubicacionAleatoriaDistrito(ruta_aleatoria[i][j],lista_coordenadas))

  return coordenadas_simuladas
limites_coordenadas_distritos=crearDiccionarioCoordenadas(COORDENADAS_PUNTO_SUR,COORDENADAS_PUNTO_NORTE,COORDENADAS_PUNTO_ESTE,COORDENADAS_PUNTO_OESTE,DISTRITOS)
simulacion_coordenadas=Simulacion_puntos_coordenadas(DISTRITOS,PROBABILIDADES,limites_coordenadas_distritos)
