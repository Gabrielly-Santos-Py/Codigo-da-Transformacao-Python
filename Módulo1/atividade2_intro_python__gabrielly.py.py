# ===============================================
# CÓDIGO COMBINADO: ATIVIDADE 3 E DESAFIO EXTRA
# ===============================================

# O Desafio Extra pede para exibir a hora atual. Para isso,
# precisamos importar a biblioteca 'datetime', que lida com
# datas e horas em Python.
import datetime

# -----------------------------------------------
# ATIVIDADE 3: Pedir nome e exibir saudação personalizada
# -----------------------------------------------

# A função 'input()' exibe uma mensagem no console e espera
# que o usuário digite algo. O valor digitado é armazenado
# na variável 'nome_usuario'.
nome_usuario = input("Por favor, digite o seu nome: ")

# -----------------------------------------------
# DESAFIO EXTRA: Exibir a hora atual
# -----------------------------------------------

# datetime.datetime.now() retorna um objeto que contém a data e hora exatas.
# .strftime("%H:%M:%S") formata esse objeto para exibir a hora, minuto e segundo.
hora_atual = datetime.datetime.now().strftime("%H:%M:%S")

# -----------------------------------------------
# Exibição dos resultados
# -----------------------------------------------

# A função 'print()' exibe a saída. Usamos 'f-strings' (strings com 'f'
# no início) para incluir (ou interpolar) variáveis dentro da mensagem.
print(f"\n--- Resultado da Saudação ---")

# Mensagem de saudação personalizada
print(f"Olá, {nome_usuario}! Seja bem-vindo(a) ao seu primeiro programa Python.")

# Exibe a hora atual como parte do Desafio Extra
print(f"A hora atual é: {hora_atual}")

print(f"---------------------------\n")


# ===============================================
# ATIVIDADE 2: Exemplos de comandos do interpretador
# ===============================================

# A Atividade 2 é feita diretamente no interpretador Python,
# mas aqui estão os exemplos de como esses comandos funcionam:

# Exemplo de 'print()':
# print("Isso é exibido na tela")

# Exemplo de 'type()' para ver o tipo de dado:
# type("Uma string de texto")  # Retorna: <class 'str'>
# type(100)                    # Retorna: <class 'int'> (número inteiro)
# type(50.5)                   # Retorna: <class 'float'> (número decimal)