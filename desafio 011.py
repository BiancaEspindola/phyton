#Faça um programa que leia a altura e a largura de uma parede em metros, e calcule sua area e a quantidade
#de tinta a ser usada para pinta-la(um litro de tinta pinta uma area de 2m²)

height = float(input("Enter the height of the wall(value in meters): "))
width = float(input("Enter the width of the wall(value in meters): "))
area = height * width
wallPaint = area / 2

print("Wall Area: {} m² and the amount of wall paint: {}".format(area,wallPaint))
