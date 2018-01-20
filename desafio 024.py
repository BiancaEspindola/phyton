"""Crie um programa que leia o nome de uma cidade e diga se ele começa ou  não com nome de santo"""

nome = str(input("Digite o nome da cidade: "))
palavras = nome.split()
print("Começa com o nome Santo?")
print('santo' in palavras[0].lower())