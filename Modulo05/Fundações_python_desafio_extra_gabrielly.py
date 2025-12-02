# Dicionário para armazenar os dados de login (usuário: senha)
DADOS_LOGIN = {
    "admin": "senha123",
    "joao": "python321",
    "maria": "abc@123"
}

def validar_login(usuario, senha):
  """
  Valida o login verificando se o usuário existe no dicionário 
  e se a senha corresponde.
  """
  # 1. Verifica se o usuário está cadastrado (é uma chave no dicionário)
  if usuario in DADOS_LOGIN:
    # 2. Se o usuário existe, verifica se a senha é a correta
    if DADOS_LOGIN[usuario] == senha:
      return True  # Login bem-sucedido
    else:
      return False # Senha incorreta
  else:
    return False   # Usuário não encontrado

# Exemplos de uso:

# 1. Login correto
usuario_teste_1 = "admin"
senha_teste_1 = "senha123"
if validar_login(usuario_teste_1, senha_teste_1):
  print(f"✅ Login bem-sucedido para o usuário: **{usuario_teste_1}**")
else:
  print(f"❌ Falha no login para o usuário: {usuario_teste_1}")

# 2. Senha incorreta
usuario_teste_2 = "joao"
senha_teste_2 = "senhaerrada"
if validar_login(usuario_teste_2, senha_teste_2):
  print(f"✅ Login bem-sucedido para o usuário: **{usuario_teste_2}**")
else:
  print(f"❌ Falha no login para o usuário: {usuario_teste_2} (Senha Incorreta)")

# 3. Usuário não existe
usuario_teste_3 = "pedro"
senha_teste_3 = "qualquercoisa"
if validar_login(usuario_teste_3, senha_teste_3):
  print(f"✅ Login bem-sucedido para o usuário: **{usuario_teste_3}**")
else:
  print(f"❌ Falha no login para o usuário: {usuario_teste_3} (Usuário Não Cadastrado)")