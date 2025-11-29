# ===============================
# 3) Classificação de idade com if/elif/else
# ===============================

def classificar_idade():
    """
    Solicita a idade e classifica o indivíduo em categorias.
    """
    print("\n--- Classificação de Idade ---")
    
    try:
        idade = int(input("Digite a idade: "))
        
        if idade < 0:
            print("Erro: A idade não pode ser negativa.")
        elif idade < 12:
            print("Categoria: Criança")
        elif idade < 18:
            print("Categoria: Adolescente")
        elif idade < 60:
            print("Categoria: Adulto")
        else:
            print("Categoria: Idoso")

    except ValueError:
        print("Erro: Entrada inválida. Por favor, digite a idade em número inteiro.")


# Este bloco permite executar a função diretamente ao rodar este arquivo
if __name__ == "__main__":
    classificar_idade()