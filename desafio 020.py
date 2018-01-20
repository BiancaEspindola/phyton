''' O mesmo professor quer que seja sorteado a ordem de apresetação de trabalhos
faça um programa que leia o nome de 4 alunos e mostre a ordem de apresentação'''
import random

n1 = str(input("Enter a first name :"))
n2 = str(input("Enter a second name: "))
n3 = str(input("Enter a third name: "))
n4 = str(input("Enter a fourth name: "))

names = [n1,n2,n3,n4]

random.shuffle(names)

print("Order of the draw: ")
print(names)