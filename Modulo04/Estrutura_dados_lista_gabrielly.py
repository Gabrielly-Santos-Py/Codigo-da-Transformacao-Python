def lista_de_compras():
    """
    Programa que gerencia uma lista de compras, permitindo adicionar, remover e visualizar itens.
    """
    lista = []
    
    while True:
        print("\n--- Gerenciador de Lista de Compras ---")
        print("1 - Adicionar item")
        print("2 - Remover item")
        print("3 - Visualizar lista")
        print("0 - Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            item = input("Digite o item a ser adicionado: ").strip()
            if item:
                lista.append(item.capitalize())
                print(f"'{item.capitalize()}' adicionado à lista.")
            else:
                print("O nome do item não pode ser vazio.")
                
        elif opcao == '2':
            if not lista:
                print("A lista está vazia. Nada para remover.")
                continue
                
            print("\nItens na lista:")
            # Exibe a lista com índices para facilitar a remoção
            for i, item in enumerate(lista):
                print(f"[{i+1}] {item}")
                
            try:
                # O usuário digita o número do item (índice + 1)
                indice_remover = int(input("Digite o número do item a remover (ou 0 para cancelar): "))
                
                if indice_remover == 0:
                    continue
                
                # Ajusta para o índice real da lista (número do usuário - 1)
                if 1 <= indice_remover <= len(lista):
                    item_removido = lista.pop(indice_remover - 1)
                    print(f"'{item_removido}' removido da lista.")
                else:
                    print("Número de item inválido.")
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")

        elif opcao == '3':
            if lista:
                print("\n--- Sua Lista de Compras Atualizada ---")
                for i, item in enumerate(lista):
                    print(f"- {item}")
            else:
                print("A lista de compras está vazia.")
                
        elif opcao == '0':
            print("Saindo do gerenciador de lista. Até mais!")
            break
            
        else:
            print("Opção inválida! Por favor, tente novamente.")

# Execução da Atividade 1
# lista_de_compras()