"""recebe três retas e diz se podem ou não formar um triângulo"""
a = float(input("Valor de A: "))
b = float(input("Valor de B: "))
c = float(input("Valor de C: "))

if b + c > a and c + a > b and a + b > c:
    print("Pode formar um triângulo!")
else:
    print("Não pode formar um triângulo!")