#faça um algortimo que leia o preço de um numero e mostre seu novo preço com 5% de desconto

price = float(input("Enter a price of the product(R$): "))
discount = price * 0.05
price = price - discount

print("The new price is: {}".format(price))
