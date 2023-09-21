#if anidados y else-if (elif)

ingresoMensual = 22000
gastoMensual = 14000

if (ingresoMensual > 10000) : 
    if (ingresoMensual - gastoMensual < 0) :
        print('Estas en deficit')
    elif (ingresoMensual - gastoMensual > 3000) : 
        print('Estas bien economicamente')
    else : 
        print('Tenes muchos gastos mensuales')
    
elif (ingresoMensual > 1000) :   #elif seria como el else if, un elif no pueden ir despues de un else,solo despues de un if.
    print('Estas bien en Latinoamerica')

else : 
    print('Estas mal economicamente')