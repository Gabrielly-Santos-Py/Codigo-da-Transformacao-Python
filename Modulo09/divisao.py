## 1. Tratamento de Divisão por Zero

def dividir(a, b):
    """
    Realiza a divisão de a por b e trata a exceção de divisão por zero.
    """
    try:
        resultado = a / b
        return resultado
    except ZeroDivisionError:
        # Captura e trata o erro se o denominador for zero
        return "Erro: Não é possível dividir por zero."
    except TypeError:
        # Trata caso os inputs não sejam números
        return "Erro: Certifique-se de que ambos os inputs são números."

# Exemplos de uso
print(f"10 / 2 = {dividir(10, 2)}")
print(f"5 / 0 = {dividir(5, 0)}")
print(f"8 / 'a' = {dividir(8, 'a')}") # Exemplo de outro erro tratado