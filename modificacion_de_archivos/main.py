# Desarrollado por Sergio Gonzalez


# La función procesa el archivo .txt más reciente en una carpeta, lo transforma, mueve el archivo .dat
# resultante a una carpeta procesada y mueve el archivo .txt original a una carpeta de memoria.

# :param carpeta: La carpeta/directorio donde se encuentran los archivos
# :return: La función `obtener_archivo_mas_reciente` devuelve la ruta del archivo más reciente con
# extensión `.txt` en la carpeta especificada. Si no hay archivos `.txt` en la carpeta, devuelve
# `Ninguno`.

import os
import time
from datetime import datetime
from transform import TransformarArchivo

def obtener_archivo_mas_reciente(carpeta):
    archivos = os.listdir(carpeta)
    archivos_completos = [os.path.join(carpeta, archivo) for archivo in archivos if archivo.endswith('.txt')] # Obtiene solo los archivos con extension .txt
    archivos_completos.sort(key=os.path.getmtime, reverse=True)
    return archivos_completos[0] if archivos_completos else None

def mover_archivo(origen, destino):
    os.rename(origen, destino)

if __name__ == '__main__':
    carpeta_nuevos = os.path.dirname(os.path.abspath(__file__)) # Carpeta donde se encuentra el archivo original
    carpeta_procesados = 'E:\TressPoll\ARCHIVOS' # Carpeta donde se guardaran los archivos procesados
    carpeta_mem = 'E:\TressPoll\PYTHON\mem' # Carpeta donde se guardaran los archivos que ya se procesaron

    archivo_reciente = obtener_archivo_mas_reciente(carpeta_nuevos)
    if archivo_reciente:
        print(f"Procesando archivo: {archivo_reciente}")
        archivo_transformado = TransformarArchivo(archivo_reciente)
        archivo_transformado.transformar_archivo()
        archivo_transformado.limpieza_archivo()
        archivo_transformado.transformar_a_punto_dat()

        nombre_archivo = os.path.basename(archivo_reciente)
        nombre_archivo_dat = nombre_archivo.replace('.txt', '.dat')

        # Obtener la fecha actual en el formato día_mes_año
        fecha_actual = datetime.now().strftime('%d_%m_%Y')

        # Agregar la fecha al nombre del archivo
        nombre_archivo_con_fecha = f"{nombre_archivo}_{fecha_actual}"

        # Mover archivo .dat a la carpeta de procesados
        destino_dat = os.path.join(carpeta_procesados, nombre_archivo_dat)
        mover_archivo(archivo_reciente.replace('.txt', '.dat'), destino_dat)

        # Mover archivo .txt a la carpeta mem con la fecha en el nombre
        destino_txt = os.path.join(carpeta_mem, nombre_archivo_con_fecha)
        mover_archivo(archivo_reciente, destino_txt)

        print("Archivo procesado y movido correctamente.")
