import json,pandas as pd
def formatearRuta(ruta):
    formato=[]
    for i in range(len(ruta)):
        formato.append(ruta[i][0])
    return formato
def exportarJSON(ruta_formateada,nombre):
    # Exportar a archivo JSON
    json_file=nombre+".json"
    with open(json_file, "w") as archivo:
        json.dump(ruta_formateada, archivo)
        print("Archivo JSON exportado con todos los valores.")

def exportarCSV(json_file,numero_ruta):
    # Cargar el archivo JSON
    with open(json_file, "r") as archivo:
        data = json.load(archivo)
    # Convertir el JSON a un DataFrame de pandas
    df = pd.DataFrame(data)
    # Exportar el DataFrame a un archivo CSV
    filename="ruta"+str(numero_ruta)+".csv"
    df.to_csv(filename, index=False)
    print("Archivo CSV exportado exitosamente.")