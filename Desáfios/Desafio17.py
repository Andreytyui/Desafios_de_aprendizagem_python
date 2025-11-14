#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente 
#Desse ângulo.
from math import radians,sin,cos,tan
angulo= float(input("Digite o valor do ângulo:"))
radi= radians(angulo)
seno= sin(radi)
cosseno= cos(radi)
tangente= tan(radi)
print("o valor do ângulo é {:.1f},o seu seno é {:.1f}, seu cosseno é {:.1f} e por último, sua tangente é {:.1f}". format(angulo,seno,cosseno,tangente))