#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário
#com 15% de aumento.

salario= float(input("Diga qual é o seu salário atualmente:"))
aumento= (salario * 15)/100
salario_novo= salario + aumento

print("Parabéns! O seu salário {:.1f} recebeu um aumento! E seu novo salário é de atualmente {:.1f}".format(salario,salario_novo))