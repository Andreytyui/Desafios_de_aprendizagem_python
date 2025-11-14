#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trbalhos
# dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem
#sorteada.

import random
aluno1= (input("Digite o número do primeiro aluno(a):"))
aluno2= (input("Digite o nome do segundo aluno(a):"))
aluno3= (input("Digite o nome do terceiro aluno(a):"))
aluno4= (input("Digite o nome do quarto aluno(a):"))

sorteio=([aluno1,aluno2,aluno3,aluno4])

random.shuffle(sorteio)

print("O primeiro será {}, o segundo será {}, o terceiro será {}, e pro fim, o quarto será {}".format(sorteio[0],sorteio[1],sorteio[2],sorteio[3]))