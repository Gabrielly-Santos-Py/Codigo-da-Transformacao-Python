# programa_principal.py

# Importa o módulo utilidades
import utilidades

# Utiliza as funções importadas
num1 = 15
num2 = 7

# Chamada das funções
resultado_soma = utilidades.somar(num1, num2)
resultado_subtracao = utilidades.subtrair(num1, num2)
resultado_potencia = utilidades.calcular_potencia(3, 3)

# Exibição dos resultados
print(f"--- Utilizando o Módulo 'utilidades' ---")
print(f"A soma de {num1} e {num2} é: {resultado_soma}")
print(f"A subtração de {num1} por {num2} é: {resultado_subtracao}")
print(f"A potência de 3 elevado a 3 é: {resultado_potencia}")