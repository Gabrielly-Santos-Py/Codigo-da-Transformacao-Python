# programa_data.py

from datetime import date

def calcular_idade(data_nascimento):
    """
    Calcula a idade de uma pessoa dada a data de nascimento (datetime.date).
    """
    hoje = date.today()
    
    # Subtrai o ano atual pelo ano de nascimento
    idade = hoje.year - data_nascimento.year
    
    # Verifica se o aniversário já ocorreu neste ano
    # Se o mês e dia de hoje for ANTES do mês e dia de nascimento,
    # significa que a pessoa ainda não fez aniversário, então subtrai 1 da idade.
    if (hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day):
        idade -= 1
        
    return idade

# Define a data de nascimento (ano, mês, dia)
data_nasc = date(1995, 11, 25) 

# Chama a função e armazena o resultado
idade_calculada = calcular_idade(data_nasc)

# Imprime o resultado
print(f"--- Utilizando a biblioteca 'datetime' ---")
print(f"Data de nascimento: {data_nasc.strftime('%d/%m/%Y')}")
print(f"Hoje é: {date.today().strftime('%d/%m/%Y')}")
print(f"A idade calculada é: {idade_calculada} anos")