import datetime  # 1. Importa a biblioteca para lidar com data e hora

# --- INÍCIO DO DESAFIO EXTRA ---

# 2. Pede o nome do usuário (Base da Atividade 3)
nome_usuario = input("Digite o seu nome para a saudação especial: ")

# 3. Obtém a hora atual (Núcleo do Desafio Extra)
# datetime.datetime.now() captura o momento atual.
# .strftime("%H:%M:%S") formata esse momento para apenas Hora:Minuto:Segundo.
hora_atual = datetime.datetime.now().strftime("%H:%M:%S")

# 4. Exibe a mensagem personalizada, incluindo a hora atual
print("-" * 35)
print(f"🎉 Olá, {nome_usuario}! Seja bem-vindo(a).")
print(f"🕒 A hora atual é: {hora_atual}")
print("-" * 35)

# Exemplo de Saída no Console:
# Digite o seu nome para a saudação especial: Pedro
# -----------------------------------
# 🎉 Olá, Pedro! Seja bem-vindo(a).
# 🕒 A hora atual é: 11:56:14 <-- (Este valor mudará a cada execução)
# -----------------------------------