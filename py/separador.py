# Agregar comas a IDs de despachos en archivo de texto
def separador():
    
    print("Modificar el txt de despachos antes de ejecutar el script")
    with open("../py/despachos.txt", "r") as archivo:
        print (",".join(archivo.read().splitlines()))
        
        
if __name__ == '__main__':
    
    separador() # Llamada a la funcion principal