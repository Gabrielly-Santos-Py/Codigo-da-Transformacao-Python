## Atividade 2: Implemente herança: Crie uma classe CarroEletrico que herda de Carro e adiciona autonomia_bateria.

from Carro import Carro  # importa a classe base Carro definida em Carro.py

# Reutilizamos a classe Carro da Atividade 1 (pode ser definida no mesmo arquivo)

class CarroEletrico(Carro):
    """
    Representa um carro elétrico, herdando de Carro
    e adicionando o atributo autonomia_bateria.
    """

    def __init__(self, marca, modelo, autonomia_bateria):
        """
        Inicializa Carro (marca, modelo) e o atributo exclusivo
        autonomia_bateria.
        """
        # Chama o construtor da classe pai (Carro)
        super().__init__(marca, modelo)
        self.autonomia_bateria = autonomia_bateria

    def exibir_info(self):
        """
        Sobrescreve o método para incluir a autonomia da bateria.
        """
        super().exibir_info() # Chama o método da classe pai
        print(f"Autonomia da Bateria: {self.autonomia_bateria} km")

if __name__ == '__main__':
    # Exemplo de Uso:
    meu_eletrico = CarroEletrico("Tesla", "Model 3", 450)
    print("\n--- Informações do Carro Elétrico ---")
    meu_eletrico.exibir_info()