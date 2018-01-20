'''crie um programa que lei um nome completo de um pessoa e mostre: o nome com todas as letras maiusculas
todas minusculas quantas letras tem ao tod se considerar os espaços quantas letras tem no primeiro nome'''
name = str(input("Enter a name: ")).strip()
print("Nome em Maiúsculas: {}".format(name.upper()))
print("Nome em minúsculas: {}".format(name.lower()))
print("Número Total de letras do seu nome: {}".format(len(name) - name.count(' ')))
palavras = name.split()
print("Seu nome {} possui {} letras".format(palavras[0], len(palavras[0])))
