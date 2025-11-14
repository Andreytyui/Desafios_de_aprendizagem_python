#Escreva um programa que leia um valor em metros e o exiba
#convertido em centímetros e milímetros.

metros= int(input("Digite um valor em metro:"))
cm= metros*100
mm= cm*10

print("o valor {}m em centimetros é {}cm.\n E o valor {}cm em milímetros é {}mm".format(metros,cm,cm,mm))