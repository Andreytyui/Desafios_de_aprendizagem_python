#Faça um programa que leia o comprimento do cateto adjacente de um
#Triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

from math import pow,sqrt
catadjacente= float(input("Digite o valor do cateto adjacente:"))
catoposto= float(input("Digite o valor do cateto oposto:"))
calculo= pow(catadjacente,2) +  pow (catoposto,2)
raiz= sqrt(calculo)
print("O valor do comprimento da hipotenusa é {:.1f}".format(raiz))