import requests # type: ignore

# --- 3: Tratamento de Erros de Conexão ---

def testar_tratamento_de_erros(url_teste):
    try:
        # Tentativa com uma URL propositalmente inválida (protocolo errado)
        print(f"Tentando acessar: {url_teste}")
        response = requests.get(url_teste, timeout=5)
        response.raise_for_status()
        print("Requisição bem-sucedida.")
        
    except requests.exceptions.ConnectionError:
        # Este é o bloco que captura problemas de conexão (rede indisponível, DNS, etc.)
        print("\n🛑 ERRO CAPTURADO (ConnectionError): Não foi possível estabelecer a conexão de rede.")
        print("Possível causa: URL inválida, servidor offline, ou problema de internet.")
        
    except requests.exceptions.Timeout:
        # Captura se demorar demais
        print("\n⚠️ ERRO CAPTURADO (Timeout): A requisição demorou muito e foi cancelada.")

    except requests.exceptions.RequestException as e:
        # Captura qualquer outro erro que o requests possa gerar
        print(    nf"\n❗ ERRO CAPTURADO (RequestException): Ocorreu um erro geral na requisição: {e}") # pyright: ignore[reportUndefinedVariable]
        
    else:
        print(f"Código de Status: {response.status_code}")
        
# Teste com uma URL que provavelmente causará um ConnectionError (ou um Timeout)
testar_tratamento_de_erros(http://este.dominio.nao.existe.na.internet)