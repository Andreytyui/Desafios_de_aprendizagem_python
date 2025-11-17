#Faça um programa que leia uma frase pelo teclado e mostre:
#Quantas vezes aparece a letra "A"
#Em que posição ela aparece pela primeira vez.
#Em que posição ela aparece pela ultima vez.

frase= input("Digite alguma frase:")

print("A letra A aparece {} vezes".format(frase.count("a")))

print("Ela aparece pela primeira vez na posição {}".format(frase.find("a")))

print("Ela termina na posição {}".format(frase.rfind("a")))