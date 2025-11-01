# --- ATIVIDADE 3: SAUDAÇÃO PERSONALIZADA ---

# 1. Solicitar o nome do usuário
# A função 'input()' exibe o texto e espera a entrada do usuário.
# O valor digitado é armazenado na variável 'nome_usuario'.
nome_usuario = input("Qual é o seu nome? ")

# 2. Exibir a mensagem personalizada
# Usamos 'f-string' (a string que começa com 'f') para inserir o
# valor da variável 'nome_usuario' dentro da mensagem de saudação.
print(f"Olá, {nome_usuario}! É um prazer ter você por aqui.")

# Exemplo de saída no console (se o usuário digitar "Ana"):
# Qual é o seu nome? Ana
# Olá, Ana! É um prazer ter você por aqui.