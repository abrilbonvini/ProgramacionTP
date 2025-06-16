from calculadora_indices import calcular_IMC

def categoria_imc(imc):
    if imc < 16:
        return "Delgadez Severa"
    elif imc < 17:
        return "Delgadez Moderada"
    elif imc < 18.5:
        return "Delgadez Aceptable"
    elif imc < 25:
        return "Peso Normal"
    elif imc < 30:
        return "Sobrepeso"
    elif imc < 35:
        return "Obesidad Tipo 1"
    elif imc < 40:
        return "Obesidad Tipo 2"
    elif imc < 50:
        return "Obesidad Tipo 3 - Mórbida"
    else:
        return "Obesidad Tipo 4 - Extrema"

try:
    peso = float(input("Ingrese su peso (En kgs): "))
    altura = float(input("Ingrese su altura (En metros): "))
    imc = calcular_IMC(peso, altura)
    
    if imc:
        categoria = categoria_imc(imc)
        print(f"Tu IMC: {imc}\nTu categoría es: {categoria}")
except ValueError as error:
    print(error)
    print("Error. Verificá que todos los campos estén completos con números.")
