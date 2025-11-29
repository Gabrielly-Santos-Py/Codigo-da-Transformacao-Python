# ===============================
# 1) Expressões matemáticas
# ===============================

def operacoes_basicas():
    print("\n--- Operações Matemáticas Básicas ---")
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))

    print(f"Soma: {a + b}")
    print(f"Subtração: {a - b}")
    print(f"Multiplicação: {a * b}")
    if b != 0:
        print(f"Divisão: {a / b}")
    else:
        print("Divisão: impossível (divisão por zero).")

    print(f"Resto da divisão: {a % b if b != 0 else 'Indefinido'}")


# ===============================
# 2) Maior número entre dois
# ===============================

def maior_numero():
    print("\n--- Verificar qual número é maior ---")
    x = float(input("Digite o primeiro número: "))
    y = float(input("Digite o segundo número: "))

    if x > y:
        print(f"O maior número é: {x}")
    elif y > x:
        print(f"O maior número é: {y}")
    else:
        print("Os dois números são iguais.")


# ===============================
# 3) Classificação de idade com if/elif/else
# ===============================

def classificar_idade():
    print("\n--- Classificação de Idade ---")
    idade = int(input("Digite a idade: "))

    if idade < 12:
        print("Categoria: Criança")
    elif idade < 18:
        print("Categoria: Adolescente")
    elif idade < 60:
        print("Categoria: Adulto")
    else:
        print("Categoria: Idoso")


# ===============================
# 4) DESAFIO EXTRA – Menu interativo com while
# ===============================

def menu_interativo():
    while True:
        print("\n====== MENU ======")
        print("1 - Soma")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("5 - Classificar Idade")
        print("6 - Comparar dois números")
        print("0 - Sair")
        print("==================")

        opcao = input("Escolha uma opção: ")

        if opcao == "0":
            print("Encerrando o programa... Até mais!")
            break

        elif opcao in ["1", "2", "3", "4"]:
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

        elif opcao == "5":
            classificar_idade()

        elif opcao == "6":
            maior_numero()

        else:
            print("Opção inválida! Tente novamente.")


# ===============================
# Execução principal
# ===============================

print("Bem-vindo! Aqui estão os exercícios da atividade.")
operacoes_basicas()
maior_numero()
classificar_idade()
menu_interativo()