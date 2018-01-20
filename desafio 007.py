#desenvolva um programa que leia duas notas de um aluno, calcule e mostre sua média

first_grade = float(input("Enter the student's first grade: "))
second_grade = float(input("Enter the student's second grade: "))

average_notes = (first_grade + second_grade)/2

print("Average student notes: {:.2f}".format(average_notes))