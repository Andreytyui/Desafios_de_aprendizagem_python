#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos 
#Doláres ela pode comprar.
#Considerando US 1,00 = R$3,27

dinheiro= float(input("Qual valor você tem em sua carteira agora mesmo?"))
conv= dinheiro/3.27

print("Com o valor R${:.2f}, você poderá comprar US${:.2f} doláres.".format(dinheiro,conv))