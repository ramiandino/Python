import re

texto = '''Hola maestro, esta es la cadena 1. Como estas mi capitan?
Esta es la segunda linea de texto 225657
Y esta es la finalabab definitiva miabab capitan'''

#Haciendo una busqueda simple.
resultado = re.search('Hola',texto)

#\d -> Busca digitos numeritos del 0 al 9

resultado1 = re.findall(r'\d',texto)    #r seria que posiblemente usemos expreciones regulares.

#\D -> Busca TODO MENOSdigitos numeritos del 0 al 9
resultado2 = re.findall(r'\D',texto)

#\w -> Busca caracteres alfanumericos [a-z A-Z 0-9 _]
resultado3 = re.findall(r'\w',texto)

#\W -> Busca TODO menos caracteres alfanumericos [a-z A-Z 0-9 _]
resultado4 = re.findall(r'\W',texto)

#\s -> Busca espacios en blanco => espacios,tabs,saltos de line
resultado5 = re.findall(r'\s',texto)

#\S -> Busca TODO menos espacios en blanco => espacios,tabs,saltos de line
resultado6 = re.findall(r'\S',texto)

#. -> Busca TODO menos saltos de line
resultado7 = re.findall(r'.',texto)

#\n -> Busca saltos de line
resultado8 = re.findall(r'\n',texto)

#\. -> Cancelar caracteres especiales, cancelando la funcion del punto y buscando puntos
resultado9 = re.findall(r'\.',texto)

#Armando una cadena que busque un numero,seguido de un punto y un espacio
resultado10 = re.findall(r'\d\. \s',texto)

#Buscando el principio de una linea
#^ -> Busca el comienzo de una linea,buscando hola al principio de la linea.
# flags=re.M activa la multilinea.
resultado11 = re.findall(r'hola',texto,flags=re.M)

#$ -> Busca el final de una linea.
# flags=re.M activa la multilinea.
resultado12 = re.findall(r'capitan$',texto,flags=re.M)

#{n} repite n cantidad de veces el valor de la izquierda(3 numeros juntos esta vez)
resultado13 = re.findall(r'\d{3}\s',texto)

#{n,m} -> al menos n,como maximo m
resultado14 = re.findall(r'\d{2,4}\s',texto)

#{n,m} -> abab
resultado15 = re.findall(r'(ab){2,4}',texto)

# | Busca una cosa o la otra
resultado16 = re.findall(r'\d{2,4}|Hola',texto)


print(resultado)
print(resultado1)
print(resultado2)
print(resultado3)
print(resultado4)
print(resultado5)
print(resultado6)
print(resultado7)
print(resultado8)
print(resultado9)
print(resultado10)
print(resultado11)
print(resultado12)
print(resultado13)
print(resultado14)
print(resultado15)
print(resultado16)
