def dados_do_aluno():
    """
    Armazena dados de um aluno em um dicionário e exibe os valores.
    """
    print("\n--- Armazenamento de Dados do Aluno ---")
    
    # Criação do dicionário com diferentes tipos de dados
    aluno = {
        "nome": "João da Silva",
        "idade": 25,
        "curso": "Engenharia de Software",
        "notas": [8.5, 7.0, 9.2],
        "ativo": True
    }
    
    print("\nDados do Aluno Armazenados:")
    print("----------------------------")
    
    # Exibir todos os dados usando um loop
    for chave, valor in aluno.items():
        if chave == "notas":
            # Formatação especial para a lista de notas
            print(f"{chave.capitalize()}: {', '.join(map(str, valor))} (Média: {sum(valor)/len(valor):.2f})")
        else:
            print(f"{chave.capitalize()}: {valor}")

    # Exibir dados acessando chaves específicas
    print("\nExemplo de Acesso Específico:")
    print(f"O aluno {aluno['nome']} tem {aluno['idade']} anos.")
    
# Execução da Atividade 2
# dados_do_aluno()