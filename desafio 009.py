#faça um programa que leia um número interio qualquer e mostre sua tabuada

number = int(input("Enter a number: "))
x = 1

while x <= 10:
    print("{} x {} = {}".format(number,x,number*x))
    x = x + 1
