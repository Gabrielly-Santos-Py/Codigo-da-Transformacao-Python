import json

# 1. Dados do dicionário de clientes
dados_clientes = {
    "1001": {"nome": "Maria Silva", "cidade": "São Paulo"},
    "1002": {"nome": "João Santos", "cidade": "Rio de Janeiro"},
    "1003": {"nome": "Ana Oliveira", "cidade": "Belo Horizonte"}
}
nome_arquivo_json = "clientes.json"

# 2. Salvar o dicionário no arquivo JSON
try:
    # O modo 'w' é usado para escrita
    with open(nome_arquivo_json, 'w', encoding='utf-8') as arquivo:
        # indent=4 formata o JSON para melhor legibilidade
        json.dump(dados_clientes, arquivo, indent=4)
    print(f"✅ Dicionário de clientes salvo em '{nome_arquivo_json}'.")

    # 3. Carregar o dicionário do arquivo JSON
    with open(nome_arquivo_json, 'r', encoding='utf-8') as arquivo:
        clientes_carregados = json.load(arquivo)
    
    print(f"\nDados carregados de '{nome_arquivo_json}':")
    print("---")
    # Exibir os dados carregados de forma estruturada
    for id_cliente, cliente in clientes_carregados.items():
        print(f"ID: {id_cliente}, Nome: {cliente['nome']}, Cidade: {cliente['cidade']}")
    print("---")

except IOError as e:
    print(f"❌ Ocorreu um erro ao manipular o arquivo: {e}")
except json.JSONDecodeError:
    print(f"❌ Erro ao decodificar o arquivo JSON: '{nome_arquivo_json}' não é um JSON válido.")