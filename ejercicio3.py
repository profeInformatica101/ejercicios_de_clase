'''
Escribe un programa que calcule 
el Índice de Masa Corporal (IMC) de una persona 
pidiéndole su peso en kilogramos y su altura en metros.

'''
print("dime tu peso")
peso =float(input())
#print(type(peso))

print("dime tu altura")
altura =float(input())

imc = peso / altura * altura

print("imc es ", imc)