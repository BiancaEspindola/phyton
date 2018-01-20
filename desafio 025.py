"""Faça um programa que leia o nome de um pessoa e diga se tem SILVA no nome"""
nome = str(input("Digite um nome: ")).strip()
print("Esse nome possui Silva?")
print('silva' in nome.lower())
