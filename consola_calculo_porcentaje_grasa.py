from calculadora_indices import calcular_porcentaje_grasa

def porcentaje_de_grasa_recomendado(edad, valor_genero):
    if edad > 19:
        if valor_genero == 1:
            return "11% - 20%"
        else:
            return "16% - 28%"
    elif edad > 29:
        if valor_genero == 1:
            return "12% - 21%"
        else:
            return "17% - 29%"
    elif edad > 39:
        if valor_genero == 1:
            return "14% - 23%"
        else:
            return "18% - 30%"
    elif edad > 49:
        if valor_genero == 1:
            return "15% - 24%"
        else:
            return "19% - 31%"

try:
    peso = float(input("Ingrese su peso (En KGs): "))
    altura = float(input("Ingrese su altura (En metros): "))
    edad = int(input("Ingrese su edad: "))
    genero = int(input("Seleccione su género: 1 para masculino, 2 para femenino: "))
    porcentaje_grasa = calcular_porcentaje_grasa(peso, altura, edad, genero)
    
    if porcentaje_grasa:
        print(f"Su porcentaje de grasa corporal es de: {porcentaje_grasa}%")
        if 20 <= edad <= 59:
            porcentaje_recomendado = porcentaje_de_grasa_recomendado(edad, genero)
            print(f"Según su edad y género, el valor recomendado está entre: {porcentaje_recomendado}")
except ValueError as error:
    print(error)
    print("Revise los datos ingresados. Todos deben ser numéricos para hacer el cálculo correctamente.")
