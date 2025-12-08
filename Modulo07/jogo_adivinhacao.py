# jogo_adivinhacao.py

import random
import math # Importado, mas será usado para algo simples como arredondamento/abs, se necessário.

def jogar_adivinhacao():
    """Implementa o jogo de adivinhação."""
    
    # 1. Gera um número aleatório entre 1 e 100
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    limite_tentativas = 7
    acertou = False
    
    print(f"--- Jogo de Adivinhação ---")
    print(f"Tente adivinhar o número secreto entre 1 e 100.")
    print(f"Você tem {limite_tentativas} tentativas.")

    while tentativas < limite_tentativas and not acertou:
        try:
            # Pede o palpite do jogador
            palpite = int(input(f"\nTentativa {tentativas + 1}: Digite seu palpite: "))
            tentativas += 1

            # 2. Compara o palpite com o número secreto
            if palpite == numero_secreto:
                acertou = True
                print(f"\n🎉 **PARABÉNS!** Você acertou o número {numero_secreto} em {tentativas} tentativas!")
            elif palpite < numero_secreto:
                print("Seu palpite é **muito baixo**. Tente um número maior.")
            else:
                print("Seu palpite é **muito alto**. Tente um número menor.")
                
            # Exemplo de uso de 'math': Se o jogador estivesse muito longe, 
            # poderíamos usar math.fabs() para calcular a distância absoluta,
            # mas vamos manter o código simples como o pedido inicial.

        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")
            # Não conta como tentativa se a entrada for inválida
            tentativas -= 1 

    # Se o loop terminar sem acerto
    if not acertou:
        print(f"\nGAME OVER! Suas {limite_tentativas} tentativas acabaram.")
        print(f"O número secreto era: **{numero_secreto}**")

# Inicia o jogo
jogar_adivinhacao()