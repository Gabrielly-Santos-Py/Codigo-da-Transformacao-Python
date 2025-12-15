import requests

# --- Função de Requisição Genérica ---

def fazer_requisicao_e_processar(url):
    """
    Função genérica para demonstrar o fluxo de requisição e tratamento.
    """
    try:
        print(f"Fazendo requisição para: {url}")
        
        # 1. Tenta a requisição
        resposta = requests.get(url, timeout=5)
        
        # 2. Verifica o status HTTP (ponto 3 - tratamento de erros de resposta)
        # Se for 4xx ou 5xx, levanta um HTTPError
        resposta.raise_for_status() 
        
        # 3. Se deu certo, exibe o resultado
        print("\n✅ Requisição HTTP bem-sucedida.")
        print(f"Conteúdo JSON recebido: {resposta.json()}")
        return resposta.json()
        
    except requests.exceptions.RequestException as e:
        # Captura e trata todos os erros de requisição/conexão/status
        print(f"\n❌ Falha no Processamento da API. Erro: {e}")
        return None

# Teste com uma API pública simples (Ex: API de fatos sobre gatos)
fazer_requisicao_e_processar("https://catfact.ninja/fact")