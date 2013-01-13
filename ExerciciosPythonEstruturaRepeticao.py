#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
#-------------------------------------------------------------------------------
# -- Quarta Lista -- 30/08/2012
#-------------------------------------------------------------------------------
print "-"*60+"\n1) Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.  \n"+"-"*60
#-------------------------------------------------------------------------------
while True:
    nota= int(raw_input("- Entre com uma nota: "))
    if nota>=0 and nota<=10: break
    print " A nota deve estar entre 0 e 10..."
print " - Você digitou a nota ",nota
#-------------------------------------------------------------------------------
print "-"*60+"\n2) Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.  \n"+"-"*60
#-------------------------------------------------------------------------------
nome = raw_input(" - Entre com o seu nome: ")
while True:
    senha = raw_input(" - Entre com a sua senha: ")
    if senha!=nome: break
    print " - Senha inválida! Não pode ser igual ao seu nome!"
#-------------------------------------------------------------------------------
print "-"*60+"\n3) Faça um programa que leia e valide as seguintes informações:\
Nome: maior que 3 caracteres;\
Idade: entre 0 e 150;\
Salário: maior que zero;\
Sexo: 'f' ou 'm';\
Estado Civil: 's', 'c', 'v', 'd';\n"+"-"*60
#-------------------------------------------------------------------------------
#Nome: maior que 3 caracteres
while True:
    nome = raw_input("- Entre com o seu nome: ")
    if len(nome)<3:
        print "Nome Inválido! Deve ser maior que 3 digitos."
        continue
    break
#Idade: entre 0 e 150
while True:
    idade = int(raw_input("-"+nome+", entre com a sua idade: "))
    if idade<0 or idade>150:
        print "Idade Inválida! Deve estar entre 0 e 150."
        continue
    break
#Salário: maior que zero
while True:
    salario = float(raw_input("-"+nome+", entre com o seu salario: "))
    if salario<0:
        print "Salário inválido! Deve ser maior que zero."
        continue
    break
#Sexo: 'f' ou 'm'
while True:
    sexo = raw_input("-"+nome+", entre com o seu sexo. (Apenas m ou f): ")
    if sexo!='f' and sexo!='m':
        print "Sexo inválido! Deve ser apenas 'm' ou 'f'."
        continue
    break
#Estado Civil: 's', 'c', 'v', 'd'
estados = 'scvd'
while True:
    estadoC = raw_input("-"+nome+" entre como seu estado civil: ")
    if estadoC not in estados:
        print "Estao Civil! Deve ser 's', 'c', 'v' ou 'd'."
        continue
    break
#-------------------------------------------------------------------------------
print "-"*60+"\n4) Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento. \n"+"-"*60
#-------------------------------------------------------------------------------
habA,habB,anos=80000,200000,0
while True:
    habA= habA*1.03
    habB= habB*1.015
    anos+=1
    if habA>=habB: break
print "- Demorou %d anos para a população A alcançar a B."%(anos)
print "- População de A: %d\n- População de B: %d"%(habA,habB)
#-------------------------------------------------------------------------------
print "-"*60+"\n5) Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.\n"+"-"*60
#-------------------------------------------------------------------------------
while True:
    habA=int(raw_input(" - Entre com o número da população A. "))
    taxA=float(raw_input(" - Entre com a taxa de crescimento da população A. "))
    habB=int(raw_input(" - Entre com a taxa de crescimento da população B. "))
    taxB=float(raw_input(" - Entre com o número da população A. "))
    anos=0
    while True:
        habA*=(1-taxA/100)
        habB*=(1-taxB/100)
        anos+=1
        if habA>=habB: break
    print "- Demorou %d anos para a população A alcançar a B."%(anos)
    print "- População de A: %f\n- População de B: %f"%(habA,habB)
    op=raw_input(" - Deseja continuar? (s) ou (n) : ")
    if op=='s': continue
    break
