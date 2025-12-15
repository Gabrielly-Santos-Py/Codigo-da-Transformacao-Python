<<<<<<< HEAD
# carro_base.py

class Carro:
    """
    Representa um carro com marca e modelo, incluindo um método para exibir 
    informações e personalização da exibição do objeto.
    """
    
    # Método especial de inicialização (Construtor) - Atividade 3
    def __init__(self, marca: str, modelo: str, ano: int):
        """Inicializa os atributos do carro."""
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        
    # Método para exibir informações (Atividade 1)
    def exibir_info(self):
        """Exibe a marca e o modelo do carro."""
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")

    # Método especial para representação em string (__str__) - Atividade 3
    def __str__(self):
        """Retorna uma representação legível do objeto Carro."""
        return f"Carro: {self.marca} {self.modelo} ({self.ano})"

# Criação de um objeto
meu_carro = Carro("Toyota", "Corolla", 2022)

# Usando o método exibir_info()
print("--- Informações detalhadas (exibir_info) ---")
meu_carro.exibir_info()

print("\n--- Exibição como String (__str__) ---")
# Usando print() que invoca automaticamente __str__
print(meu_carro)
=======
class Carro:
	"""
	Classe base que representa um carro genérico.
	"""

	def __init__(self, marca, modelo):
		self.marca = marca
		self.modelo = modelo

	def exibir_info(self):
		"""Exibe informações básicas do carro."""
		print(f"Marca: {self.marca}")
		print(f"Modelo: {self.modelo}")

>>>>>>> 8e4fb37646846699e5cc1a1a14ea2f015cee3fde
