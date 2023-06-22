import os
import chardet

class TransformarArchivo:
    def __init__(self, archivo_txt):
        self.archivo_txt = archivo_txt
    
    def verificar_archivo(self):
        return os.path.isfile(self.archivo_txt)
    
    def verificar_codificacion(self):
        with open(self.archivo_txt, 'rb') as file:
            raw_data = file.read()
            result = chardet.detect(raw_data)
            encoding = result['encoding']
            return encoding
        
    def leer_archivo(self, encoding):
        with open(self.archivo_txt, 'r', encoding=encoding) as archivo:
            contenido = archivo.read()
        return contenido
    
    def transformar_archivo(self):
        encoding = self.verificar_codificacion()
        contenido = self.leer_archivo(encoding)
        
        with open(self.archivo_txt, 'w', encoding='utf-8') as archivo:
            archivo.write(contenido)
            
    def eliminar_valores_null(self):
        with open(self.archivo_txt, 'r', encoding='utf-8') as archivo:
            lineas = archivo.readlines()
        
        with open(self.archivo_txt, 'w', encoding='utf-8') as archivo:
            for linea in lineas:
                if linea.strip() != 'NULL':
                    archivo.write(linea)
                    
    def eliminar_lineas_en_blanco(self):
        with open(self.archivo_txt, 'r', encoding='utf-8') as archivo:
            lineas = archivo.readlines()
        
        with open(self.archivo_txt, 'w', encoding='utf-8') as archivo:
            for linea in lineas:
                if linea.strip():
                    archivo.write(linea)
                    
    def mantener_valores_importantes(self):
        with open(self.archivo_txt, 'r', encoding='utf-8') as archivo:
            lineas = archivo.readlines()
        
        with open(self.archivo_txt, 'w', encoding='utf-8') as archivo:
            # Guarda solo las lineas que empiezen con 0000000000@
            for linea in lineas:
                if linea.strip().startswith('0000000000@'):
                    archivo.write(linea)
                    
    def limpieza_archivo(self):
        self.eliminar_lineas_en_blanco()
        self.eliminar_valores_null()
        self.mantener_valores_importantes()
        
    def transformar_a_punto_dat(self):
        # genera una copia del archivo con extension .dat
        with open(self.archivo_txt, 'r', encoding='utf-8') as archivo:
            lineas = archivo.readlines()
            
        with open(self.archivo_txt.replace('.txt', '.dat'), 'w', encoding='utf-8') as archivo:
            for linea in lineas:
                archivo.write(linea)
            
        


if __name__ == '__main__':
    archivo = 'Asistencias21037AM.txt'
    
    archivo_transformado = TransformarArchivo(archivo)
    
    if archivo_transformado.verificar_archivo():
        archivo_transformado.transformar_archivo()
        
        archivo_transformado.limpieza_archivo()
        archivo_transformado.transformar_a_punto_dat()
        
        print(f'El archivo {archivo} se ha transformado correctamente.')
    else:
        print(f'El archivo {archivo} no existe.')
