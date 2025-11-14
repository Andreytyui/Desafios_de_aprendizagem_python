#Desenvolva um programa que leia as duas notas de um aluno
# E calcule e mostre a sua média

n1= int(input("Digite a Nota 01:"))
n2= int(input("Digite a Nota 02:"))

s= n1+n2
m= s/2

print("A soma de suas duas notas são {}.\n E sua média é {}".format(s,m))