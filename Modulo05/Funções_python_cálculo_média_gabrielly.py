def calcular_media(notas):
  """
  Recebe uma lista de notas, calcula a média e determina a situação do aluno.
  A média de aprovação é 7.
  """
  if not notas:
    print("Erro: A lista de notas está vazia.")
    return

  media = sum(notas) / len(notas)
  
  print(f"Notas: {notas}")
  print(f"Média calculada: {media:.2f}") # .2f formata para duas casas decimais

  if media >= 7:
    print("**Situação: APROVADO**")
  else:
    print("**Situação: REPROVADO**")

# Exemplos de uso:
# Aluno Aprovado
calcular_media([8.0, 7.5, 9.0, 6.5])

print("\n" + "="*20 + "\n")

# Aluno Reprovado
calcular_media([5.0, 6.0, 4.5, 7.0])