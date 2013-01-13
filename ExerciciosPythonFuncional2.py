#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
#-------------------------------------------------------------------------------
# -- Lista Programação Funcional--
#-------------------------------------------------------------------------------
print "-"*60+"\n1) Faça um programa para imprimir:\n1\n 2   2\n  3   3   3\n .....\n  n   n   n   n   n   n  ... n\npara um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha. \n"+"-"*60
#-------------------------------------------------------------------------------
pypi = lambda n:  reduce ( lambda x,i : str(x)+"\n"+((str(i)+" ")*i) , range(1, n+1) )
print pypi(5)
#0i...
n=5
pypi2 = "\n".join([ ((str(i)+" ")*i) for i in range(1, n+1) ])
print pypi2
#-------------------------------------------------------------------------------
print "-"*60+"\n2) Faça um programa para imprimir:\n 1\n 1   2\n 1   2   3\n .....\n 1   2   3   ...  n\n para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha. \n"+"-"*60
#-------------------------------------------------------------------------------
pip = lambda x,i : str(x)+"\n"+ " ".join([str(i) for i in range(1,i+1,1)]) 
pypi = lambda n:  reduce ( pip , range(1, n+1) )
print pypi(5)
#-------------------------------------------------------------------------------
print "-"*60+"\n3) Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.\n"+"-"*60
#-------------------------------------------------------------------------------
som = lambda x=0,y=0,z=0 : x+y+z
print som(2,3,34)
print som(1,4,9)
#-------------------------------------------------------------------------------
print "-"*60+"\n4) Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.\n"+"-"*60
#-------------------------------------------------------------------------------
print ", ".join( [ "%d is %s"%(i, (i>0 and 'P') or 'N' ) for i in range(-5,5,1)] )
#-------------------------------------------------------------------------------
print "-"*60+"\n5) Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas. \n"+"-"*60
#-------------------------------------------------------------------------------
somaImposto = lambda taxaImposto,custo : custo*float(1 + taxaImposto/100.0)
print somaImposto(5.0,100)
print somaImposto(12.0,100)
#-------------------------------------------------------------------------------
print "-"*60+"\n12) Embaralha palavra. Construa uma função que receba uma string como parâmetro e devolva outra string com os carateres embaralhados. Por exemplo: se função receber a palavra python, pode retornar npthyo, ophtyn ou qualquer outra combinação possível, de forma aleatória. Padronize em sua função que todos os caracteres serão devolvidos em caixa alta ou caixa baixa, independentemente de como foram digitados. \n"+"-"*60
#-------------------------------------------------------------------------------
import random

def shuffleWord(word):
    word= list(word.lower())
    random.shuffle(word)
    return reduce( lambda s,a: s+a, word)

print shuffleWord("python")
print shuffleWord("Embaralha")
print shuffleWord("Construa")
#-------------------------------------------------------------------------------
print "-"*60+"\n13) Desenha moldura. Construa uma função que desenhe um retângulo usando os caracteres ‘+’ , ‘−’ e ‘| ‘. Esta função deve receber dois parâmetros, linhas e colunas, sendo que o valor por omissão é o valor mínimo igual a 1 e o valor máximo é 20. Se valores fora da faixa forem informados, eles devem ser modificados para valores dentro da faixa de forma elegante. \n"+"-"*60
#-------------------------------------------------------------------------------

inter = lambda n: 3 if n<1 else 20 if n>20 else n

def drawRec(l,c):
    l,c=inter(l),inter(c)
    str1="- retangulo de %d x %d :\n"%(l,c)
    for linha in range(1,l):
        str1+=  "%s %s %s\n"%( ("+","-"*(c-2),"+") if linha in [1,l-1]  else  ("|"," "*(c-2),"|") )
    return str1
        
print drawRec(4,5)
print drawRec(23,3)
print drawRec(-23,-3)
#-------------------------------------------------------------------------------
print "-"*60+"\n1) Implementar duas funções:\n\
▪ Uma que converta temperatura em graus Celsius para Fahrenheit.\n\
▪ Outra que converta temperatura em graus Fahrenheit para Celsius.\n\
Lembrando que: F = (9/5)*C32\n"+"-"*60
#-------------------------------------------------------------------------------

