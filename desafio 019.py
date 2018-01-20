#um prefessor quer sortear um dos seus quatro alunos pra apagar o quadro. Faça um programa que ajude
#elelendo o nome dos lunos, e escreva o nome escolhido
import random

n1 = str(input("Enter a first name: "))
n2 = str(input("Enter  second name: "))
n3 = str(input("Enter a third name: "))
n4 = str(input("Enter a fourth name: "))
name = [n1,n2,n3,n4]
print("The chosen student is: {} ".format(random.choice(name)))