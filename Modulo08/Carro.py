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

