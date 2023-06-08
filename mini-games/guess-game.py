import random
number = random.randint(0,20)
escolha = None
tentativas = 0
chance = 5
# Este é um jogo de adivinhar o número
while chance > 0 and escolha != number:
    print("Você tem "+str(chance)+" chances para adivinhar o número de 0 a 20")
    escolha = int(input())
    tentativas = tentativas + 1
    chance = chance - 1
    if escolha > number:
        print("O número é menor que", escolha)
    elif escolha < number:
        print("O número é maior que", escolha)
    else:
        print("O NÚMERO É:",escolha,"\nVocê acertou após",tentativas,"tentativa(s)")
    if escolha != number:
        if chance == 0:
            print("Suas chances esgotaram")