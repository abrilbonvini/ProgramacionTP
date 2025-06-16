from calculadora_indices import consumo_calorias_recomendado_para_adelgazar

try:
    peso = float(input("Ingresa tu peso (En kgs): "))
    altura = float(input("Ingresa tu altura (En centímetros): "))
    edad = int(input("Ingresa tu edad: "))
    genero = int(input("Seleccioná tu género: 1 para masculino, 2 para femenino: "))
    calorias_para_adelgazar = consumo_calorias_recomendado_para_adelgazar(peso, altura, edad, genero)
    
    if calorias_para_adelgazar:
        print(calorias_para_adelgazar)
except ValueError as error:
    print(error)
    print("Error. Verificá que todos los campos estén completos con números.")
