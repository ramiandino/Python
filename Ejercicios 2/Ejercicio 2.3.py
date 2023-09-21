#Creando una funcion que muestre la serie Fibonacci entre el 0 y el numero dado.

def fibonacci(num):
    a,b = 0,1
    listaFibonacci = [0]
    for i in range(num):
        if (b > num): return listaFibonacci
        else: 
            listaFibonacci.append(b)
            a,b = b,a + b
resultado = fibonacci(20)
print(resultado)