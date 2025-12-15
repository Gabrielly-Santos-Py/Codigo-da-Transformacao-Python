import requests

# --- Configurações ---
# OBS: O TMDB requer uma API Key diferente do OpenWeatherMap
TMDB_API_KEY = 'SUA_CHAVE_TMDB_AQUI' 
FILME_ID = 550 # Exemplo: O Clube da Luta
URL_TMDB_BASE = f'https://api.themoviedb.org/3/movie/{FILME_ID}'

# --- Desafio Extra: TMDB ---

def buscar_dados_filme(filme_id, api_key):
    parametros = {
        'api_key': api_key,
        'language': 'pt-BR' # Pede as informações em Português
    }
    
    try:
        response = requests.get(URL_TMDB_BASE, params=parametros)
        response.raise_for_status()
        dados_filme = response.json()
        
        # Filtra e exibe os dados
        titulo = dados_filme.get('title', 'N/A')
        sinopse = dados_filme.get('overview', 'Sinopse indisponível.')
        
        # Extrai os nomes dos gêneros
        generos = [g['name'] for g in dados_filme.get('genres', [])]
        
        print("\n--- Detalhes do Filme ---")
        print(f"🎬 Título: {titulo}")
        print(f"🎭 Gêneros: {', '.join(generos) or 'N/A'}")
        print(f"📝 Sinopse:\n{sinopse}")
        print("-------------------------")
        
    except Exception as e:
        print(f"\n[ERRO TMDB] Falha ao buscar dados do filme: {e}")
        
# Execução
buscar_dados_filme(FILME_ID, TMDB_API_KEY)