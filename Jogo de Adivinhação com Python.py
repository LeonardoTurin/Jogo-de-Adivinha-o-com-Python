import random
def jogo_adivinhação():
    print('Bem vindo ao jogo')
numero_secreto = random.randint(1,100)
tentativas = 0
max_tentativas = 5

while tentativas < max_tentativas:
        palpite = int(input("Tente adivinhar o número: "))

        if palpite == numero_secreto:
            print("Parabéns! Você acertou!")
            break
        elif palpite > numero_secreto:
            print("Tente um número menor.")
        else:
            print("Tente um número maior.")

        tentativas += 1
if tentativas == max_tentativas:
    print(f'Fim de jogo. O número secreto era {numero_secreto}')





