def separar_pares_impares():
    """
    Percorre um conjunto de números e separa-os em pares e ímpares.
    """
    print("\n--- Separador de Números Pares e Ímpares ---")
    
    # Conjunto de números a ser percorrido
    numeros = [4, 7, 12, 1, 9, 20, 5, 10, 3, 16]
    
    # Inicializa as listas para armazenar os resultados
    pares = []
    impares = []
    
    print(f"Conjunto original: {numeros}")
    
    # Percorre o conjunto de números
    for num in numeros:
        # Verifica se o número é par (resto da divisão por 2 é 0)
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)
            
    print("\n--- Resultados ---")
    print(f"Números Pares: {pares}")
    print(f"Números Ímpares: {impares}")
    
# Execução da Atividade 3
# separar_pares_impares()