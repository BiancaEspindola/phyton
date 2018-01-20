"""escreva um programa que faça o computador pensar em um numero intero de 0 a 5 e peça para o usuariotentar descobrir o numero
escolhido pelo computador"""
import random
number = random.randint(1, 5)

print("Sorteamos um número de 1 a 5, tente adivinhar qual é")
tentativa = int(input("Digite o número: "))

if tentativa == number:
    print("Parabéns, você acertou!! o número era {}".format(number))
else:
    print("Você errou, o número era: {}".format(number))


