def agenda_de_contatos():
    """
    Sistema de agenda de contatos usando dicionários, permitindo adicionar, remover e buscar.
    """
    agenda = {}
    
    while True:
        print("\n--- Agenda de Contatos (Dicionário) ---")
        print("1 - Adicionar Contato")
        print("2 - Remover Contato")
        print("3 - Buscar Contato")
        print("4 - Visualizar Todos")
        print("0 - Sair")
        
        opcao = input("Escolha uma opção: ").strip()

        if opcao == '1':
            nome = input("Nome do contato: ").strip().capitalize()
            numero = input("Número de telefone: ").strip()
            
            if nome and numero.isdigit():
                agenda[nome] = numero
                print(f"Contato '{nome}' adicionado com sucesso.")
            else:
                print("Erro: Nome não pode ser vazio ou número de telefone inválido.")

        elif opcao == '2':
            nome = input("Nome do contato a remover: ").strip().capitalize()
            # Usamos .pop() com um valor padrão para evitar erro se a chave não existir
            if agenda.pop(nome, None) is not None:
                print(f"Contato '{nome}' removido com sucesso.")
            else:
                print(f"Erro: Contato '{nome}' não encontrado na agenda.")

        elif opcao == '3':
            nome = input("Nome do contato a buscar: ").strip().capitalize()
            # Usamos .get() para obter o valor ou None se a chave não existir
            numero = agenda.get(nome)
            
            if numero:
                print(f"Contato encontrado: {nome} -> {numero}")
            else:
                print(f"Contato '{nome}' não encontrado.")

        elif opcao == '4':
            if agenda:
                print("\n--- Lista de Contatos ---")
                # Itera sobre as chaves e valores do dicionário
                for nome, numero in agenda.items():
                    print(f"- {nome}: {numero}")
            else:
                print("A agenda está vazia.")
                
        elif opcao == '0':
            print("Encerrando a agenda. Até logo!")
            break
            
        else:
            print("Opção inválida! Tente novamente.")

# Execução da Atividade 4 (Desafio Extra)
# agenda_de_contatos()