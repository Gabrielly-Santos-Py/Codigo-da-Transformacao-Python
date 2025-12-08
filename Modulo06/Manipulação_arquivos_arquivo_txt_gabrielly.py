# 1. Gravar informações no arquivo .txt
nome_arquivo = "info.txt"
informacao = "Este é um teste de gravação e leitura de arquivo TXT.\n"

try:
    # O modo 'w' (write) cria o arquivo ou sobrescreve o existente
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        arquivo.write(informacao)
    print(f"✅ Informação gravada em '{nome_arquivo}'.")

    # 2. Ler as informações do arquivo
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        conteudo = arquivo.read()
    
    print(f"\nConteúdo lido de '{nome_arquivo}':")
    print("---")
    print(conteudo.strip()) # strip() remove espaços/quebras de linha extras
    print("---")

except IOError as e:
    print(f"❌ Ocorreu um erro ao manipular o arquivo: {e}")