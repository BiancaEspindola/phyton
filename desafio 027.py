"""Faça um programa que leia o nome completo de uma pessoa e retorne o primeiro e o ultimo nome """

nome = str(input("Digite seu nome completo: ")).strip()
pNome = nome.find(' ')
fNome = nome.rfind(' ')
print("Seu primeiro nome é {}, e seu ultimo nome é: {}".format(nome[:pNome], nome[fNome+1:]))
