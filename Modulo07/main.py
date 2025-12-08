# main.py

# Importação explícita dos módulos dentro dos pacotes
from pacotes.aritmetica import operacoes
from pacotes.geometria import formas

# Exemplo de uso das funções
# Aritmética
num1 = 10
num2 = 5
resultado_soma = operacoes.somar(num1, num2)
print(f"A soma de {num1} e {num2} é: {resultado_soma}")

# Geometria
raio = 5
lado_quadrado = 6
area_circulo_calc = formas.area_circulo(raio)
perimetro_quadrado_calc = formas.perimetro_quadrado(lado_quadrado)

# Uso da formatação de string para arredondar a área
print(f"A área do círculo com raio {raio} é: {area_circulo_calc:.2f}")
print(f"O perímetro do quadrado com lado {lado_quadrado} é: {perimetro_quadrado_calc}")