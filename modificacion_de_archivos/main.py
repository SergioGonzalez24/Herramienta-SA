import os
import time
from datetime import datetime
from transform import TransformarArchivo

def obtener_archivo_mas_reciente(carpeta):
    archivos = os.listdir(carpeta)
    archivos_completos = [os.path.join(carpeta, archivo) for archivo in archivos]
    archivos_completos.sort(key=os.path.getmtime, reverse=True)
    return archivos_completos[0] if archivos_completos else None

def mover_archivo(origen, destino):
    os.rename(origen, destino)

if __name__ == '__main__':
    carpeta_nuevos = 'nuevos'
    carpeta_procesados = 'procesados'
    carpeta_mem = 'mem'

    while True:
        archivo_reciente = obtener_archivo_mas_reciente(carpeta_nuevos)
        if archivo_reciente:
            print(f"Procesando archivo: {archivo_reciente}")
            archivo_transformado = TransformarArchivo(archivo_reciente)
            archivo_transformado.transformar_archivo()
            archivo_transformado.limpieza_archivo()
            archivo_transformado.transformar_a_punto_dat()

            nombre_archivo = os.path.basename(archivo_reciente)
            nombre_archivo_dat = nombre_archivo.replace('.txt', '.dat')

            # Mover archivo .dat a la carpeta de procesados
            destino_dat = os.path.join(carpeta_procesados, nombre_archivo_dat)
            mover_archivo(archivo_reciente.replace('.txt', '.dat'), destino_dat)

            # Mover archivo .txt a la carpeta mem
            destino_txt = os.path.join(carpeta_mem, nombre_archivo)
            mover_archivo(archivo_reciente, destino_txt)

            print("Archivo procesado y movido correctamente.")

        # Esperar 5 minutos antes de verificar nuevamente y imprimir cada minuto que pasa
        print(f"Esperando 5 minutos para verificar nuevos archivos. {datetime.now()}")
        time.sleep(300) # 300 segundos = 5 minutos
        
