#Actividad 2
#En consola se piden las unidades y el precio.
#Estos datos permiten calcular el subtotal.
#Si el día de hoy es anterior al 15 de cada mes, se aplica
#un descuento del 5%
#Muestra el resultado el total de la factura.

def calcular_subtotal(unidades, precio):
    subtotal = unidades * precio
    return subtotal

def aplicar_descuento(subtotal):
    dia_actual = int(input("¿Qué día es hoy? Ingresa el número: "))
    if dia_actual < 15:
        descuento = subtotal * 0.05
        subtotal -= descuento
    return subtotal

def main():
    unidades = int(input("Ingresa la cantidad de unidades: "))
    precio = float(input("Ingresa el precio por unidad: "))

    subtotal = calcular_subtotal(unidades, precio)
    total = aplicar_descuento(subtotal)

    print(f"El subtotal es: {subtotal:.2f}")
    print(f"El total de la factura es: {total:.2f}")

if __name__ == "__main__":
    main()
