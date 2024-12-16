# Función para la entrada de datos diarios
def ingresar_temperaturas():
    temperaturas = []
    print("Ingrese las temperaturas diarias de la semana (7 días):")
    for dia in range(1, 8):
        while True:
            try:
                temp = float(input(f"Día {dia}: "))
                temperaturas.append(temp)
                break
            except ValueError:
                print("Por favor, ingrese un valor numérico válido.")
    return temperaturas

# Función para calcular el promedio semanal
def calcular_promedio(temperaturas):
    total = sum(temperaturas)
    promedio = total / len(temperaturas)
    return promedio

# Función principal para coordinar el flujo del programa
def main():
    print("Programa para calcular el promedio semanal de temperaturas")
    temperaturas = ingresar_temperaturas()
    promedio = calcular_promedio(temperaturas)
    print("\nResumen:")
    print("Temperaturas ingresadas:", temperaturas)
    print(f"Promedio semanal de temperaturas: {promedio:.5f} °C")

# Llamada a la función principal
if __name__ == "__main__":
    main()
