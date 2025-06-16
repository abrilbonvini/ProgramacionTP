def calcular_IMC(peso, altura):
    return peso / (altura ** 2)


def calcular_porcentaje_grasa(peso, altura, edad, factor_genero):
    imc = calcular_IMC(peso, altura)
    return 1.2 * imc + 0.23 * edad - 5.4 - factor_genero


def calcular_calorias_en_reposo(peso, altura, edad, factor_genero):
   
    return 10 * peso + 6.25 * altura * 100 - 5 * edad + factor_genero


def calcular_calorias_en_actividad(peso, altura, edad, factor_genero, factor_actividad):
    tmb = calcular_calorias_en_reposo(peso, altura, edad, factor_genero)
    return tmb * factor_actividad


def consumo_calorias_recomendado_para_adelgazar(peso, altura, edad, factor_genero):
  
    tmb = calcular_calorias_en_reposo(peso, altura, edad, factor_genero)
    min_calorias = tmb * 0.8
    max_calorias = tmb * 0.85
    return f"Para adelgazar lo recomendado es que consuma entre: {int(min_calorias)} y {int(max_calorias)} calorías al día."
