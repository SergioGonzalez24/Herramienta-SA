# Desarrollado por Sergio Gonzalez

import HerramientaFac
import GeneradorContras
import time as t

# importar modulo para generar GUI de Herramientas

def main():
    # Funcion principal de llamada a nuestros modulos de herramientas
    while True:
        print('''
        Bienvenido a Herramientas
        1. Generador de contraseñas
        2. Generador de facturas
        3. Generador de fecha
        4. Salir
        ''')
        opcion = int(input('Introduce la opcion deseada: '))
        if opcion == 1:
            numero_estacion = input('Introduce el numero de estacion: ')
            print(GeneradorContras.transformadora(numero_estacion))
            
        elif opcion == 2:
            fac = input('Introduce la factura: ')
            print(HerramientaFac.generadorFac(fac.capitalize()), '\n')
            
        elif opcion == 3:
            fechaOriginal = input('Introduce la fecha de la factura: ')
            fechaBase = '01/01/1900'
            fechaActual = t.strftime('%d/%m/%Y', t.localtime())
            print("  Factura | Actual \n", 
                  HerramientaFac.dateCounter(fechaBase, fechaOriginal, fechaActual))
            
        elif opcion == 4:
            break
        
        else:
            print('Opcion invalida')
        input('Presiona enter para continuar')


if __name__ == '__main__':
    
    main() # Llamada a la funcion principal
        
    