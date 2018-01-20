#faça um programa que leia o comprimento do cateto oposto e do adjacente de um triangulo retangulo e mostre
#o comprimento da hipotenusa

import math

oppositeSide = float(input("Enter the opposite side: "))
adjacentSide = float(input("Enter the adjacent side: "))

print("The hypotenuse is: {:.3f}".format(math.hypot(oppositeSide,adjacentSide)))