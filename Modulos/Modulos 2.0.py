#Enrutamiento de modulos.
#Si el modulo estuviera dentro de una carpeta en la misma ruta.
# import FuncionesBuenas.Saludar as m_saludar

# print(m_saludar.saludar('Ramiro'))

import sys

print(sys.path) #Lista de rutas de modulos.

sys.path.append('C:\\Users\\Ramiro Andino\\Desktop\\Python\\FuncionesBuenas')

import ModuloSaludar as modulo_saludo

print(modulo_saludo.saludar('Ramiro'))