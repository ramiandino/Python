#Promedios de duracion de cursos:

otrosCursosMin = 2.5
otrosCursosMax = 7
otrosCursosProm = 4
cursoDalto = 1.5

#Diferencia de duracion:

diferenciaMin = 100 - (cursoDalto / otrosCursosMin * 100)
diferenciaMax = 100 - (cursoDalto * 1000  // otrosCursosMax / 10)
diferenciaProm = 100 - (cursoDalto / otrosCursosProm * 100)

#Diferencia de crudos

crudoProm = 5
crudoDalto = 3.5

#Calculando el porcentaje de tiempo vacio

tiempoVacioProm = 100 - (otrosCursosProm * 1000  // crudoProm / 10)

tiempoVacioDalto= 100 - (cursoDalto * 1000  // crudoDalto / 10)

#Mostrando las diferencias de duracion (ejercicio A)
print('----------------')
print('El curso de Dalto dura:')
print(f' - un {diferenciaMin}% menos que el mas rapido')
print(f' - un {diferenciaMax}% menos que el mas lento')
print(f' - un {diferenciaProm}% menos que el promedio')
print('----------------')

#Mostrando la cantidad de espacios vacios que se remueven (ejercicio B)
print(f' - Un curso promedio elimina un {tiempoVacioProm}% de tiempo vacio')
print(f' - Este curso elimino el {tiempoVacioDalto}% de tiempo vacio')
print('----------------')

#Mostrando diferencias si los cursos duraran 10 horas
print(f' - Ver 10 horas de este curso equivale a ver {otrosCursosProm * 100 // cursoDalto / 10} horas de otros cursos')
print(f' - Ver 10 horas de otros cursos equivale a ver {cursoDalto * 100 // otrosCursosProm / 10} horas de otros cursos')
print('----------------')