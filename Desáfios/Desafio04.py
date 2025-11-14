#Desáfio 04 - Fazer com que exiba ao digitar dois números, A soma de N1 e N2 seja S.


n1= int(input("Digite um número:"))
n2= int(input("Digite outro número:"))
somatoria= n1 + n2

# print ("A soma entre", n1,"e", n2,"é",somatoria)

print ("A soma entre {} e {} vale {} ".format (n1, n2, somatoria))