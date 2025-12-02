def maior_menor(lista_numeros):
  """
  Recebe uma lista de números e retorna uma tupla (maior, menor) contendo 
  o maior e o menor valores da lista.
  """
  if not lista_numeros:
    # Retorna None ou levanta um erro, dependendo do requisito.
    # Neste caso, vamos retornar None.
    return None, None 

  # As funções built-in (nativas) max() e min() facilitam a busca
  maior = max(lista_numeros)
  menor = min(lista_numeros)
  
  return maior, menor

# Exemplo de uso:
numeros = [12, 5, 45, 8, 30, 2, 51]
maior, menor = maior_menor(numeros)

print(f"Lista de números: {numeros}")

if maior is not None:
  print(f"O **maior** valor é: {maior}")
  print(f"O **menor** valor é: {menor}")
else:
  print("A lista está vazia.")