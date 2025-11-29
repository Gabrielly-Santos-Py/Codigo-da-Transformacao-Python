# ===============================
# 2) Maior número entre dois
# ===============================

def maior_numero():
    """
    Solicita dois números e determina qual é o maior.
    """
    print("\n--- Verificar qual número é maior ---")
    
    try:
        x = float(input("Digite o primeiro número: "))
        y = float(input("Digite o segundo número: "))

        if x > y:
            print(f"O maior número é: {x}")
        elif y > x:
            print(f"O maior número é: {y}")
        else:
            print("Os dois números são iguais.")
            
    except ValueError:
        print("Erro: Entrada inválida. Por favor, digite apenas números.")


# Este bloco permite executar a função diretamente ao rodar este arquivo
if __name__ == "__main__":
    maior_numero()