#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
#-------------------------------------------------------------------------------
# -- Primeira Lista --
#-------------------------------------------------------------------------------
print "-"*60+"\n1) Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento. Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.\n"+"-"*60
#-------------------------------------------------------------------------------
str1= raw_input(" - Entre com uma palavra: ")
str2= raw_input(" - Entre com outra palavra: ")

print "String 1:",str1
print "String 2:",str2
print "Tamanho de ",str1,": ",len(str1)," caracteres"
print "Tamanho de ",str2,": ",len(str2)," caracteres"

if len(str1)!=len(str2):
    print "As duas strings são de tamanhos diferentes."
else:
    print "As duas strings têm o mesmo tamanho."

if str1!=str2:
    print "As duas strings possuem conteúdo diferentes."
else:
    print "As duas strings possuem o mesmo conteúdo."
#-------------------------------------------------------------------------------
print "-"*60+"\n2) Nome ao contrário em maiúsculas. Faça um programa que permita ao usuário digitar o seu nome e em seguida mostre o nome do usuário de trás para frente utilizando somente letras maiúsculas. Dica: lembre−se que ao informar o nome o usuário pode digitar letras maiúsculas ou minúsculas.\n"+"-"*60
#-------------------------------------------------------------------------------
nome= raw_input(" - Entre com um nome: ")
nome = nome.upper()
nom=""
for s in range(-1,-len(nome)-1,-1):
    nom+=nome[s]
print nom
#-------------------------------------------------------------------------------
print "-"*60+"\n3) Nome na vertical. Faça um programa que solicite o nome do usuário e imprima-o na vertical\n"+"-"*60
#-------------------------------------------------------------------------------
nome= raw_input(" - Entre com um nome: ")
for i in range(len(nome)):
    print nome[i]   
#-------------------------------------------------------------------------------
print "-"*60+"\n4) Nome na vertical em escada. Modifique o programa anterior de forma a mostrar o nome em formato de escada.\n \
F\n \
FU\n \
FUL\n \
FULA\n \
FULAN\n \
FULANO\n"+"-"*60
#-------------------------------------------------------------------------------
nome= raw_input(" - Entre com um nome: ")
nome = nome.upper()
for s in range(len(nome)+1):
    print nome[:s]
#-------------------------------------------------------------------------------
print "-"*60+"\n\5) Nome na vertical em escada invertida. Altere o programa anterior de modo que a escada seja invertida\n \
FULANO\n \
FULAN\n \
FULA\n \
FUL\n \
FU\n \
F"+"-"*60
#-------------------------------------------------------------------------------
nome= raw_input(" - Entre com um nome: ")
nome = nome.upper()
for s in range(len(nome)+1):
    print nome[s:]

#-------------------------------------------------------------------------------
# -- Segunda Lista --
#-------------------------------------------------------------------------------
print "-"*60+"\n1) Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.\n"+"-"*60
#-------------------------------------------------------------------------------
lista=[]
for i in range(5):
    lista.append(int(raw_input(" Entre com um número inteiro: ")))
for i in range(5):
    print "lista[%d]=%d"%(i,lista[i])
#-------------------------------------------------------------------------------
print "-"*60+"\n2) Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.\n"+"-"*60
#-------------------------------------------------------------------------------
lista=[]
for i in range(10):
    lista.append(int(raw_input(" - Entre com um número: ")))
for i in range(-1,-len(lista)-1,-1):
    print "lista[%d]=%d"%(i,lista[i])
#-------------------------------------------------------------------------------
print "-"*60+"\n3) Faça um Programa que leia 4 notas, mostre as notas e a média na tela.\n"+"-"*60
#-------------------------------------------------------------------------------
notas=[]
media=0
for i in range(4):
    notas.append(float(raw_input(" - Entre o a "+str(i+1)+"ª nota: ")))
for i in range(len(notas)):
    media+=notas[i]
media/=len(notas)
print " - A média das notas é: %f"%(media)

#-------------------------------------------------------------------------------
print "-"*60+"\n4) Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.\n"+"-"*60
#-------------------------------------------------------------------------------
lista=[]
vogais='aeiou'
for i in range(10):
    lista.append(raw_input(" - Entre com um caracter: "))
print " - Consoantes:"
count=0
for c in lista:
    if c.lower() not in vogais:
        print " - ",c
        count+=1
print " - Foram ao todo %d consoantes. "%(count)
#-------------------------------------------------------------------------------
print "-"*60+"\n5) Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.\n"+"-"*60
#-------------------------------------------------------------------------------
vetor=[]
pares=[]
impares=[]
for i in range(20):
    n=int(raw_input(" - Entre com um número inteiro: "))
    vetor.append(n)
    if n%2==0:
        pares.append(n)
    else:
        impares.append(n)
print " ---- "
print " -  Você digitou: ",vetor
print " -  Pares: ",pares
print " -  Ímpares:",impares
print " ---- "
#-------------------------------------------------------------------------------
print "-"*60+"\n6) Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.\n"+"-"*60
#-------------------------------------------------------------------------------
medias=[]
for i in range(10):
    print "Entre com as notas do aluno (%d)"%(i+1) 
    media=0
    for y in range(4):
        n = float(raw_input(" - "+str(y+1)+"ª nota: "))
        media+=n
    media/=4
    medias.append(media)
print " - Alunos aprovados:"
for i in range(len(medias)):
    if medias[i]>=7 : print " - Aluno %d com média %f"%(i+1,medias[i])
#-------------------------------------------------------------------------------
print "-"*60+"\n7) Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.\n"+"-"*60
#-------------------------------------------------------------------------------
vetor=[]
soma, mul= 0, 1
for i in range(5):
    n = int(raw_input(" -Entre com um número: "))
    vetor.append(n)
    soma+=n
    mul*=n
print " ---- "
print " - Você entrou com: ",vetor
print " - Somas deles: ",soma
print " - Multiplicação deles: ",mul
print " ---- "
#-------------------------------------------------------------------------------
print "-"*60+"\n8) Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.\n"+"-"*60
#-------------------------------------------------------------------------------
alt, idad=[], []
for i in range(5):
    print " - Pessoa ",i
    alt.append(float(raw_input(" -Entre com a sua altura: ")))
    idad.append(int(raw_input(" -Entre com a sua Idade: ")))
print "\tAltura\tIdade"
for i in range(-1,-5,-1):
    print "\t%f\t%i"%(alt[i],idad[i])
#-------------------------------------------------------------------------------
print "-"*60+"\n9) Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.\n"+"-"*60
#-------------------------------------------------------------------------------
vetor=[]
for i in range(10):
    n = int(raw_input(" - Entre com um número: "))
    vetor.append(n)
som=0
for n in vetor:
    som+=(n*n)
print " - A soma dos quadrados dos elementos é ",som
#-------------------------------------------------------------------------------
print "-"*60+"\n10) Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.\n"+"-"*60
#-------------------------------------------------------------------------------
vetor1=[]
vetor2=[]
vetInter=[]
print " - Preenchendo o primeiro vetor: - "
for i in range(10):
    vetor1.append(int(raw_input(" -Entre com um número: ")))

print " - Preenchendo o segundo vetor: - "
for i in range(10):
    vetor2.append(int(raw_input(" -Entre com um número: ")))
    
for i,y in zip(vetor1,vetor2):
    vetInter.append(i)
    vetInter.append(y)

print " - Original 1:"
print "",vetor1
print " - Original 2:"
print "",vetor2
print " - Intercalado:"
print "",vetInter
