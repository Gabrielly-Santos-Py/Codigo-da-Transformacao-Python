# carro_eletrico_heranca.py

# A classe Carro deve ser definida (ou importada) antes
class Carro:
    def __init__(self, marca: str, modelo: str, ano: int):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        
    def exibir_info(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")

# Implementa Herança: CarroEletrico herda de Carro (Atividade 2)
class CarroEletrico(Carro):
    """
    Representa um carro elétrico, herdando de Carro e adicionando
    autonomia_bateria (em km).
    """
    def __init__(self, marca: str, modelo: str, ano: int, autonomia_bateria: int):
        # Chama o construtor da classe pai (Carro)
        super().__init__(marca, modelo, ano)
        # Adiciona o atributo exclusivo da classe filha
        self.autonomia_bateria = autonomia_bateria

    # Sobrescreve o método exibir_info para incluir a autonomia
    def exibir_info(self):
        # Chama o método da classe pai para reutilizar o código
        super().exibir_info() 
        print(f"Autonomia da Bateria: {self.autonomia_bateria} km")
        print(f"Tipo de motorização: Elétrica")

# Criação de um objeto CarroEletrico
meu_eletrico = CarroEletrico("Tesla", "Model 3", 2023, 550)

print("--- Informações do Carro Elétrico (Herança) ---")
meu_eletrico.exibir_info()

# Demonstra que os atributos herdados ainda funcionam
print(f"\nModelo do carro elétrico (atributo herdado): {meu_eletrico.modelo}")