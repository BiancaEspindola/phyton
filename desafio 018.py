#faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno etangente desse angulo
import math

angle = float(input("Enter the angle in degrees: "))
sin = math.sin(math.radians(angle))
cos = math.cos(math.radians(angle))
tan = math.tan(math.radians(angle))


print("Sin = {:.2f}, Cos = {:.2f} and Tan = {:.2f}".format(sin,cos,tan))