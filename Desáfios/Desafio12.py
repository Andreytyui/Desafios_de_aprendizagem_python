#faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua
# área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma 
#área de 2m quadrados.

largura= float(input("Digite a largura da parede:"))
altura= float(input("Digite a altura da parede:"))
#Calcula a altura e largura para dar a área.
area= altura*largura
#Calcula a quantidade de tinta necessária.
tinta= area/2

print("O valor da área é precisamente {:.1f} metros quadrados, e a quantidade de tinta para pintar toda essa área é de {:.1f} litros de tinta ".format(area,tinta))

