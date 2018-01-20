"""escreva um programa que leia  velocidade de um caro se ele ultrapassar 80k/h. mostre um mensagem
dizendo ue ele foi multado"""
velocidade = float(input("Qual a velicidade? "))

if velocidade > 80.0:
    print("Você foi multado, o limite era 80km/h e você estava {:.2f} km/h".format(velocidade))
else:
    print("Você está dentro da velocidade permitida, o limite é de 80 km/h e você estava a {:.2f} km/h".format(velocidade))