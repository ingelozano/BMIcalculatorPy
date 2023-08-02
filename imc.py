def calcular_imc(peso, altura):
    try:
        # Convertimos el peso y la altura a valores numéricos
        peso = float(peso)
        altura = float(altura)

        # Verificamos que el peso y la altura sean valores válidos (mayor que cero)
        if peso <= 0 or altura <= 0:
            return None

        # Calculamos el IMC
        imc = peso / (altura ** 2)
        return imc
    except ValueError:
        return None

if __name__ == "__main__":
    print("¡Calculadora de IMC!")
    peso_usuario = input("Ingresa tu peso en kilogramos: ")
    altura_usuario = input("Ingresa tu altura en metros (por ejemplo, si mides 1.75, ingresa '1.75'): ")

    # Calculamos el IMC llamando a la función
    imc_resultado = calcular_imc(peso_usuario, altura_usuario)

    if imc_resultado is not None:
        # Mostramos el resultado del IMC con dos decimales
        print(f"Tu Índice de Masa Corporal (IMC) es: {imc_resultado:.2f}")
    else:
        print("Por favor, ingresa valores numéricos válidos para peso y altura.")
