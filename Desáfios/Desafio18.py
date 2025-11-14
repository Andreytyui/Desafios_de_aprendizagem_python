#Um professor quer sortear um dos seus alunos para apagar o quadro, 
# faça um programa que ajude ele, lendo o nome deles e escrevendo
#o nome do escolhido.
import random
aluno1= (input("Digite o número do primeiro aluno(a):"))
aluno2= (input("Digite o nome do segundo aluno(a):"))
aluno3= (input("Digite o nome do terceiro aluno(a):"))
aluno4= (input("Digite o nome do quarto aluno(a):"))

sorteio= random.choice ([aluno1,aluno2,aluno3,aluno4])

print ("O aluno(a) sorteado foi {}! boa sorte para apagar o quadro {}! HAHAHAHAHAHAHA!".format(sorteio,sorteio))