#-------------------------------------------------------------------------------
print "-"*60+"\n6) Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. Depois modifique o programa para que ele mostre os números um ao lado do outro.\n"+"-"*60
#-------------------------------------------------------------------------------
for i in range(1,21,1):
    print i

str1=""
for i in range(1,21,1):
    str1+=str(i)+" "
print str1
#-------------------------------------------------------------------------------
print "-"*60+"\n7) Faça um programa que leia 5 números e informe o maior número.\n"+"-"*60
#-------------------------------------------------------------------------------
n = int(raw_input(" - Entre com um número: "))
maior=n
for i in range(4):
    n = int(raw_input(" - Entre com um número: "))
    if maior<n: maior=n
print " O maior dos números: ",maior
#-------------------------------------------------------------------------------
print "-"*60+"\n8) Faça um programa que leia 5 números e informe a soma e a média dos números.\n"+"-"*60
#-------------------------------------------------------------------------------
n = int(raw_input(" - Entre com um número: "))
som, maior=n, n
for i in range(4):
    n = int(raw_input(" - Entre com um número: "))
    if maior<n: maior=n
    som+=n
print " O maior dos números: ",maior
print " Soma dos números: ",som
print " A média entre eles: ",float(som/5)
#-------------------------------------------------------------------------------
print "-"*60+"\n9) Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.\n"+"-"*60
#-------------------------------------------------------------------------------
for i in range(1,51,2):
    print " - ",i
#-------------------------------------------------------------------------------
print "-"*60+"\n10) Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.\n"+"-"*60
#-------------------------------------------------------------------------------
n1 = int(raw_input(" -Entre com um número inteiro: "))
n2 = int(raw_input(" -Entre com outro número inteiro: "))
for i in range(n1,n2,1):
    print "-",i
#-------------------------------------------------------------------------------
print "-"*60+"\n11) Altere o programa anterior para mostrar no final a soma dos números\n"+"-"*60
#-------------------------------------------------------------------------------
n1 = int(raw_input(" -Entre com um número inteiro: "))
n2 = int(raw_input(" -Entre com outro número inteiro: "))
som=0
for i in range(n1,n2,1):
    print "-",i
    som+=i
print "- A soma deles é: ",som
#-------------------------------------------------------------------------------
print "-"*60+"\n12) Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:\n \
Tabuada de 5:\n \
5 X 1 = 5\n \
5 X 2 = 10\n \
...\n \
5 X 10 = 50\n"+"-"*60
#-------------------------------------------------------------------------------
n = int(raw_input("- Entre com um número para calcular a tabuada:"))

for i in range(1,11,1):
    print "%dx%d=%d"%(i,n,(i*n))
#-------------------------------------------------------------------------------
print "-"*60+"\n13) Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem.\n"+"-"*60
#-------------------------------------------------------------------------------
b= int(raw_input("- Entre com a base: "))
e= int(raw_input("- Entre com o expoente: "))
if e!=0: 
    po=b
    for i in range(1,e,1):
        po*=b
else:
    po=0

print "%d^%d=%d"%(b,e,po)
#-------------------------------------------------------------------------------
print "-"*60+"\n14) Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares. \n"+"-"*60
#-------------------------------------------------------------------------------
par, impar = 0, 0
for i in range(10):
    n = int(raw_input(" - Entre com um número: "))
    if n%2==0: par+=1
    else: impar+=1
print "- %d números pares, %d números impares"%(par,impar)
#-------------------------------------------------------------------------------
print "-"*60+"\n15) A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo. \n"+"-"*60
#-------------------------------------------------------------------------------

def fib(i):
    a, b = 1, 1
    for y in range(i):
        print a
        c=a+b
        a,b=b,c

i = int(raw_input("- Entre com o um número: "))
fib(i)
#-------------------------------------------------------------------------------
print "-"*60+"\n16) A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série até que o valor seja maior que 500.  \n"+"-"*60
#-------------------------------------------------------------------------------
def fib():
    a, b = 1, 1
    while a<700:
        print a
        c=a+b
        a,b=b,c

fib()

