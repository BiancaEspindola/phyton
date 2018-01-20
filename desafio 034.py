"""Escreva um programa que pergunte o salário de um funcinário e calcule o valor do novo salário """
salario = float(input("Digite o salário do funcionário: "))

if salario > 1250:
    salario = salario + (salario * 0.10)
else:
    salario = salario + (salario * 0.15)
print("O novo salário é de R${:.2f}".format(salario))