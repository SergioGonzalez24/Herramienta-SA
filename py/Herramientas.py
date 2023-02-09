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
        stay = True
        opcion = int(input('Introduce la opcion deseada: '))
        if opcion == 1:
            # Repetir hasta que el usuario decida salir
            while stay:
                numero_estacion = input('Introduce el numero de estacion: ')
                print(GeneradorContras.transformadora(numero_estacion))
                
                print("Enter para seguir en Contraseñas, escriba exit para salir ")
                if input() == 'exit':
                    stay = False
                else:
                    continue
                
            
        elif opcion == 2:
            # Repetir hasta que el usuario decida salir
            while stay:
                fac = input('Introduce la factura: ')
                print(HerramientaFac.generadorFac(fac.capitalize()), '\n')
                
                print("Enter para seguir en Contraseñas, escriba ""exit"" para salir ")
                if input() == 'exit':
                    stay = False
                else:
                    continue
                
            
        elif opcion == 3:
            # Repetir hasta que usuario decida salir
            while stay:
                fechaOriginal = input('Introduce la fecha de la factura: ')
                fechaBase = '01/01/1900'
                fechaActual = t.strftime('%d/%m/%Y', t.localtime())
                print("  Factura | Actual \n", 
                    HerramientaFac.dateCounter(fechaBase, fechaOriginal, fechaActual))
                
                print("Enter para seguir en Contraseñas, escriba exit para salir ")
                if input() == 'exit':
                    stay = False
                else:
                    continue
                
        elif opcion == 4:
            break
        
        else:
            print('Opcion invalida')
            input('Presiona enter para continuar')


if __name__ == '__main__':
    
    main() # Llamada a la funcion principal
        
    