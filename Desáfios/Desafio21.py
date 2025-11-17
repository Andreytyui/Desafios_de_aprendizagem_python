#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas
#O nome com todas minúsculas.
#Quantas letras ao todo (sem considerar espaços).
#Quantas letras tem o primeiro nome.

nome = input("Digite seu nome completo: ")

print("Este é seu nome em maiúsculo:", nome.upper())
print("Este é seu nome em minúsculo:", nome.lower())

nome_sem_espacos = nome.replace(" ", "")
print("Seu nome tem ao todo {} letras.".format(len(nome_sem_espacos)))

primeiro_nome = nome.split()[0]
print("Seu primeiro nome tem exatamente {} caracteres.".format(len(primeiro_nome)))
