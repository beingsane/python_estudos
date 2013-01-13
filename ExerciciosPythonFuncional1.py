#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
#-------------------------------------------------------------------------------
print "-"*60+"\n1. Implementar um gerador de números primos\n"+"-"*60
#-------------------------------------------------------------------------------
def isPrimo(x):
    for i in range(2,x-1):
        if x%i==0: return False
    return True
print filter(isPrimo,range(20))
#-------------------------------------------------------------------------------
print "-"*60+"\n2. Implementar o gerador de números primos como uma expressão.\n"+"-"*60
#-------------------------------------------------------------------------------
# -- 1º Estudo: 
def isPrimo(x):
    return not any([i for i in range(2,x-1) if x%i==0])

for x in range(0,20):
    print str(x)+(" é primo" if isPrimo2(x) else " não é primo")

# -- 2º Estudo: 
isPrimo2 = lambda x: not any([i for i in range(2,x-1) if x%i==0]) 

for x in range(0,20):
    print str(x)+(" é primo" if isPrimo2(x) else " não é primo")

# -- 3º Estudo:
print [x for x in range(0,20) if isPrimo2(x)]

# -- Ultimo Estudo:
print [x for x in range(0,20) if (lambda x: not any([i for i in range(2,x-1) if x%i==0]))(x) ]

# -- aceitando um valor n
n = int(raw_input("- Entre com o limite da sequencia de primos: "))
primos =  [x for x in range(n) if (lambda x: not any([i for i in range(2,x-1) if x%i==0]))(x) ]
print primos

## 3 exercicios?
rgb = lambda r=0,g=0,b=0:  '#%02x%02x%02x' % (r, g, b)
print rgb(200, 200, 255)

#-------------------------------------------------------------------------------
print "-"*60+"\n4. Implementar um gerador que leia um arquivo e retorne uma lista de tuplas com os dados (o separador de campo do arquivo é vírgula), eliminando as linhas vazias.\n"+"-"*60
#-------------------------------------------------------------------------------
arquivo = "nome,lucas;idade,21;sexo,masculino"
#-- 1º Estudo - Iterativo:
dic={}
lista = arquivo.split(";")
for s in lista:
    campo,valor=s.split(",")
    dic[campo]=valor
print dic

#-- 2º Estudo - retorna lista de tuples :  [('nome', 'lucas'), ('idade', '21'), ('sexo', 'masculino')] :

print [tuple(a.split(",")) for a in arquivo.split(";")]

#-- 3º Estudo - retorna dicionario {'idade': '21', 'sexo': 'masculino', 'nome': 'lucas'}:
dic={}
for c in [a.split(",") for a in arquivo.split(";")] : dic[c[0]]=c[1]
print dic

