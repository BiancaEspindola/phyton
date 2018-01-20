"""Faça um programa que leia uma frase no teclado mostre quantas vezes aparece a letra A, em que posição ela aparece a primeira vez
e a ultima posição que ela aparece"""
frase = str(input("Digite uma frase : ")).strip()

print("A frase possui {} letras 'A'".format(frase.lower().count('a')))
print("Posição da primeira letra 'A': {}".format(frase.lower().find('a')))
print("Ultima posição em que 'A' aparece {}".format(frase.lower().rfind('a')))