"""Desevolva um programa que pergunte a distâcia de uma viagem em km e calcule o preço cobrado por passagem
R$ 0,50 por km ate 200 km e R$ 0,45 para viagens mais longas"""
km = float(input("Qual a distância que será percorrida em km: "))

if km <= 200:
    preco = km * 0.50
else:
    preco = km * 0.45
print("Preço da passagem é: R$ {:.2f}".format(preco))
