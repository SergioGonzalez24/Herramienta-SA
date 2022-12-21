# Codigo desarrollado por Sergio Gonzalez

def transformadora(numero_estacion:str) -> str:
    contra = "E" + numero_estacion[:2] + "$y$" + numero_estacion[2:]
    return contra

if __name__ == '__main__':
    numero_estacion = input('Introduce el numero de estacion: ')
    print(transformadora(numero_estacion))
    


