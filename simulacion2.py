#Actividad 3
#En consola pides número inicial.
#En consola pides número final.
#Muestra una lista con todos los números pares que hay entre
#estos dos números.

def encontrar_pares(num_inicial, num_final):
    lista_pares = [num for num in range(num_inicial, num_final + 1) if num % 2 == 0]
    return lista_pares

def main():
    num_inicial = int(input("Ingresa el número inicial: "))
    num_final = int(input("Ingresa el número final: "))

    if num_final < num_inicial:
        print("El número final debe ser mayor que el número inicial.")
    else:
        pares = encontrar_pares(num_inicial, num_final)
        print("Los números pares entre", num_inicial, "y", num_final, "son:", pares)

if __name__ == "__main__":
    main()
