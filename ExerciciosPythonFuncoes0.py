#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
#-------------------------------------------------------------------------------
# -- Lista Funções --
#-------------------------------------------------------------------------------
print "-"*60+"\n1) Implementar duas funções:\n\
▪ Uma que converta temperatura em graus Celsius para Fahrenheit.\n\
▪ Outra que converta temperatura em graus Fahrenheit para Celsius.\n\
Lembrando que: F = (9/5)*C32\n"+"-"*60
#-------------------------------------------------------------------------------

def celsiusToFah(c=0):
    return (9/5)*c+32 

def fahToCelsius(f=0):
    return (f-32)*5/9

print celsiusToFah(c=34)
print celsiusToFah(125)
print celsiusToFah(100)
print celsiusToFah(0)
print fahToCelsius(f=0)
print fahToCelsius(180)
#-------------------------------------------------------------------------------
print "-"*60+"\n2) Implementar uma função que retorne verdadeiro se o número for primo (falso caso contrário). Testar de 1 a 100.\n"+"-"*60
#-------------------------------------------------------------------------------
def isPrimo(n):
    for i in range(2,n-1,1):
        if n%i==0: return False
    return True

for i in range(1,101,1):
    p= '' if isPrimo(i) else 'não' 
    print "%d %s é primo."%(i,p)
#-------------------------------------------------------------------------------
print "-"*60+"\n3) Implementar uma função que receba uma lista de listas de comprimentos quaisquer e retorne uma lista de uma dimensão.\n"+"-"*60
#-------------------------------------------------------------------------------
def toList(*objeto):
    return objeto

print toList(1,2,3,4,5,6,7,8)
print toList(1,2,'a','v','b',7,8)
print toList(1,'a')
print toList(True,True,False,True)
#-------------------------------------------------------------------------------
print "-"*60+"\n4) Implementar uma função que receba um dicionário.\n"+"-"*60
#-------------------------------------------------------------------------------
def toDic(**objeto):
    return objeto

print toDic(a=1,b=2,c=3,d=4,e=5,f=6,g=7,h=8)
print toDic(a=1,b='a')
print toDic(a=True,b=True,c=False,d=True)
#-------------------------------------------------------------------------------
print "-"*60+"\n4.2) Implementar uma função que receba um dicionário e retorne a soma, a média e a variação dos valores.\n"+"-"*60
#-------------------------------------------------------------------------------
def toDic(**objeto):
    som,var=0,0.0
    for o in objeto: som+=objeto[o]
    avg=float(som/len(objeto))
    for o in objeto: var+= avg-objeto[o]
    return objeto,avg,float(var/len(objeto))

print toDic(a=9,b=8,c=3,d=4,e=5,f=6,g=7,h=8)
print toDic(a=15,c=2,d=1,f=41,g=75,h=28)
#-------------------------------------------------------------------------------
print "-"*60+"\n5) Escreva uma função que:\n\
▪ Receba uma frase como parâmetro.\n\
▪ Retorne uma nova frase com cada palavra com as letras invertidas.\n\
\n"+"-"*60
#-------------------------------------------------------------------------------
def inverseWords(frase):
    f=""
    for word in frase.split(" "):
        str=""
        for i in range(-1,-len(word)-1,-1): str+=word[i]
        f+=str+" "
    return f

print inverseWords("Receba uma frase como parametro")
#-------------------------------------------------------------------------------
print "-"*60+"\n6) Crie uma função que:\n\
▪ Receba uma lista de tuplas (dados), um inteiro (chave, zero por padrão igual) e um booleano (reverso, falso por padrão).\n\
▪ Retorne dados ordenados pelo item indicado pela chave e em ordem decrescente sereverso for verdadeiro.\n"+"-"*60
#-------------------------------------------------------------------------------
def sort(chave,reverso=False,*tuples):
    tu=list(tuples[chave])
    tu = sorted(tu)
    if reverso: tu = reversed(tu)
    return tuple(tu)

print sort(1,True,(4,5,6,2,3),(4,0,2,3,9),(5,6,3),(0,2,1,-2))  


