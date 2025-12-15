## Desafio Extra: Sistema de Login

USUARIO_CORRETO = "admin"
SENHA_CORRETA = "12345"
MAX_TENTATIVAS = 3

def sistema_login():
    tentativas = 0
    print("--- Sistema de Login ---")
    
    while tentativas < MAX_TENTATIVAS:
        usuario = input("Usuário: ")
        senha = input("Senha: ")
        
        # Simula a verificação de credenciais
        if usuario == USUARIO_CORRETO and senha == SENHA_CORRETA:
            print("\nLogin bem-sucedido! Bem-vindo(a).")
            return
        else:
            tentativas += 1
            restantes = MAX_TENTATIVAS - tentativas
            
            if restantes > 0:
                print(f"Credenciais inválidas. Você tem mais {restantes} tentativa(s).")
            else:
                print("\nCredenciais inválidas.")

    # Mensagem final se as tentativas esgotarem
    print("Número máximo de tentativas excedido. O sistema será bloqueado.")

# Teste do Desafio Extra
sistema_login()