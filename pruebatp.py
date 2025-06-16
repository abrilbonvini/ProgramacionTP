import calculadora_indices

print("PRUEBATP\n")


hombre_IMC = calculadora_indices.calcular_IMC(81, 1.75) 
mujer_IMC = calculadora_indices.calcular_IMC(58, 1.69)

print("Cálculos del IMC")
print(f"Hombre IMC: {hombre_IMC:.2f}")
print(f"Mujer IMC: {mujer_IMC:.2f}")
print("")


valor_hombre = 1  
valor_mujer = 2   
hombre_PG = calculadora_indices.calcular_porcentaje_grasa(81, 1.75, 20, valor_hombre)
mujer_PG = calculadora_indices.calcular_porcentaje_grasa(58, 1.69, 21, valor_mujer)

print("Cálculos de porcentaje grasa")
print(f"Hombre porcentaje de grasa: {hombre_PG:.2f}%")
print(f"Mujer porcentaje de grasa: {mujer_PG:.2f}%")
print("")


hombre_CR = calculadora_indices.calcular_calorias_en_reposo(81, 175, 20, valor_hombre)
mujer_CR = calculadora_indices.calcular_calorias_en_reposo(58, 169, 21, valor_mujer)

print("Cálculos de calorías en reposo")
print(f"Hombre calorías en reposo: {hombre_CR:.2f} cal")
print(f"Mujer calorías en reposo: {mujer_CR:.2f} cal")
print("")


actividad_hombre = 3 
actividad_mujer = 2  
hombre_CA = calculadora_indices.calcular_calorias_en_actividad(81, 175, 20, valor_hombre, actividad_hombre)
mujer_CA = calculadora_indices.calcular_calorias_en_actividad(58, 169, 21, valor_mujer, actividad_mujer)

print("Cálculos de calorías en actividad")
print(f"Hombre calorías en actividad: {hombre_CA:.2f} cal")
print(f"Mujer calorías en actividad: {mujer_CA:.2f} cal")
print("")


calorias_hombre = calculadora_indices.consumo_calorias_recomendado_para_adelgazar(81, 175, 20, valor_hombre)
calorias_mujer = calculadora_indices.consumo_calorias_recomendado_para_adelgazar(58, 169, 21, valor_mujer)

print("Cálculos calorías recomendadas para adelgazar")
print(calorias_hombre)
print(calorias_mujer)
