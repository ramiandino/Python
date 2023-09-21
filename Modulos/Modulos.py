import ModuloSaludar as MSaludar  #Nos sirve para poder cambiar el nombre al modulo para que no tenga interferencias.

saludo = MSaludar.saludar('Ramiro')
print(saludo)


# "valor" as variable


from ModuloSaludar import saludar  #Me traigo solo la funcion que quiero del modulo.

saludo = saludar('Ramiro')
print(saludo)

#Con import * nos importamos todo.  #No es buena practica,el programa se sobrecarga.

#Para ver las propiedades y metodos de el namespace
#print(dir(namespace))

#Accedemos al nombre de este modulo.
print(__name__)

#Accedemos al nombre de modulo llamado.

print(MSaludar.__name__)

