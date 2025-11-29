# ===============================
# 4) DESAFIO EXTRA – Menu interativo com while
# 
# NOTA: Para rodar este código, as funções 
# 'classificar_idade' e 'maior_numero' precisariam ser
# importadas de seus respectivos arquivos.
# ===============================

# ⚠️ SIMULAÇÃO: No código original, essas funções eram definidas no mesmo arquivo. 
# Para fins deste arquivo isolado, as funções de suporte são redefinidas aqui 
# ou você precisaria importá-las. Vamos redefinir as operações para simplicidade.

def _realizar_operacoes(opcao):
    """Função auxiliar para o menu."""
    try:
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))
        
        if opcao == "1":
            print(f"Resultado da Soma: {a + b}")
        elif opcao == "2":
            print(f"Resultado da Subtração: {a - b}")
        elif opcao == "3":
            print(f"Resultado da Multiplicação: {a * b}")
        elif opcao == "4":
            if b != 0:
                print(f"Resultado da Divisão: {a / b}")
            else:
                print("Erro: divisão por zero!")
    except ValueError:
        print("Erro: Entrada inválida. Por favor, digite apenas números.")


def menu_interativo():
    """
    Apresenta um menu interativo que chama as outras funcionalidades.
    """
    # Usando as funções do código original (assumindo que foram importadas ou definidas)
    # Aqui, vamos usar as implementações temporárias para fins de demonstração.
    
    # IMPORTANTE: Se você quisesse usar as funções dos arquivos 2 e 3, 
    # você faria: from classificar_idade import classificar_idade
    # e from maior_numero import maior_numero
    
    while True:
        print("\n====== MENU ======")
        print("1 - Soma")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("5 - Classificar Idade (chama classificar_idade)")
        print("6 - Comparar dois números (chama maior_numero)")
        print("0 - Sair")
        print("==================")

        opcao = input("Escolha uma opção: ")

        if opcao == "0":
            print("Encerrando o programa... Até mais!")
            break

        elif opcao in ["1", "2", "3", "4"]:
            _realizar_operacoes(opcao) # Chama a função auxiliar para as 4 operações

        elif opcao == "5":
            # Aqui você chamaria: classificar_idade()
            print("⚠️ Chamando a função Classificar Idade (veja o arquivo 3).")
            # Para testes, chame a função diretamente:
            # classificar_idade() 

        elif opcao == "6":
            # Aqui você chamaria: maior_numero()
            print("⚠️ Chamando a função Comparar dois números (veja o arquivo 2).")
            # Para testes, chame a função diretamente:
            # maior_numero() 

        else:
            print("Opção inválida! Tente novamente.")

# Este bloco permite executar a função diretamente ao rodar este arquivo
if __name__ == "__main__":
    menu_interativo()