#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
#-------------------------------------------------------------------------------
# -- Lista Funções --
#-------------------------------------------------------------------------------
print "-"*60+"\n1) Faça um programa para imprimir:\n\
        1\n\
        2   2\n\
        3   3   3\n\
        .....\n\
        n   n   n   n   n   n  ... n\n\
    para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha. \n"+"-"*60
#-------------------------------------------------------------------------------
def pyramid(n):
    str1=""
    for i in range(0,n+1,1):
        for col in range(0,i,1): str1+=str(i)+" "
        str1+="\n"
    return str1

#ou...
def pyramid1(n):
    for i in range(1, n+1): 
        print((str(i)+" ")*i)

print pyramid(5)
print pyramid(3)
print pyramid1(9)
#-------------------------------------------------------------------------------
print "-"*60+"\n2) Faça um programa para imprimir:\n\
        1\n\
        1   2\n\
        1   2   3\n\
        .....\n\
        1   2   3   ...  n\n\
    para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha.  \n"+"-"*60
#-------------------------------------------------------------------------------
def pyramid2(n):
    str1=""
    for i in range(0,n+1,1):
        for col in range(1,i+1,1): str1+=str(col)+" "
        str1+="\n"
    return str1

print pyramid2(5)
print pyramid2(3)
print pyramid2(9)
#-------------------------------------------------------------------------------
print "-"*60+"\n3) Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.\n"+"-"*60
#-------------------------------------------------------------------------------
def som(x,y,z):
    return x+y+z

print som(2,3,34)
print som(1,4,9)
#-------------------------------------------------------------------------------
print "-"*60+"\n4) Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.\n"+"-"*60
#-------------------------------------------------------------------------------
def isPOrN(x):
    return 'P' if x>0 else 'N'

for i in range(-5,5,1):
    print "%d is %s"%(i,isPOrN(i))
#-------------------------------------------------------------------------------
print "-"*60+"\n5) Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas. \n"+"-"*60
#-------------------------------------------------------------------------------
def somaImposto(taxaImposto,custo):
    return custo+custo*float(taxaImposto/100)

print somaImposto(5.0,100)
print somaImposto(12.0,100)
#-------------------------------------------------------------------------------
print "-"*60+"\n6) Faça um programa que converta da notação de 24 horas para a notação de 12 horas. Por exemplo, o programa deve converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros. Deve haver pelo menos duas funções: uma para fazer a conversão e uma para a saída. Registre a informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M. Assim, a função para efetuar as conversões terá um parâmetro formal para registrar se é A.M. ou P.M. Inclua um loop que permita que o usuário repita esse cálculo para novos valores de entrada todas as vezes que desejar. \n"+"-"*60
#-------------------------------------------------------------------------------
def conv(hour,min1):
    if hour==24: hour=0
    time = ":"+str(min1)+(" P.M." if hour >= 12 else " A.M.") 
    if hour < 12 : time= str(hour)+time
    else: time= str(hour-12)+time
    return time

def vqToT(time='00:00'):
    hour,min1= time.split(":")
    print time," => ",conv(int(hour),int(min1)) 

vqToT("12:34")
vqToT("7:45")
vqToT("15:12")
vqToT("24:00")
#-------------------------------------------------------------------------------
print "-"*60+"\n7) Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação de uma conta. O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e passar estes valores para a função valorPagamento, que calculará o valor a ser pago e devolverá este valor ao programa que a chamou. O programa deverá então exibir o valor a ser pago na tela. Após a execução o programa deverá voltar a pedir outro valor de prestação e assim continuar até que seja informado um valor igual a zero para a prestação. Neste momento o programa deverá ser encerrado, exibindo o relatório do dia, que conterá a quantidade e o valor total de prestações pagas no dia. O cálculo do valor a ser pago é feito da seguinte forma. Para pagamentos sem atraso, cobrar o valor da prestação. Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso. \n"+"-"*60
#-------------------------------------------------------------------------------
def valorPagamento(prest,dias):
    return prest+prest*(0.05*dias)

total,qtde=0,0
while True:
    prest = float(raw_input("- Entre com o valor da prestação ou 0 para sair: "))
    if prest ==0 : break
    dias = int(raw_input("- Entre com o número de dias: "))
    prest = valorPagamento(prest,dias)
    print "-- R$%d --"%(prest)
    total+=prest
    qtde+=1
print
print "-- Relatório: --"
print "================"
print "Foram pagas %d prestações no valor total de %d"%(qtde,total)
print "================"
#-------------------------------------------------------------------------------
print "-"*60+"\n8) Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.\n"+"-"*60
#-------------------------------------------------------------------------------
def numOfDigits(numero):
    return len(str(numero))

lista=[1,2,45,567,892,123456]
for l in lista:
    print "%d tem %d digitos."%(l,numOfDigits(l))
#-------------------------------------------------------------------------------
print "-"*60+"\n9) Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.\n"+"-"*60
#-------------------------------------------------------------------------------
def rever(numero):
    return str(numero)[::-1]

lista=[1,2,45,567,892,123456]
for l in lista:
    print "%d -> %s "%(l,rever(l))
