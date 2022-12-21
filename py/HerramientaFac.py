# Desarrollado por Sergio Gonzalez
# Herramienta para Transformar Facturas a formato de CG

from datetime import date
import pandas as pd
import time as t

# Transformar a OPP
    

# Datos de factura
serieFac = pd.DataFrame({'Serie': ['B', 'C', 'H', 'T', 'W'], 
                        'Numero': ['1', '11', '16', '2', '21']})


# Transformar datos de la factura a formato de CG
def dateCounter(fechaBase: str, fechaOriginal: str, fechaActual: str) -> list[str]:
    fechaBase = fechaBase.split('/')
    fechaOriginal = fechaOriginal.split('/')
    fechaActual = fechaActual.split('/')
    
    fechaBase = date(int(fechaBase[2]), int(fechaBase[1]), int(fechaBase[0]))
    fechaOriginal = date(int(fechaOriginal[2]), int(fechaOriginal[1]), int(fechaOriginal[0]))
    fechaActual = date(int(fechaActual[2]), int(fechaActual[1]), int(fechaActual[0]))
    
    fechas = [str(abs((fechaOriginal - fechaBase).days) + 1), 
              str(abs((fechaActual - fechaBase).days) + 1)]
    return fechas

# Generar el numero de factura para CG
def generadorFac(fac: str) -> str:
    if '-' in fac:
        fac = fac.split('-')
        letter = fac[0]
        print (letter)
    elif ' ' in fac:
        fac = fac.split(' ')
        letter = fac[0]
        print (letter)
    else :
        letter = fac[0]
        fac = fac[1:]
        fac = [letter, fac]
    

    for i in range(serieFac['Serie'].size):
        if letter == serieFac['Serie'][i]:
            fac = serieFac['Numero'][i] + fac[1]
            
            if fac[1] != '0':
                while len(fac) < 10:
                    fac = fac[0:2] + '0' + fac[2:]
                break
            else:
                fac = fac[0] + '0' + fac[1:]
                break
    
    return fac

        

if __name__ == '__main__':
    
    # Agregar excepciones para el formato de la fecha y el numero de factura
    
    fechaBase = '01/01/1900'
    fechaActual = t.strftime("%d/%m/%Y", t.localtime())
    
    fac = input('Introduce el numero de factura: ')
    # fechaOriginal = input('Introduce la fecha de la factura: ')

    
    print(serieFac, '\n')
    print(generadorFac(fac.capitalize()), '\n')
    # print(dateCounter(fechaBase, fechaOriginal, fechaActual))
    
