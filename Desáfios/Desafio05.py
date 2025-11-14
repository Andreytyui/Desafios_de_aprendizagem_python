#Desáfio 05- Faça um programa que leia algo pelo teclado 
# E mostre na tel ao seu tipo primitivo e todas as 
# informações possiveis sobre ele.

digite= input ("Digite alguma coisa:")
print ("O tipo primitivo do valor escrito é ", type(digite))
print ("Só tem letras?", digite.isalpha() )
print ("Só tem números?", digite.isnumeric())
print ("Tem só espaços?", digite.isspace())
print ("Tem letras ou números?", digite.isalnum())
print ("Tem só número Decimal?", digite.isdecimal())
print("Está em maiúsculas?", digite.isupper())
print ("Está em minúsculas?", digite.islower())
print("Está capitalizada?",digite.istitle())