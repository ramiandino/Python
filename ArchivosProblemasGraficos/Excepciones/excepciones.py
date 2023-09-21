#Creando una funcion que suma numeros.
def sumar_dos():
    #Iniciando un bucle
    while True:
        #Pidiendo numeros
        a = input('Numero 1: ')
        b = input('Numero 2: ')
        #Intentando convertirlos a enteros y sumarlos
        try:
            resultado = int(a) + int(b)
        #Si lanzo una excepcion,pedirle que reingrese los datos
        except Exception as e:
            print('Te pedi un numero')
            print(f'ERROR: {e}')
        #Si todo salio bien,terminamos el bucle
        else:
            break
        #finally se ejecuta siempre
        finally:
            print('Manejo de excepcion finalizado')
    #Mostrando el resultado
    return resultado

print(sumar_dos())