celsiusToFah = lambda c=0:(9/5)*c+32 
fahToCelsius = lambda f=0:(f-32)*5/9

print celsiusToFah(c=34)
print celsiusToFah(125)
print celsiusToFah(100)
print celsiusToFah(0)
print fahToCelsius(f=0)
print fahToCelsius(180)
#-------------------------------------------------------------------------------
print "-"*60+"\n2) Implementar uma função que retorne verdadeiro se o número for primo (falso caso contrário). Testar de 1 a 100.\n"+"-"*60
#-------------------------------------------------------------------------------
isPrimo = lambda n: '' if [i for i in range(2,n-1) if n%i==0]==[] else 'não'
print "\n".join( ["%d %s é primo."%(i,isPrimo(i)) for i in range(1,101,1) ] )
def toDic(**objeto):
    som = reduce( lambda x,y: x+y , objeto.itervalues() )
    avg = float(som/len(objeto))
    var = reduce( lambda o,p: o+(p-avg) , objeto.itervalues() )
    return objeto,avg,float(var/len(objeto))

print toDic(a=9,b=8,c=3,d=4,e=5,f=6,g=7,h=8)
print toDic(a=15,c=2,d=1,f=41,g=75,h=28)
#-------------------------------------------------------------------------------
print "-"*60+"\n5) Escreva uma função que:\n\
▪ Receba uma frase como parâmetro.\n\
▪ Retorne uma nova frase com cada palavra com as letras invertidas.\n\
\n"+"-"*60
#-------------------------------------------------------------------------------
inverseWords = lambda frase: " ".join( [s[::-1] for s in frase.split(" ")] )
print inverseWords("Receba uma frase como parametro")
#-------------------------------------------------------------------------------
print "-"*60+"\n6) Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. Depois modifique o programa para que ele mostre os números um ao lado do outro.\n"+"-"*60
#-------------------------------------------------------------------------------
print "\n".join([ str(i) for i in range(1,21) ])
print " ".join([ str(i) for i in range(1,21) ])
#-------------------------------------------------------------------------------
print "-"*60+"\n9) Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.\n"+"-"*60
#-------------------------------------------------------------------------------
print ",".join([ str(i) for i in range(1,51,2)])
#-------------------------------------------------------------------------------
print "-"*60+"\n10) Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.\n"+"-"*60
#-------------------------------------------------------------------------------
n1 = int(raw_input(" -Entre com um número inteiro: "))
n2 = int(raw_input(" -Entre com outro número inteiro: "))
print ",".join( [str(i) for i in range(n1,n2)] )
#-------------------------------------------------------------------------------
print "-"*60+"\n11) Altere o programa anterior para mostrar no final a soma dos números\n"+"-"*60
#-------------------------------------------------------------------------------
n1 = int(raw_input(" -Entre com um número inteiro: "))
n2 = int(raw_input(" -Entre com outro número inteiro: "))
num = [i for i in range(n1,n2)] 
som = reduce( lambda x,y:x+y, num)
print "-Os números são %s\n A soma deles é: %d" %(str(num),som)
#-------------------------------------------------------------------------------
print "-"*60+"\n12) Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:\nTabuada de 5:\n5 X 1 = 5\n5 X 2 = 10\n...\n5 X 10 = 50\n"+"-"*60
#-------------------------------------------------------------------------------
n = int(raw_input("- Entre com um número para calcular a tabuada:"))
print "Tabuada de %d"%n
tab = [ "%d x %d = %d"%(i,n,(i*n)) for i in range(1,11) ]
print "\n".join(tab)
#-------------------------------------------------------------------------------
print "-"*60+"\n13) Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem.\n"+"-"*60
#-------------------------------------------------------------------------------
b= int(raw_input("- Entre com a base: "))
e= int(raw_input("- Entre com o expoente: "))
po = 0 if e==0 else reduce( lambda i,y: i*y, [b]*e)
print "%d^%d=%d"%(b,e,po)
#-------------------------------------------------------------------------------
print "-"*60+"\n15) A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo. \n"+"-"*60
#-------------------------------------------------------------------------------
fib = lambda i : i if i<2 else fib(i-1)+fib(i-2)

i = int(raw_input("- Entre com o um número: "))
print fib(i)
print "- termos: %s"% ",".join([ str(fib(i)) for i in range(1,6) ])



