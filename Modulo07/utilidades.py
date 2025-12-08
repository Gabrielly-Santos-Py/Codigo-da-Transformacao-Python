# utilidades.py

def somar(a, b):
    """Retorna a soma de dois números."""
    return a + b

def subtrair(a, b):
    """Retorna a diferença entre dois números."""
    return a - b

def calcular_potencia(base, expoente):
    """Retorna a potência de um número (base elevado ao expoente)."""
    return base ** expoente

# Exemplo de como usar o módulo
if __name__ == "__main__":
    print(f"Teste de Soma: 5 + 3 = {somar(5, 3)}")
    print(f"Teste de Subtração: 10 - 4 = {subtrair(10, 4)}")
    print(f"Teste de Potência: 2^4 = {calcular_potencia(2, 4)}")