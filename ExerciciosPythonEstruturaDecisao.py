#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
#-------------------------------------------------------------------------------
# -- Terceira Lista -- 30/08/2012
#-------------------------------------------------------------------------------
print "-"*60+"\n1) Faça um Programa que peça dois números e imprima o maior deles\n"+"-"*60
#-------------------------------------------------------------------------------
n1 = int(raw_input("- Entre com um número: "))
n2 = int(raw_input("- Entre com um número: "))
if n1>n2:
    print "%d > %d"%(n1,n2)
else:
    print "%d > %d"%(n2,n1)
#-------------------------------------------------------------------------------
print "-"*60+"\n2) Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo. \n"+"-"*60
#-------------------------------------------------------------------------------
n = int(raw_input("- Entre com um número: "))
if n<0:
    print "%d é negativo."%(n)
else:
    print "%d é positivo."%(n)
#-------------------------------------------------------------------------------
print "-"*60+"\n3) Faça um Programa que verifique se uma letra digitada é 'F' ou 'M'. Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.\n"+"-"*60
#-------------------------------------------------------------------------------
sexo = raw_input("- Entre com o seu sexo. (F-Feminino e M-Masculino) ")
sexo = sexo.upper()
if sexo!='F' and sexo !='M':
    print "%s não é um sexo válido."%(sexo)
elif sexo =='M':
    print "%s - Masculino."%(sexo)
else:
    print "%s - Feminino."%(sexo)
#-------------------------------------------------------------------------------
print "-"*60+"\n4) Faça um Programa que verifique se uma letra digitada é vogal ou consoante.\n"+"-"*60
#-------------------------------------------------------------------------------
vogais='aeiou'
num='1234567890'

while True:
    letra = raw_input("- Entre com uma letra ")
    if len(letra)==1 and letra not in num: break
    print " Apenas uma letra..."

letra = letra.lower()

if letra not in vogais:
    print "%s é uma consoante"%(letra)
else:
    print "%s é uma vogal"%(letra)
#-------------------------------------------------------------------------------
print "-"*60+"\n5) Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:\
    A mensagem 'Aprovado', se a média alcançada for maior ou\ igual a sete;\
    A mensagem 'Reprovado', se a média for menor do que sete;\
    A mensagem 'Aprovado com Distinção', se a média for igual a dez. \n"+"-"*60
#-------------------------------------------------------------------------------
def pedirNota():
    while True:
        nota= int(raw_input("- Entre com uma nota: "))
        if nota>=0 and nota<=10: return nota
        print " A nota deve estar entre 0 e 10..."

nota1 = pedirNota()
nota2 = pedirNota()
media = (nota1+nota2)/2
if media==10:
    print "com média: %d, o aluno foi aprovado com Distinção "%(media)
elif media>=7:
    print "com média: %d, o aluno foi aprovado "%(media)
else:
    print "com média: %d, o aluno foi reprovado "%(media)
#-------------------------------------------------------------------------------
print "-"*60+"\n6) Faça um Programa que leia três números e mostre o maior deles.  \n"+"-"*60
#-------------------------------------------------------------------------------
n1= int(raw_input("- Entre com o primeiro número: "))
n2= int(raw_input("- Entre com o segundo número: "))
n3= int(raw_input("- Entre com o terceiro número: "))

if n1>n2 and n1>n3:
    if n2>n3:
        print "(%d,%d,%d) "%(n3,n2,n1)
    else:
        print "(%d,%d,%d) "%(n2,n3,n1)
else:
    if n2>n3:
        if n1>n3:
            print "(%d,%d,%d) "%(n3,n1,n2)
        else:
            print "(%d,%d,%d) "%(n1,n3,n2)
    else:
        if n1>n2:
            print "(%d,%d,%d) "%(n2,n1,n3)
        else:
            print "(%d,%d,%d) "%(n1,n2,n3)
#-------------------------------------------------------------------------------
print "-"*60+"\n7) Faça um Programa que leia três números e mostre o maior e o menor deles.   \n"+"-"*60
#-------------------------------------------------------------------------------
n1= int(raw_input("- Entre com o primeiro número: "))
n2= int(raw_input("- Entre com o segundo número: "))
n3= int(raw_input("- Entre com o terceiro número: "))

if n1>n2 and n1>n3:
    if n2>n3:
        print "%d é o menor e %d, maior "%(n3,n1)
    else:
        print "%d é o menor e %d, maior "%(n2,n1)
else:
    if n2>n3:
        if n1>n3:
            print "%d é o menor e %d, maior "%(n3,n2)
        else:
            print "%d é o menor e %d, maior "%(n1,n2)
    else:
        if n1>n2:
            print "%d é o menor e %d, maior "%(n2,n3)
        else:
            print "%d é o menor e %d, maior "%(n1,n3)
#-------------------------------------------------------------------------------
print "-"*60+"\n8) Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato. .   \n"+"-"*60
#-------------------------------------------------------------------------------
p1= int(raw_input("- Entre com o preço do produto 1: "))
p2= int(raw_input("- Entre com o preço do produto 2: "))
p3= int(raw_input("- Entre com o preço do produto 3: "))

if p1<p2 and p1<p3:
    print "%d é o menor dos preços"%(p1)
elif p2<p3 and p2<p1:
    print "%d é o menor dos preços"%(p2)
else:
    print "%d é o menor dos preços"%(p3)
#-------------------------------------------------------------------------------
print "-"*60+"\n9) Faça um Programa que leia três números e mostre-os em ordem decrescente.\n"+"-"*60
#-------------------------------------------------------------------------------
n1= int(raw_input("- Entre com o primeiro número: "))
n2= int(raw_input("- Entre com o segundo número: "))
n3= int(raw_input("- Entre com o terceiro número: "))
if n1>n2 and n1>n3:
    if n2>n3:
        print "(%d,%d,%d) "%(n1,n2,n3)
    else:
        print "(%d,%d,%d) "%(n1,n3,n2)
else:
    if n2>n3:
        if n1>n3:
            print "(%d,%d,%d) "%(n2,n1,n3)
        else:
            print "(%d,%d,%d) "%(n2,n3,n1)
    else:
        if n1>n2:
            print "(%d,%d,%d) "%(n3,n1,n2)
        else:
            print "(%d,%d,%d) "%(n3,n2,n1)
#-------------------------------------------------------------------------------
print "-"*60+"\n10) Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N-Noturno. Imprima a mensagem 'Bom Dia!', 'Boa Tarde!' ou 'Boa Noite!' ou 'Valor Inválido!', conforme o caso. \n"+"-"*60
#-------------------------------------------------------------------------------
ts='VMNvmn'

while True:
    turno= raw_input("- Entre com o seu turno\n\
    - M - Matutino, V - Vespertino ou N - Noturno: ")
    if turno in ts: break
    print " Turno inválido..."

if turno in 'Mm':
    print "Bom Dia! :)"
elif turno in 'Vv':
    print "Boa Tarde! :)"
elif turno in 'Nn':
    print "Boa Noite! :/"
else:
    print " Um erro ocorreu :("

