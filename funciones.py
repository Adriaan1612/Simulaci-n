#capítulo 10 - pádina 204

#user functions
def sumar(i,j):
    return i+j

suma_anonima=lambda i,j:i+j
print(fr"el total de la suma anonima con lambda es {suma_anonima}")
def sumar_default(i,j,k=25):
    return i+j+k

def sumar_variables(*args):
    total=0
    for i in args:
        total+=i
    return total

suma=sumar(4,5)
print(f"el total de la suma es {suma}")

suma2=sumar_default(4,5)
print(f"El total de una funcion con  argumentos variables es {suma}")

suma3=sumar_variables(5,9,4,7)
print(f"la suma totalde una funcion con argumentos variables es {suma}")

#recursividad una funcion que se llama asi misma
def factorial(n):
    if n==1:
        return n
    elif n <=0:
        print(f"no hay factorial para 0 o menor que 0")
    else:
        return n+factorial(n-1) #recursividad porque se llama a si mismo

resultado_factorial=factorial(996)
print(F"el factorial es {resultado_factorial}")