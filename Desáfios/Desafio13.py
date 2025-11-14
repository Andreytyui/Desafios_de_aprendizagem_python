#Faça um algoritmo que leia o preço de um produto e mostre
# seu novo preço, com 5% de desconto

preco= float(input("Digite o preço do produto:"))
desconto= (preco - 5)/100
preco_desconto= preco - desconto

print("O valor do produto é {:.2f}, e com desconto é de {:.2f}, aproveite suas compras!".format(preco,preco_desconto))