#-------------------------------------------------------------------------------
print "-"*60+"\n10) Jogo de Craps. Faça um programa de implemente um jogo de Craps. O jogador lança um par de dados, obtendo um valor entre 2 e 12. Se, na primeira jogada, você tirar 7 ou 11, você um 'natural' e ganhou. Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de 'craps' e você perdeu. Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,este é seu 'Ponto'. Seu objetivo agora é continuar jogando os dados até tirar este número novamente. Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente. \n"+"-"*60
#-------------------------------------------------------------------------------
import random
def lanD():
    faces=[1,2,3,4,5,6]
    random.shuffle(faces)
    return faces[len(faces)/2]

jogN, ponto = 1,1
while True:
    r = lanD()+lanD()
    print " - %d ..."%(r)
    if jogN==1:
        if r in [7,11]: 
           print "Você ganhou!"
           break
        if r in [2,3,12]:
           print "Craps! Você perdeu!"
           break 
        ponto, jogN = r, jogN+1
        print "- Ponto: ",ponto
        continue
    jogN+=1
    if r==7:
        print "Você perdeu!"
        break
    if r==ponto and jogN!=1:
        print "Você ganhou!"
        break 
#-------------------------------------------------------------------------------
print "-"*60+"\n11) Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no formato D de mesPorExtenso de AAAA. Opcionalmente, valide a data e retorne NULL caso a data seja inválida. \n"+"-"*60
#-------------------------------------------------------------------------------
mes={1:"Janeiro", 2:"Fevereiro", 3:"Março", 4:"Abril", 5:"Maio", 6:"Junho", 7:"Julho", 8:"Agosto", 9:"Setembro", 10:"Outubro", 11:"Novembro", 12:"Dezembro"}

def toStringMonth(date="22/02/2012"):
    global mes
    d,m,a=date.split("/")
    return str(d)+" de "+mes[int(m)]+" de "+str(a)

print toStringMonth("22/02/2012")
print toStringMonth("07/08/1991")
print toStringMonth("31/09/1985")
#-------------------------------------------------------------------------------
print "-"*60+"\n12) Embaralha palavra. Construa uma função que receba uma string como parâmetro e devolva outra string com os carateres embaralhados. Por exemplo: se função receber a palavra python, pode retornar npthyo, ophtyn ou qualquer outra combinação possível, de forma aleatória. Padronize em sua função que todos os caracteres serão devolvidos em caixa alta ou caixa baixa, independentemente de como foram digitados. \n"+"-"*60
#-------------------------------------------------------------------------------
import random

def shuffleWord(word):
    word= list(word.lower())
    random.shuffle(word)
    toReturn=""
    for s in word: toReturn+=s
    return toReturn

print shuffleWord("python")
print shuffleWord("Embaralha")
print shuffleWord("Construa")
#-------------------------------------------------------------------------------
print "-"*60+"\n13) Desenha moldura. Construa uma função que desenhe um retângulo usando os caracteres ‘+’ , ‘−’ e ‘| ‘. Esta função deve receber dois parâmetros, linhas e colunas, sendo que o valor por omissão é o valor mínimo igual a 1 e o valor máximo é 20. Se valores fora da faixa forem informados, eles devem ser modificados para valores dentro da faixa de forma elegante. \n"+"-"*60
#-------------------------------------------------------------------------------
def inter(n):
    if n<1: return 3
    if n>20: return 20
    return n

def drawRec(l,c):
    l,c=inter(l),inter(c)
    str1="- retangulo de "+str(l)+"x"+str(c)+":\n"
    for linha in range(1,l):
        if linha in [1,l-1]: str1+="+"+("-"*(c-2))+"+\n"
        else: str1+="|"+(" "*(c-2))+"|\n"
    return str1
        
print drawRec(4,5)
print drawRec(23,3)
print drawRec(-23,-3)
#-------------------------------------------------------------------------------
print "-"*60+"\n14) Quadrado mágico. Um quadrado mágico é aquele dividido em linhas e colunas, com um número em cada posição e no qual a soma das linhas, colunas e diagonais é a mesma. Por exemplo, veja um quadrado mágico de lado 3, com números de 1 a 9:\n\
\n\
    8  3  4 \n\
    1  5  9\n\
    6  7  2\n\
\n\
    Elabore uma função que identifica e mostra na tela todos os quadrados mágicos com as características acima. Dica: produza todas as combinações possíveis e verifique a soma quando completar cada quadrado. Usar um vetor de 1 a 9 parece ser mais simples que usar uma matriz 3x3. \n"+"-"*60
#-------------------------------------------------------------------------------
n = int(raw_input("- Entre com a dimensão do quadrado mágico (Deve ser impar): "))
rows,cols=n,n
maxi=n*n
quadrado=[]

def preencher(n):
    r,c=n,n
    global quadrado
    for i in range(r):
        l=[]
        for y in range(c): l.append(-1)
        quadrado.append(l)

preencher(n)

print quadrado
num, row , col = 0, 0, cols/2
quadrado[row][col]=num
num+=1
print quadrado
while True:
    colAnt,rowAnt=col,row
    col-=1
    if col<0: col=cols-1
    row-=1
    if row<0: row=rows-1
    while True:
        if quadrado[row][col]!=-1:  
            col, row = colAnt, rowAnt+1
            if row>=rows: row = rows-1
        else:
            quadrado[row][col] = num
            break
    num+=1
    print quadrado
    if num==maxi: break

def showSquare():
    global quadrado
    str1=""
    for r in range(0,len(quadrado)):
        for c in range(0,len(quadrado[r])):
            str1+=str(quadrado[r][c])+"\t"
        str1+="\n"
    print str1

showSquare()

