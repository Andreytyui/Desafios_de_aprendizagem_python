#Faça um programa que leia um número de 0 a 9999. 
# E mostre na tela cada um dos digitos separados.
#Ex: Digite um número: 1834
#Unidade:4
#Dezena:3
#Centena:8
#Milhar:1

num=input("Digite um número(de 0 a 9999):")
num= num.zfill(4)
print ("Unidade:",(num[3]))
print ("Dezena:",(num[2]))
print ("Centena:",(num[1]))
print ("Milhar:",(num[0]))