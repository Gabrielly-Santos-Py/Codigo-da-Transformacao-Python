import os
import requests # type: ignore
import json

# --- Configurações ---
# Recomendo definir a variável de ambiente OPENWEATHER_API_KEY em vez de deixar a chave
API_KEY = os.environ.get('OPENWEATHER_API_KEY', 'SUA_CHAVE_AQUI')
CIDADE = 'London'  # Cidade para a qual você quer a previsão
URL_BASE = 'http://api.openweathermap.org/data/2.5/weather'

# --- 1 & 2 & 3: Consumo da API com Tratamento de Erros ---

def obter_previsao(cidade, api_key):
    params = {
        'q': cidade,
        'appid': api_key,
        'units': 'metric', # Para obter a temperatura em Celsius
        'lang': 'pt' # Para obter a descrição em português
    }
    
    # Validação simples da chave de API para evitar requisições desnecessárias
    if not api_key or api_key == 'SUA_CHAVE_AQUI':
        print("[ERRO] API key ausente. Defina OPENWEATHER_API_KEY ou substitua API_KEY no arquivo.")
        return None

    response = None

    try:
        # Tenta realizar a requisição HTTP
        print(f"Buscando dados para {cidade}...")
        response = requests.get(URL_BASE, params=params, timeout=10)
        response.raise_for_status() # Levanta uma exceção para códigos de status HTTP 4xx/5xx
        
        # Converte a resposta JSON
        try:
            dados = response.json()
        except (json.JSONDecodeError, ValueError):
            print("\n[ERRO DE DADOS] Resposta inválida da API (Não é JSON).")
            return None
        
        # Filtra e exibe informações específicas (Ponto 2)
        temperatura = dados['main']['temp']
        condicao = dados['weather'][0]['description']
        umidade = dados['main']['humidity']
        
        print("\n--- Previsão do Tempo ---")
        print(f"📍 Cidade: {cidade.upper()}")
        print(f"🌡️ Temperatura Atual: {temperatura}°C")
        print(f"☁️ Condição Climática: {condicao.capitalize()}")
        print(f"💧 Umidade: {umidade}%")
        print("---------------------------")
        
    except requests.exceptions.HTTPError as err_http:
        # Trata erros HTTP (ex: 401 Unauthorized, 404 Not Found)
        status = None
        if hasattr(err_http, 'response') and err_http.response is not None:
            status = err_http.response.status_code
        elif response is not None:
            status = response.status_code

        print(f"\n[ERRO HTTP] Falha na requisição. Código: {status}.")
        if status == 401:
            print("Verifique sua API Key (401 Unauthorized).")
        elif status == 404:
            print(f"Cidade '{cidade}' não encontrada (404).")
            
    except requests.exceptions.ConnectionError:
        # Trata falhas de conexão (ex: sem internet)
        print("\n[ERRO DE CONEXÃO] Falha ao conectar à API. Verifique sua internet.")
        
    except requests.exceptions.Timeout:
        # Trata se a requisição demorar muito
        print("\n[TIMEOUT] A requisição excedeu o tempo limite.")
        
    except requests.exceptions.RequestException as err:
        # Trata outros erros de requisição
        print(f"\n[ERRO GERAL] Ocorreu um erro: {err}")
        
    except KeyError:
        # Trata se a estrutura JSON mudar ou estiver incompleta
        print("\n[ERRO DE ESTRUTURA] Estrutura de dados inesperada na resposta da API.")

# Execução
obter_previsao(CIDADE, API_KEY)