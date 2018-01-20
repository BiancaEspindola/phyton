#Faça um algortimo que leia o salário de um funcionário e mostre o seu novo salário com 15% de aumento

salary = float(input("Enter the salary: "))
increase = salary * 0.15
salary = salary + increase

print("The new salary is: {}".format(salary))