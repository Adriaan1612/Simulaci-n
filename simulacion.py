#Actividad 1 - 25 puntos
#Por consola se piden como máximo 5 números hasta que pulsas q
#muestra la suma de los números introducidos.
#algoritmo funciona:5 puntos
#algoritmo utiliza mejora en argumentos : 5 puntos
#algoritmo controla errores y excepciones : 5 puntos
#algoritmo aplica funciones anónimas o recursividad : 5 puntos
#algoritmo resuelve una mejora de funcionalidad : 5 puntos

def pedir_numeros():
    numeros = []
    contador = 0

    while contador < 5:
        entrada = input("Ingresa un número (o 'q' para terminar): ")

        if entrada.lower() == 'q':
            break

        try:
            numero = float(entrada)
            numeros.append(numero)
            contador += 1
        except ValueError:
            print("Entrada inválida. Ingresa un número o 'q' para terminar.")

    return numeros


def main():
    numeros = pedir_numeros()
    suma = sum(numeros)
    print("Los números ingresados son:", numeros)
    print("La suma de los números es:", suma)


if __name__ == "__main__":
    main()



