#Pedirle un numero al usuario.

numero = input('Por favor , dame un numero: ')

#Multiplicando el numero por 2.

resultado = numero * 2   #Si el numero que ingresa el usuario por ejemplo es un 6 va a dar 66 porque es un texto.

#Para poder pasarlo a numero hacemos lo siguiente:

resultado2 = int(numero) * 2 #Aca si nos va a dar 12 si ingresamos el 6.Convertimos el numero a entero.

print(resultado)
print(resultado2)