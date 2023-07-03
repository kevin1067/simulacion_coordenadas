# simulacion_coordenadas
    Este es un proyecto de tesis de la universidad UTEC que tiene como objetivo simular las rutas de pedidos por distritos en una empresa retail de Perú. Se consideran 30 distritos de la región metropolitana de Lima y la provincia constitucional del Callao. La simulación considera una region cuadrada aproximada de cada distrito de manera que la coordenada aleatoria siempre se encuentre dentro del distrito a elegir.
# Requisitos previos
    * Tener instalado python
    * Tener instalado pip
# Paso 1: crear un entorno virtual el directorio
    abrir la terminal
    cd "directorio de trabajo"
    ejecutar python -m venv venv
# Paso 2: activar el entorno virtual de python
    Para Windows:
        ejecutar venv\Scripts\activate
    Para Mac/Linux:
        ejecutar source ./venv/bin/activate
# Paso 2: instalar las librerías necesarias para el funcionamiento
    Una vez activado el entorno virtual ejecutar lo siguiente en la terminal:
    Para Windows:
        pip install -r requirements.txt
    Para Mac/Linux:
        pip3 install -r requirements.txt
# Paso 4: Ejecutar el código
    En la terminal ejecutar lo siguiente:
        python main.py
        
El código tiene como salidas unos archivos CSV para que puedan ser leidos por un optimizador de rutas. 