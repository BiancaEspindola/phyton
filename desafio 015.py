#escreva um programa que pergunte a quantidade de km percorridos por um carro e a quantidade de dias pelos
#quais ele foi alugado. Calcule o preço a pagar,sabendo que o carro custa R$60 por dia e R$0,15 por km rodado

km = float(input("Enter the number of the km rotated: "))
days = int(input("Enter the number of days with the car: "))
price = (km * 1.15) + (days * 60)

print("The price to pay is: R${:.2f}".format(price))