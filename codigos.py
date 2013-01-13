#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-


#-------------------------------------------------------------------------------
# -- Básicos --
#-------------------------------------------------------------------------------


#prints com variaveis e entradas de dados
rept=40
print "-"*rept

print "Bem vindo ao %s" %("python")
user =  raw_input('Entre com o seu login:')
print "Bem vindo %s" %(user)
password = int(raw_input("Entre com a senha:"))
print "Você digitou a senha: %d" %(password)

print "-"*rept

nome = raw_input('Ola! Qual o seu nome? ')
print 'Muito prazer %s!!'%nome
n1 = float(raw_input('Entre com o primeiro numero:'))
n2 = float(raw_input('Entre com o segundo numero:'))
soma = n1 + n2
print 'A soma dos número %(n1)s! e %(n2)s! é %(soma)s!' %vars()

raw_input('Press ENTER to continue...\n')
print "-"*rept

print " - Vamos conhecer as coleções em python:"
print "- lists: a=[1,2,3,4]"
a=[1,2,3,4]
print " a[0] %d" %(a[0])
print " a[2] %d" %(a[2])
print " a[2:] ",a[2:]
print " a[:3] ",a[:3]
print "- dictionaries: d={'ovo':'galinha', 'leite':'vaca', 'la':'ovelha'}"
d={'ovo':'galinha', 'leite':'vaca', 'lã':'ovelha'}
print " Quem dá ovos? d['ovo']=",d['ovo']
print " Quem dá leite? d['leite']=",d['leite']
print " Quem dá lã? d['lã']=",d['lã']

raw_input('Press ENTER to continue...\n')
print "-"*rept

nome = raw_input(" - Olá! Qual é o seu nome?")
print " - Muito prazer "+nome

n1 = float(raw_input(" - Entre com a primeira nota: "))
n2 = float(raw_input(" - Entre com a segunda nota: "))
n3 = float(raw_input(" - Entre com a terceira nota: "))
media = (n1+n2+n3)/3
print
print " - Sua média foi:",media
if media>7 :
   print " * Parabens! Você foi aprovado!"
else:
   print " * Que azar, você for reprovado!"
print

raw_input('Press ENTER to continue...\n')
print "-"*rept

numero = int(raw_input(" - Insira um número qualquer inteiro: "))
if numero>0 :
	print " * Você digitou um número positivo."
elif numero<0 :
	print " * Você digitou um número negativo."
else:
	print " * Você digitou zero."

raw_input('Press ENTER to continue...\n')
print "-"*rept

n1 = float(raw_input(" - Entre com o primeiro número: "))
n2 = float(raw_input(" - Entre com o segundo número: "))

if n2==0 :
	print " * O denominador não pode ser zero"
else:
	resultado = str(n1+n2)
	print " * n1/n2=",resultado
	
resultado = "O denominador não pode ser zero" if n2==0 else " * n1/n2="+str(n1+n2)
print resultado

raw_input('Press ENTER to continue...\n')
print "-"*rept

colecao = ['a','b','c','d','e','f','g']
print "- Coleção: ",colecao
print "- 'a' existe na coleção" if 'a' in colecao else "- 'a' não existe na coleção"
print "- 'b' existe na coleção" if 'b' in colecao else ""
print "- 'k' existe na coleção" if 'k' in colecao else "- 'k' não existe na coleção"

lista = [1, 2, 3, 4, 5]
item = int(raw_input('Escolha um numero dentro da seguinte lista:\n'+str(lista)+'\n'))
if item in lista:
    print 'Você escolheu',str(item)
else:
    print 'Este numero nao esta na lista'

raw_input('Press ENTER to continue...\n')
print "-"*rept

var = input("Informe uma variavel para ser analisada: ")
tipo = type(var)
if tipo == int:
    print 'Você infomrou um numero inteiro.'
elif tipo == float:
    print 'Você infomrou um numero ponto flutuante.'
elif tipo == str:
    print 'Você infomrou uma string.'
elif tipo == dict:
    print 'Você infomrou um dicionario.'
elif tipo == list:
    print 'Você infomrou uma lista.'
elif tipo == tuple:
    print 'Você infomrou uma tupla.'
else:
    print 'Desconheço esse tipo de variável.'
print

raw_input('Press ENTER to continue...\n')
print "-"*rept



filename = raw_input(" Entre com o nome do arquivo")
try:
	arq = open(filename,'r')
except IOError, e:
	print 'file open error',e
else:
	#será executado caso não ocorra a exception
	for el in arq:
		print el,
	arq.close()

print

contador=3
while contador != 0:
	print "%i..."%(contador)
	contador=contador-1
print "BOOM!!"

palavra = raw_input(" - Entre com uma frase: ")
contador=0
total=0
while contador<len(palavra):
	if palavra[contador]==' ':
		total+=1
	contador+=1
else:
	print " - São %i espaços em branco"%(total)

print
print "----------------------\nFor in.\n---------------------------------------"
print

smashing_pumpkins = {'Gish':1991, 'Siamese Dream':1993, 'Mellon Collie':1995}

for item in smashing_pumpkins.items():
	 print item

for album,ano in smashing_pumpkins.items():
	 print 'O album',album,'foi lançado em',ano

print
print "----------------------\nFor aninhados.\n---------------------------------------"
print

listas_nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for lista_num in listas_nums:
    # For externo, responsável por percorrer pegar a lista de números dentro da lista
    print 'Encontrei a lista',lista_num
    print '   Essa lista é composta por:',
    for num in lista_num:
        # For interno, responsável por percorrer os números dentro de cada lista.
        print num,
    print ''


for lista_num in listas_nums:
    tamanho = len(lista_num)
    soma = 0
    for num in lista_num:
        soma = soma + num
    media = float(soma)/tamanho
    print 'A média da lista', lista_num, 'é:',media


print '-'*30
print 

#isso...
for x in range(1,11):
    for y in range(x+1,11):
        print '%i, %i'%(x,y)

# por virar isso... 0.0!

from itertools import combinations
 
for x,y in combinations(range(1,11), 2):
    print '%i, %i'%(x,y)

print '-'*30
print 

lista1 = [1,2,3]
lista2 = [7, 5, 3, 4, 1]
 
for item1 in lista1:
    print 'procurando por',item1,':',
    for item2 in lista2:
        if item1 == item2:
            print 'Encontrado!'
            break
    else:    
        print 'Não encontrado...'

def busca_letra():
    contador = 0
    for letra in palavra:
        if letra == 'a':
            contador += 1
    print 'Na palavra',palavra,'exitem',contador,'ocorrencias da letra a'

palavra = 'teste'
busca_letra()
palavra = 'reutilizacao'
busca_letra()
palavra = 'codigo'
busca_letra()  


def calcula_media(notas):
    total = 0
    tamanho = 0
    for nota in notas:
        total += nota
        tamanho += 1

    total = float(total)/tamanho
    print 'Media:', total

for aluno in notas:
    print 'Aluno',aluno,
    calcula_media(notas[aluno])  


faltas = {'aluno1':2, 'aluno2':3, 'aluno3':7, 'aluno4':11, 'aluno5':0, 'aluno6':10}

notas = {'aluno1':[5,6,5], 'aluno2':[7,8,6], 'aluno3':[6,6,8], 'aluno4':[5,9,8], 'aluno5':[5,6,3], 'aluno6':[6,6,6]}


def calcula_media(notas):
    total = 0
    tamanho = 0
    for nota in notas:
        total += nota
        tamanho += 1

    total = float(total)/tamanho
    print 'Media:', total

for aluno in notas:
    print 'Aluno',aluno,
    calcula_media(notas[aluno])  

#similar ao ... em java
def teste_args(*args):
     print 'args =',args

teste_args(1,2,3,4,5,6,7,8,9)
teste_args(1,2,3,4)
teste_args("a","s")

def soma(*args):
     resultado = 0
     for numero in args:
         resultado = resultado + numero
     print 'resultado =',resultado

soma(1,2)
soma(1,2,3)
soma(1,2,3,4,5,6,7,8,9,10)


# érnia monstruosa:
def teste():
     return True, 2

flag, numero = teste()
print flag
print numero


#cuidado com as globais
x = 1
def altera_x():
     global x
     print 'valor global:',x
     x = 10
     print 'valor global:',x

print 'x:',x
altera_x()
print 'x:',x


#None
#O None é o vazio do Python, geralmente utilizado para inicializar variáveis. #O valor booleano do None é false, dessa forma podemos testar se uma variável #está vazia ou não:
x = None
print x
if x:
   print 'none e true'
else:
   print 'none e false'


print '-'*30
print 

i=15
# \ separa os comandos em mais de uma linha para rganização
if i>9 and \
   i<20:
	print " i está entre 9 e 20"


print '-'*30
print 

#swap:
x, y = 2,4
print x
print y

x,y=y,x
print x
print y


temp = int(raw_input('Entre com a temperatura: '))
if temp < 0:
    print 'Congelando...'
elif 0 <= temp <= 20:
    print 'Frio'
elif 21 <= temp <= 25:
    print 'Normal'
elif 26 <= temp <= 35:
    print 'Quente'
else:
    print 'Muito quente!'

if temp < 0: print 'Congelando...'


#-------------------------------------------------------------------------------
# -- Funções --
#-------------------------------------------------------------------------------

def fatorial(num):
    ''' retorna a fatorial de num '''
    return 1 if num <= 1 else (num * fatorial(num - 1))

def fib(n):
    """ retorna o n-ésimo termo da sequencia de fibonacci """
    return 1 if n <= 1 else fib(n - 1) + fib(n - 2)

for i in [0,1, 2, 3, 4, 5]:
    print i, '(fib)=>', fib(i)
print
for i in [1, 2, 3, 4, 5]:
    print i, '(fat)=>', fatorial(i)

print

#-------------------------------------------------------------------------------
# -- Funções com argumento padrão --
#-------------------------------------------------------------------------------
print

def rgb_html(r=0, g=0, b=0):
    """Converte R, G, B em #RRGGBB"""
    return '#%02x%02x%02x' % (r, g, b)

def html_rgb(color='#000000'):
    """Converte #RRGGBB em R, G, B"""
    if color.startswith('#'): color = color[1:]
    r = int(color[:2], 16)
    g = int(color[2:4], 16)
    b = int(color[4:], 16)
    return r, g, b # Uma seqüência

print rgb_html(200, 200, 255)
print rgb_html(b=200, g=200, r=255) # O que houve?
print html_rgb('#c8c8ff')

#-------------------------------------------------------------------------------
# -- Funções com argumentos variaveis --
#-------------------------------------------------------------------------------

def func(*args, **kargs):
    print args
    print kargs

#No exemplo, kargs receberá os argumentos nomeados e args receberá os outros.
func(1,2,3,5,1,4,a=4,b=5,c=7)

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

def soma_e_multiplica (x, y):
    ''' soma_e_multiplica (x,y) -> (inteiro,inteiro)
        
        recebe dois inteiros, e retorna a soma e depois a multiplicação deles. '''
    return x + y , x * y
    
print soma_e_multiplica (2,3)

#-------------------------------------------------------------------------------
# -- Programação funcional --
#-------------------------------------------------------------------------------


inc = lambda x: x + 1
print inc(10)
ampl = lambda x, y, z: (x ** 2 + y ** 2 + z ** 2) ** 0.5
print ampl(1, 4, 7)
print ampl(5, 2, 4)

# -- Mapeamento
#Usando um laço for
lista = [1, 2, 3, 4, 5]
lista_2 = []
for i in lista:
    lista_2.append(i ** 2)
print lista_2
# Imprime [1, 4, 9, 16, 25]

#Usando a função map
quad = lambda x: x ** 2
lista = [1, 2, 3, 4, 5]
lista_2 = map(quad, lista)
print lista_2
# Imprime [1, 4, 9, 16, 25]


map(None, [1, 3, 5])   #[1, 3, 5]
map(abs, [-1, -2, -3]) #[1, 2, 3]
map(str, [2, 4, 6])    #['2', '4', '6']
map(hex, (10, 11, 12)) #['0xa', '0xb', '0xc']
map(lambda x, y: x*y, [1, 3, 5], [2, 4, 6]) #[2, 12, 30]
map(lambda a, b, x: a*x+b, [1, 3, 5], [2, 4, 8], [0, 0, 0])#[2, 4, 8]



fx = lambda f: f()
f1 = lambda: 'f1() executada'
f2 = lambda: 'f2() executada'
f3 = lambda: 'f3() executada'
f4 = lambda: 'f4() executada'
fn = [f1, f2, f3, f4]
print map(fx, fn)

nova_lista= map(lambda x :x*2, range(1,11))
print nova_lista

# -- Filtragem
lista = [1, 2, 3, 4, 5, 6]
print lista 

e_par = lambda x: (x % 2) == 0
lista_pares = filter(e_par, lista)
print lista_pares

e_par = lambda x: (x % 2) != 0
lista_impar = filter(e_par, lista)
print lista_impar

# -- Filtragem
def psoma(x, y):
    print '%d + %d = %d' % (x, y, x + y)
    return x + y

lista = [1, 2, 3, 4, 5]
print reduce(psoma, lista)

# -- zip 
print zip(range(10),("Gato","Cachorro","Papagaio"))

#Transposta de uma matriz
matriz = [[1,2,3],[4,5,6],[7,8,9]]
print zip(*matriz)

#Imperativo
tupla = (1, 2, 3, 4, 5)
soma = 0
for num in tupla:
    soma += num
print soma
# Funcional
tupla = (1, 2, 3, 4, 5)
print reduce(lambda x, y: x + y, tupla)

# fatorial Functional
n = int(raw_input("- Entre com um valor para a fatorial: "))
print reduce(lambda x,y: x*y, range(1,n+1))

#Primos
print filter(None,map(lambda y:y*reduce(lambda x,y:x*y!=0,map(lambda x,y=y:y%x, range(2,int(pow(y,0.5)+1))),1),range(2,50)))

#Fibonnaci
print map(lambda x,f=lambda x,f:(x<=1) or (f(x-1,f)+f(x-2,f)):int(f(x,f)),range(10))

#Palindromos
print filter(lambda x:x[::-1]==x,["casa","ovo","palavra","radar"])

#3025 = (30+25) = 55² = 3025
print filter(lambda x: sum(divmod(x,100))**2==x,range(1000,10000))

#há algum multiplo de 3 ou 5
any(map(lambda x: x%3==0 or x%5==0, (7,11,3,4,2)))

#List Comprehension
print [i for i in range(20) if i%2==0]

lista_strings = [' Linha 1 \n', ' Linha 2 \n', ' Linha 3 ']
# Com list comprehensions
stripped_list = [linha.strip() for linha in lista_strings]
print stripped_list
# Imprime ['Linha 1', 'Linha 2', 'Linha 3']
for linha in stripped_list:
    print linha


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# Eleve os ímpares ao quadrado
print [ x**2 for x in nums if x % 2 ]



p = lambda x: x%2==0
print map( p , range(2,6))

print map(lambda x,y: x+y,[1,2,3,4,5],[6,7,8,9,10])

p2 = lambda x,y: x%y==0
print map( p2 , range(1,15), range(2,16))

#-------------------------------------------------------------------------------
print "-"*60+"\nDesenvolva uma função que faz a soma de uma P.A. de razão 1 até o elemento passado como parâmetro.\n"+"-"*60
#-------------------------------------------------------------------------------
print reduce( lambda x,y: x+y, range(12) )
#-------------------------------------------------------------------------------
print "-"*60+"\nLimpe a string (retire '#' e '\n'): \n\
>>> nome = '\n\n ## E#\n##s#t#\n\n#\na f#r\n\na###s\ne ti##nh##a# #s##u\n#j\ne##\n\n#i\nr##a#.\n## \n\n\n\n'\n"+"-"*60
#-------------------------------------------------------------------------------
nome = '\n\n ## E#\n##s#t#\n\n#\na f#r\n\na###s\ne ti##nh##a# #s##u\n#j\ne##\n\n#i\nr##a#.\n## \n\n\n\n'
print filter( lambda x: x not in ('#','\n'), nome )
print [ s for s in nome if s not in ('#','\n')]
#-------------------------------------------------------------------------------


def knights():
    title = 'Sir'
    action = (lambda x: title + ' ' +x)
    return action

act = knights()
print act('robin')

key = 'got'
print { 'already' : (lambda : 2+2),
  'got' : (lambda : 2*4),
  'one' : (lambda : 2**6)
}[key]()

t, f = 1, 0
x, y = 88, 99
a = (t and x) or y #se for verdadeiro, x
print a
a = (f and x) or y #se for falso, y
print a
# deve ter certeza que x não será falso! senão retornará sempre y
# Erro:
print (t and f) or y # 99 (y)
# Corrigindo:
print ((t and [f]) or [y])[0] # 0 (f)

ifelse = lambda x,y,z: ((x and [y]) or [z])[0]
print ifelse(1,'spam','ni') # spam
print ifelse(0,'spam','ni') # ni

lower = lambda x,y: ( ((x<y) and [x]) or [y] )[0]
print lower('aa','bb')
print lower('bb','aa')
print lower(6,5)


def isPrimo(x):
    return not any([i for i in range(2,x-1) if x%i==0])

print isPrimo(11)
print isPrimo(6)
print isPrimo(7)

isPrimo2 = lambda x: not any([i for i in range(2,x-1) if x%i==0]) 

for x in range(0,20):
    print str(x)+(" é primo" if isPrimo2(x) else " não é primo")

print [x for x in range(0,20) if isPrimo2(x)]


print [x for x in range(0,20) if (lambda x: not any([i for i in range(2,x-1) if x%i==0]))(x) ]

# -- aceitando um valor n
n = int(raw_input("- Entre com o limite da sequencia de primos: "))
primos=  [x for x in range(n) if (lambda x: not any([i for i in range(2,x-1) if x%i==0]))(x) ]
print primos

# !!! O generator foi introduzido a partir do Python 2.4. Então a notação S usando geradores para iterar listas infinitas pode ser:

from itertools import count
S = (x for x in count() if x**2 > 3)

def action(x):
    return (lambda y: x+y)

act = action(99)
print act(2)

action2 = ( lambda x : (lambda y: x + y) )
print action2(99)(4)

#funcao interna apply

f = lambda x, y, z: x + y + z
print apply(f, (2,3,4) )
#poder:
#if <?>:
#    action, args = func1, (1,)
#else:
#    action, args = func2, (1,2,3)
#....
#apply(action,args)
# em geral é util quando não se pode prever a lista de argumentos antecipadamente.

import operator
print reduce(operator.add,[2,4,6])



#---------------------------------------------------------------------------
res=[]
for x in 'spam':
    res.append(ord(x))
print res

res= map(ord,'spam')
print res

res = [ord(x) for x in 'spam']
print res


res = [x+y for x in [0,1,2] for y in [100,200,300]]
print res

print [x+y for x in 'spam' for y in 'SPAM']
print [(x,y) for x in range(5) if x%2 == 0 for y in range(5) if y%2==1]


arq = ['aaa\n','bbb\n','ccc\n']
print [line[:-1] for line in arq]
print map( (lambda line: line[:-1]) , arq )


listOfTuple=[('bob',35,'mgr'),('mel',40,'dev')]
print [ al for al in listOfTuple]
print map((lambda (name,age,job):age ),listOfTuple)


lista_nome_classes = ["tela_principal","mapa_de_dispositivos","classe_negocio_pesado","acumulador","fim_da_lista_de_classes_do_exercicio"]
resposta = ["".join([z.title() for z in y]) for y in [x.split("_") for x in lista_nome_classes]]
print resposta

#QuickSort - iterativo 
def partition(list, l, e, g):
    if list == []:
        return (l, e, g)
    else:
        head = list[0]
        if head < e[0]:
            return partition(list[1:], l + [head], e, g)
        elif head > e[0]:
            return partition(list[1:], l, e, g + [head])
        else:
            return partition(list[1:], l, e + [head], g)
#QuickSort - funcional
def qsort(L):
    if len(L) <= 1: return L
    return qsort( [ lt for lt in L[1:] if lt < L[0] ] )  +  [ L[0] ]  +  qsort( [ ge for ge in L[1:] if ge >= L[0] ] )


print qsort('asdfggfgretytpoivcbnbkcxqwpko')

noprimes = [j for i in range(2, 8) for j in range(i*2, 50, i)]
print noprimes
primes = [x for x in range(2, 50) if x not in noprimes]
print primes

primes = [x for x in range(2, 50) if x not in [j for i in range(2, 8) for j in range(i*2, 50, i)] ]
print primes

words = 'The quick brown fox jumps over the lazy dog'.split()
stuff = [[w.upper(), w.lower(), len(w)] for w in words]
for i in stuff:
    print i



#---------Introspecção e outros truques com dados------------------


#dir
#A função dir nos permite inspecionar as propriedades e métodos de um objeto. Por exemplo:

x="Teste"
print dir(x)

#Isto lista os nomes de todos os métodos e propriedades das strings.


# para saber se o nome se refere a auma função
f='oi'
print callable(f)

print "OI, eu sou uma função" if callable(f) else "Não sou uma função."

f = lambda x:x+3
print "OI, eu sou uma função" if callable(f) else "Não sou uma função."

# classes são callable
class x: pass
print "OI, eu sou uma classe" if callable(x) else "Não sou uma classe."

#teste se o objeto é de um determinado tipo
print isinstance("teste",str)
print isinstance("teste",int)

def info(objeto):
    methodlist = [method for method in dir(objeto) if callable(getattr(objeto,method))]
    print "-- Métodos do ",type(objeto)," : --"
    for m in methodlist:
        print "-"*30
        print " - ",m," -- : ",str(getattr(objeto,m).__doc__).replace("\n",""),"\n"

info("")


from random import randint

def odd(n):
    return n%2

allNums=[]
for eachNum in range(9):
    allNums.append(randint(1,99))
print filter(odd,allNums)

print filter(lambda n : n%2, allNums)

print [n for n in allNums if n%2]

from random import randint as ri
print [ n for n in [ri(1,99) for i in range(9)] if n%2 ]



print map( lambda x: x+2, [0,1,2,3,4,5])
print map( lambda x: x**2, range(6) )
print [x+2 for x in range(6)]
print [x**2 for x in range(6)]
print map(lambda x,y: x+y, [1,2,3], [4,5,6])
print map(lambda x,y: (x+y,x-y), [1,2,3], [4,5,6])
print reduce(lambda x,y: x+y, range(5))

app=4
def func():
    print "...app()"
    app=5
    print "app=%d"%(app)
def func2():
    global app
    app=6

print "app %d"%app
func()
print "app still %d"%app
func2()
print "new app from func2() %d"%app


def foo():
    m=3
    def bar():
        n=4
        print m+n
    print m
    bar()

foo()

x=10
def foo3():
    y=5
    bar=lambda: x+y
    print bar()
    y=9
    print bar()
foo3()



#-------------------------------------------------------------------------------
# -- Arquivos --
#-------------------------------------------------------------------------------

import sys

# Criando um objeto do tipo file
temp = file('temp.txt', 'w')
# Escrevendo no arquivo
for i in range(100):
    temp.write('%03d\n' % i)
# Fechando
temp.close()
temp = file('temp.txt')
# Escrevendo no terminal
for x in temp:
    sys.stdout.write(x)
#Escrever em sys.stdout envia
# otexto para a saída padrão
temp.close()
#-------------------------------------------------------------------------------

import os.path
# raw_input retorna a string digitada
fn = raw_input('Nome do arquivo: ').strip()
if not os.path.exists(fn):
    print 'Tente outra vez...'
    sys.exit()
# Numerando as linhas
for i, s in enumerate(file(fn)):
    print i + 1, s,

#-------------------------------------------------------------------------------

import os.path as path

fn = raw_input('Nome do arquivo: ').strip()
if not path.exists(fn):
    print 'Tente outra vez...'
    sys.exit()

print "Caminho: %s/%s"%(path.dirname(fn),path.basename(fn))
print "Nome: %s"%(path.basename(fn))
print "Tamanho: %d bytes"%path.getsize(fn)
#-------------------------------------------------------------------------------

import glob as go 

# Mostra uma lista de nomes de arquivos
# e seus respectivos tamanhos
for arq in sorted(go.glob('*.py')):
    print arq, path.getsize(arq)

#-------------------------------------------------------------------------------
import csv

# Dados
dt = (('temperatura', 15.0, 'C', '10:40', '2006-12-31'),
('peso', 42.5, 'kg', '10:45', '2006-12-31'))
# A escrita recebe um objeto do tipo "file"
out = csv.writer(file('dt.csv', 'w'))
# Escrevendo as tuplas no arquivo
out.writerows(dt)

# A leitura recebe um objeto arquivo
dt = csv.reader(file('dt.csv'))
# Para cada registro do arquivo, imprima
for reg in dt:
    print reg

#-------------------------------------------------------------------------------
"""
Gravando texto em um arquivo compactado
"""
import zipfile
texto = """
***************************************
Esse é o texto que será compactado e...
... guardado dentro de um arquivo zip.
***************************************
"""
# Cria um zip novo
zip = zipfile.ZipFile('arq.zip', 'w',zipfile.ZIP_DEFLATED)
# Escreve uma string no zip como se fosse um arquivo
zip.writestr('texto.txt', texto)
# Fecha o zip
zip.close()


"""
Lendo um arquivo compactado
"""
import zipfile
# Abre o arquivo zip para leitura
zip = zipfile.ZipFile('arq.zip')
# Pega a lista dos arquivos compactados
arqs = zip.namelist()
for arq in arqs:
    # Mostra o nome do arquivo
    print 'Arquivo:', arq
    # Informações do arquivo
    zipinfo = zip.getinfo(arq)
    print 'Tamanho original:', zipinfo.file_size
    print 'Tamanho comprimido:', zipinfo.compress_size
    # Mostra o conteúdo do arquivo
    print zip.read(arq)

#-------------------------------------------------------------------------------
arq = file('arquivo_2.txt','w')
arq.write('123456789abcd\ntrygh')
arq.close()
arq = file('arquivo_2.txt')
arq.seek(8)
print arq.read()
# Imprime 6
arq.close()
#-------------------------------------------------------------------------------
arquivo = file('arquivo.txt', 'w')
print """\
Nome do arquivo: %s
Modo de abertura: %s
Está fechado?: %s""" % (arquivo.name, arquivo.mode, arquivo.closed)

#-------------------------------------------------------------------------------

arq = open('arquivo.txt', 'w')
arq.write('Linha 1\n')
# Abra o arquivo com seu editor preferido e veja que ele existe mas ainda está vazio.
arq.flush() 
# Feche o arquivo e o abra novamente – a string foi gravada em disco!
arq.write('Linha 2\n')
arq.close()



#-------------------------------------------------------------------------------
# -- Erros --
#-------------------------------------------------------------------------------
try:
    print 1/0
except ZeroDivisionError:
    print 'Erro ao tentar dividir por zero.'
#-------------------------------------------------------------------------------

try:
    x = int(raw_input("Digite um número: "))
    y = int(raw_input("Digite outro: "))
    resultado = x / y
    print "Resultado da divisão:", resultado
except ValueError:
    print "O valor digitado não é um número válido"
except ZeroDivisionError:
    print "O valor digitado para y deve ser maior do que 0 (zero)"
#-------------------------------------------------------------------------------
try:
    nome_arq = raw_input("Caminho do arquivo: ")
    arquivo = open(nome_arq)
    print arquivo.read()
    arquivo.close()
except IOError:
    print "Erro no arquivo '%s'", nome_arq
except:
    print "Um erro inesperado ocorreu!"
#-------------------------------------------------------------------------------
try:
    nome = raw_input("Nome: ")
    if len(nome) == 0:
        raise ValueError("Digite seu nome!")
    idade = int(raw_input("Idade: "))
    if idade < 18:
        raise ValueError("Você precisa ser maior de idade!")
except ValueError, mensagem:
    print mensagem
except:
    print "Um erro inesperado ocorreu!"
#-------------------------------------------------------------------------------
try:
    raise IndexError, 'Erro!!'
except IndexError:
    print '....:'
    raise
try:
    raise IndexError('Erro!!2')
except IndexError,men:
    print '....:2',men
try:
    raise IndexError, 'Erro!!'
except IndexError,e:
    print '....:',e
try:
    lis=[1]
    cod = int(raw_input("- entre com um numero: "))
    print lis[cod]
except (ValueError, IndexError):
    print "Erro!"
#-------------------------------------------------------------------------------
import traceback
# Tente receber o nome do arquivo
try:
    fn = raw_input('Nome do arquivo: ').strip()
    # Numerando as linhas
    for i, s in enumerate(file(fn)):
        print i + 1, s,
    # Se ocorrer um erro
except:
    # Mostre na tela
    trace = traceback.format_exc()
    #E salve num arquivo
    print 'Aconteceu um erro:\n', trace
    file('trace.log', 'a').write(trace)
    # Encerre o programa
    raise SystemExit
#-------------------------------------------------------------------------------
try:
    nome = raw_input("Nome Arquivo.:")
    with open(nome,'r') as f:
        for eachline in f:
            print eachline
except IOError:
    print "- Erro, arquivo não existe"
#-------------------------------------------------------------------------------
try:
   assert 1==0, 'one does not equals zero sily!'
except AssertionError, args:
   print "Assertion: %s"%args
#-------------------------------------------------------------------------------
try:
    import isDrufis as ids
except ImportError:
    print "- Falha ao importar o módulo isDrufis, verifique se o mesmo estpa instalado e tente mais tarde."
#-------------------------------------------------------------------------------
try:
    import os.path as os
except ImportError:
    print "- Falha ao importar o módulo isDrufis, verifique se o mesmo estpa instalado e tente mais tarde."
else:
    print dir()
#-------------------------------------------------------------------------------
'''The primary use of with statement is an exception-safe cleanup of an object used in the statement. with makes sure that files are closed, locks are released, contexts are restored, etc.

Does cvs.reader have things to cleanup in case of exception?

I'd go with:

with open("myfile.csv") as f:
    for row in csv.reader(f):
        # process row

You don't need to submit the patch to use cvs.reader and with statement together.

import contextlib

Help on function contextmanager in module contextlib:

contextmanager(func)
    @contextmanager decorator.

Typical usage:

    @contextmanager
    def some_generator(<arguments>):
        <setup>
        try:
            yield <value>
        finally:
            <cleanup>

This makes this:

    with some_generator(<arguments>) as <variable>:
        <body>

equivalent to this:

    <setup>
    try:
        <variable> = <value>
        <body>
    finally:
        <cleanup
'''

#-------------------------------------------------------------------------------
# -- Time --
#-------------------------------------------------------------------------------
import time
print time.localtime()
tim = time.localtime()
#(tm_year=2012, tm_mon=9, tm_mday=13, tm_hour=11, tm_min=32, tm_sec=8, tm_wday=3, tm_yday=257, tm_isdst=0)
print tim[0] #"tm_year"
# localtime() Retorna a data e hora local no formato
# de uma tupla:
# (ano, mês, dia, hora, minuto, segundo, dia da semana,
# dia do ano, horário de verão)
print time.localtime()
# asctime() retorna a data e hora como string, conforme
# a configuração do sistema operacional
print time.asctime()
# time() retorna o tempo do sistema em segundos
ts1 = time.time()
# gmtime() converte segundos para tuplas no mesmo
# formato de localtime()
tt1 = time.gmtime(ts1)
print ts1, '=>', tt1
# Somando uma hora
tt2 = time.gmtime(ts1 + 3600.)
# mktime() converte tuplas para segundos
ts2 = time.mktime(tt2)
print ts2, '=>', tt2
# clock() retorma o tempo desde quando o programa
# iniciou, em segundos
print 'O programa levou', time.clock(), \
'segundos sendo executado até agora...'
# Contando os segundos...
for i in xrange(5):
    # sleep() espera durante o número de segundos especificados
    time.sleep(1)
    print i + 1, 'segundo(s)'



import datetime
# datetime() recebe como parâmetros:
# ano, mês, dia, hora, minuto, segundo
# e retorna um objeto do tipo datetime
dt = datetime.datetime(2020, 12, 31, 23, 59, 59)
# Objetos date e time podem ser criados
# a partir de um objeto datetime
data = dt.date()
hora = dt.time()
# Quanto tempo falta para 31/12/2020
dd = dt - dt.today()
print 'Data:', data
print 'Hora:', hora
print 'Quanto tempo falta para 31/12/2020:', \
str(dd).replace('days', 'dias')


#-------------------------------------------------------------------------------
# -- Classes --
#-------------------------------------------------------------------------------
#estudando classes
class Shape:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    description = "This shape has not been described yet"
    author = "Nobody has claimed to make this shape yet"
    def area(self):
        return self.x * self.y
    def perimeter(self):
        return 2 * self.x + 2 * self.y
    def describe(self,text):
        self.description = text
    def authorName(self,text):
        self.author = text
    def scaleSize(self,scale):
        self.x = self.x * scale
        self.y = self.y * scale

rectangle = Shape(100,45)
print rectangle.area()
print rectangle.perimeter()
rectangle.scaleSize(0.5)
print rectangle.area()
print rectangle.perimeter()

class Classe(supcl1, supcl2):
	""" Isto é uma classe """
	clsvar = []
	def __init__(self, args):
		""" Inicializador da classe """
		<bloco de código>
	def __done__(self):
		""" Destrutor da classe """
		<bloco de código>
	def metodo(self, params):
		""" Método de objeto """
		<bloco de código>
	@classmethod
	def cls_metodo(cls, params):
		""" Método de classe """
		<bloco de código>
	@staticmethod
	def est_metodo(params):
		""" Método estático """
		<bloco de código>


class Cell(object):
	""" Classe para células de planilha """
	def __init__(self, formula='""', format='%s'):
		""" Inicializa a célula """
		self.formula = formula
		self.format = format
	def __repr__(self):
		""" Retorna a representação em string da célula """
		return self.format % eval(self.formula)

print Cell('123**2')
print Cell('23*2+2')
print Cell('abs(-1.45 / 0.3)', '%2.3f')
#--------Classes Abertas, podem ser modificadas em tempo de execução---------------------------------------------------------
class User(object):
	"""Uma classe bem simples. """
	def __init__(self, name):
		"""Inicializa a classe, atribuindo um nome """
		self.name = name

# Um novo método para a classe
def set_password(self, password):
	"""Troca a senha """
	self.password = password
	print 'Classe original:', dir(User)

# O novo método é inserido na classe
User.set_password = set_password
print 'Classe modificada:', dir(User)
user = User('guest')
user.set_password('guest')
print 'Objeto:', dir(user)
print 'Senha:', user.password


#--------Métodos estáticos e de classe --------------------------------------

class Exemplo(object):
    @classmethod
    def da_classe(cls,arg):
        return (cls,arg)
    @staticmethod
    def estatico(arg):
        return

print Exemplo.da_classe('fu')
print Exemplo.estatico('bar')
#--------Classes abertas--------------------------------------
class Animal(object):
    pass
''' as classes são abertas e permite que um módulo redefina uma classe e adicione atributos a uma classe definida em outro módulo.
    Em python é chamado de 'monkey patching', usa uma sintaxer de reflexão explicita e não é considerada uma boa protica (mas acontece) '''

baleia = Animal()
baleia.nome= "Moby Dick"
baleia.peso=1200
print '{0.nome} ({0.peso:.1f})'.format(baleia)
#--------Herança simples--------------------------------------

class Pendrive(object):
	def __init__(self, tamanho, interface='2.0'):
		self.tamanho = tamanho
		self.interface = interface

class MP3Player(Pendrive):
	def __init__(self, tamanho, interface='2.0', turner=False):
		self.turner = turner
		Pendrive.__init__(self, tamanho, interface)

mp3 = MP3Player(1024)
print '%s\n%s\n%s' % (mp3.tamanho, mp3.interface, mp3.turner)
#--------Herança Multipla--------------------------------------

class Terrestre(object):
	""" Classe de veículos terrestres """
	se_move_em_terra = True

	def __init__(self, velocidade=100):
		""" Inicializa o objeto """
		self.velocidade_em_terra = velocidade

class Aquatico(object):
	"""Classe de veículos aquaticos"""
	se_move_na_agua = True
	def __init__(self, velocidade=5):
		"""Inicializa o objeto"""
		self.velocidade_agua = velocidade

class Carro(Terrestre):
	"""Classe de carros"""
	rodas = 4
	def __init__(self, velocidade=120, pistoes=4):
		"""Inicializa o objeto"""
		self.pistoes = pistoes
		Terrestre.__init__(self, velocidade=velocidade)

class Barco(Aquatico):
	"""Classe de barcos"""
	def __init__(self, velocidade=6, helices=1):
		"""Inicializa o objeto"""
		self.helices = helices
		Aquatico.__init__(self, velocidade=velocidade)

class Anfibio(Carro, Barco):
	"""Classe de anfíbios"""
	def __init__(self, velocidade_em_terra=80, velocidade_na_agua=4, pistoes=6, helices=2):
		""" Inicializa o objeto """
		# É preciso evocar o __init__ de cada classe pai
		Carro.__init__(self, velocidade=velocidade_em_terra,
		pistoes=pistoes)
		Barco.__init__(self, velocidade=velocidade_na_agua,
		helices=helices)

novo_anfibio = Anfibio()
for atr in dir(novo_anfibio):
	# Se não for método especial:
	if not atr.startswith('__'):
	    print atr, '=', getattr(novo_anfibio, atr)
#-----------Propriedades----similiar ao C#-----------------------

class Projetil(object):
	def __init__(self, alcance, tempo):
		self.alcance = alcance
		self.tempo = tempo
	# Calcula a velocidade
	def getv(self):
	    return self.alcance / self.tempo
	# Calcula o tempo
	def setv(self, v):
	    self.tempo = self.alcance / v
	# Define a propriedade
	velocidade = property(getv, setv)

moab = Projetil(alcance=10000, tempo=60)
print moab.velocidade
# Muda a velocidade
moab.velocidade = 350
print moab.tempo
#----------- Sobrecarga de operadores ----------------------
class String(str):
	def __sub__(self, s):
	    return self.replace(s, '')

s1 = String('The Lamb Lies Down On Broadway')
s2 = 'Down '
print '"%s" - "%s" = "%s"' % (s1, s2, s1 - s2)
#----------- Attributos de classes ----------------------
class myclass(str):
    pass

print myclass.__name__
print myclass.__doc__
print myclass.__bases__
print myclass.__module__
print myclass.__class__
#----------- Destrutor ----------------------
class C():
    def __init__(self):
        print 'initialized'
    def __del__(self):
        print 'deleted'

c1=C()
c2=c1
c3=c1
print (id(c1),id(c2),id(c3))
del c1
del c2
del c3

class Aluno:
    def __init__(self,ra,name,curso):
        self.name=name
        print '%s foi criado na memoria'%self.name
        self.ra=ra
        self.curso=curso
    def __del__(self):
        print '%s foi deletado da memoria'%self.name

al1=Aluno(12,'Flavio','Java')
print al1
#----------- Classes como registros ----------------------

class rec:pass
#define os atributos da classe
#rec.name ='mel'
#rec.age = 40
#rec.job ='trainer/writer'

#print rec.age


#define os atributos do objeto (cada instancia)
p1=rec()
p1.name ='mel'
p1.age = 40
p1.job ='trainer/writer'


p2=rec()
p2.name ='oto'
p2.age = 67

print p1.name," ",p1.age," ",p1.job
#print p2.name," ",p2.age," ",p2.job #vai da erro
print p2.name," ",p2.age


class Person:
    def __init__(self,name,job):
        self.name=name
        self.job=job
    def info(self):
        return (self.name, self.job)

mark = Person ('ml','trainer')
dave = Person ('da','developer')

print mark.job
print dave.info()

import aluno as a

als=[]
al1=a.Aluno(12,'Flavio','Java')
al1.Ra=5
als.append(al1)
al2=a.Aluno(12,'Oto','Java')
als.append(al2)
al3=a.Aluno(34,'Martins','Java')
als.append(al3)
al4=a.Aluno(17,'Lucas','Java')
als.append(al4)
al5=a.Aluno(87,'Gal','Java')
als.append(al5)

print dir(al1)
for al in als:
    print al.Ra," ",al.Name," ",al.Curso

print a.Aluno.version
print al1.version
al1.version +=0.2 #altera somente a instancia
#a.Aluno.version +=0.2 #altera total (instancia e objeto)
print a.Aluno.version
print al1.version
print al2.version
print a.Aluno.Name #<property object at 0xb783dacc>



#----------- Delegação ----------------------
class wrapper:
    def __init__(self,object):
        self.wrapped = object
    def __getattr__(self,attrname):
        print 'Trace',attrname
        return getattr(self.wrapped,attrname)

x = wrapper([1,2,3])
x.append(4)
print x.wrapped
x = wrapper({"a":1,"b":2})
print x.keys()
print x.wrapped

#----------- outros... ----------------------

class Carta (object):
    def __init__(self,valor,naipe):
        self.valor = valor
        self.naipe = naipe
    def __repr__(self):
        return '<%s de %s>'%(self.valor,self.naipe)

class Baralho(object):
    naipes = 'paus copas espadas ouros'.split()
    valores = 'A 2 3 4 5 6 7 8 9 10 J Q K'.split()
    def __init__(self):
        self.cartas = [Carta(v,n) for n in self.naipes
                                  for v in self.valores]
    def __len__(self):
        return len(self.cartas)
    def __getitem__(self,pos):
        return self.cartas[pos]
    #para funcionar o shuffle
    def __setitem__(self,pos,valor):
        self.cartas[pos]=valor
    def __getitem__(self,pos):
        return self.cartas[pos]

b= Baralho()
len(b)
print b[0], b[1], b[2]
for carta in reversed(b):
    print carta

from random import choice
for i in range(5): print choice(b)
from random import shuffle
l= range(10)
shuffle(l)
shuffle(b)
print b[::5]


#-------------------------------------------------------------------------------
# -- Módulos -- 
#-------------------------------------------------------------------------------
import numeros
print numeros.soma(2, 3)
print dir(numeros)
from numeros import soma, produto
print soma(2, 4)
print produto(3, 9)
print numeros.__name__

#-------------------------------------------------------------------------------
# -- eval -- 
#-------------------------------------------------------------------------------


import os

#eval - evaluated expression
eval_code = compile('100 + 200',' ','eval')
print eval(eval_code)
#single - single executable
single_code = compile('print "hello world!"','','single')
exec single_code
#exec - group of executable 
exec_code = compile("""
req = int(raw_input("- entre com um número: "))
for an in range(req):
    print an
""",'','exec')
exec exec_code

os.system("chmod +x Teste.py")
os.system("./Teste.py")
os.execv("Teste.py",("teste",""))

#-------------------------------------------------------------------------------
# -- tópicos para quem sabe python -- 
#-------------------------------------------------------------------------------


class Carta(object):
    def __init__(self,valor,naipe):
        self.valor=valor
        self.naipe=naipe
    def __repr__(self):
        return '<%s de %s>'%(self.valor,self.naipe)

zape=Carta('4','paus')
print zape

class Baralho(object):
	naipes = 'copas ouros espadas paus'.split()
	valores = 'A 2 3 4 5 6 7 8 9 10 J Q K'.split()
	def __init__(self):
		self.cartas = [Carta(v, n) for n in self.naipes for v in self.valores]
	def __getitem__(self, pos):
		return self.cartas[pos]
	def __len__(self):
		return len(self.cartas)


b = Baralho()
print b[0]
print b[:3]
print b[-3:]
# b é iterável, ou seja, algo que possa ser percorrido por uma iteração. Em python
for carta in b:
    print carta

#-------------------------------------------------------------------------------

from random import randint
def dado():
    return randint(1,6)
## gera valores ate que um 6 seja sorteado
for r in iter(dado,6):
    print r

#-------------------------------------------------------------------------------

# -- função geradora --
def gera_letra(ultima='C', verboso=True):
	cod = ord('A')
	while chr(cod) <= ultima:
		letra = chr(cod)
		if verboso:
		    print 'gerando %r...'% letra
		yield letra
		cod += 1
# -- list comp vs função geradora --
for ii in [letra for letra in gera_letra()]:
    print ii
for ii in (letra for letra in gera_letra()):
    print ii


#-------------------------------------------------------------------------------
class Quantidade(object):
	def __init__(self, nome_atr):
		self.nome_atr = nome_atr
	def __get__(self, instance, owner):
		return getattr(instance, '_qtd_'+self.nome_atr)
	def __set__(self, instance, value):
		value = int(value)
		if value >= 0:
			setattr(instance, '_qtd_'+self.nome_atr, value)
		else:
			raise TypeError('quantidade < 0')

class C(object):
	def __init__(self, x):
		self.x = x
	x = Quantidade('x')

o = C(7)
print o.x
o = C(-7)

class C(object):
	def __init__(self):
		self._x = None
	@property
	def x(self):
		"""O 'x' deste objeto"""
		return self._x
	@x.setter
	def x(self, value):
		self._x = value
	@x.deleter
	def x(self):
		del self._x



#-------------------------------------------------------------------------------


#-------------------------------------------------------------------------------






#----------- Metaclasses ----------------------


from warnings import warn
class R(type):
    def __init__(cls, name, bases, attrd):
        super(R,cls).__init__(name,bases,attrd)
        if '__str__' not in attrd:
            raise TypeError("Você deve criar str na classe")

class F(object):
    __metaclass__= R
    def __init__(self):
        print "instanciando foo"
    #def __str__(self): print "Classe Foo rs"
        

f = F()
print isinstance(f,F)
print isinstance(f,R)

#---------------------------------------------------------------------------------------------

class Bar(object): pass
class Foo: pass
print dir(Foo)
print dir(Bar)

class Bola(object):
    def __init__(self,cor,circunferencia,material):
        self.cor=cor
        self.circunferencia=circunferencia
        self.material=material
    def trocarCor(self,novaCor):
        self.cor=navaCor
    def mostraCor(self):
        return self.cor
    def get(self,obj,typ=None):
        print "capturando attr...",obj
        return getattr(self,obj)
    def set(self,obj,val):
        print "setando attr...",obj
        setattr(self,obj,val)

b= Bola("amarela",12,"madeira")
b.cor="azul"
print b.cor
print b.get("cor")
b.set("cor","branca")
print b.cor


class Clock:  
        def __init__(self):  
            self.hour = 0  
            self.minute = 0  
            self.second = 0  
      
        def __getattr__(self, name):  
            print "--- Accessing %s in __getattr__()..." % name  
            if name == "hour":  
                return self._hour  
            elif name == "minute":  
                return self._minute  
            elif name == "second":  
                return self._second  
            else:  
                raise AttributeError, name  
      
        def __setattr__(self, name, value):  
            print "+++ Accessing %s in __setattr__()..." % name
            if name == "hour":  
                if 0 <= value <= 23:  
                    self.__dict__["_hour"] = value  
                else:  
                    raise ValueError,"Invalid %s value: %s"%(name,value)
            elif name == "minute":  
                if 0 <= value <= 59:  
                    self.__dict__["_minute"] = value  
                else:  
                    raise ValueError, "Invalid %s value: %s" % (name, value)  
            elif name == "second":  
                if 0 <= value <= 59:  
                    self.__dict__["_second"] = value  
                else:  
                    raise ValueError, "Invalid %s value: %s" % (name, value)  
            else:  
                raise AttributeError, name  
      
# Main  
      
clock = Clock()  
      
print "=== State of clock object is: %d:%d:%d." % (clock.hour, clock.minute,clock.second)  
      
clock.hour = 17  
clock.minute = 25  
clock.second = 23  
      
print "=== State of clock object is: %d:%d:%d." % (clock.hour, clock.minute,clock.second)  
      
# Access object's attributes without using __getattr__().  
print ">>> State of clock object is: %d:%d:%d." % (clock._hour, clock._minute,clock._second) 



# o codigo abaixo somente
# sera executado se este
# arquivo for executado
# diretamente.
# nao o será se a classe
# TiaVelha for importada
# para dentro de outro
# programa python
if __name__=='__main__':
    b= Bola("amarela",12,"madeira")
    b.cor="azul"
    print b.cor
    print b.get("cor")
    b.set("cor","branca")
    print b.cor


#---------------------------------------------------------------------------------------------

import pdb

def pyramid1(n):
    for i in range(1, n+1): 
        print((str(i)+" ")*i)

pdb.run("pyramid1(4)")
print pdb.runeval("2+3")

pdb.set_trace()
print "oioioi" 
#---------------------------------------------------------------------------------------------
import traceback
import sys

def produce_exception(recursion_level=2):
    sys.stdout.flush()
    if recursion_level:
        produce_exception(recursion_level-1)
    else:
        raise RuntimeError()

def call_function(f, recursion_level=2):
    if recursion_level:
        return call_function(f, recursion_level-1)
    else:
        return f()

print 'print_exc() with no exception:'
traceback.print_exc(file=sys.stdout)
print

try:
    produce_exception()
except Exception, err:
    print 'print_exc():'
    traceback.print_exc(file=sys.stdout)
    print
    print 'print_exc(1):'
    traceback.print_exc(limit=1, file=sys.stdout)


import traceback
import sys
from pprint import pprint


try:
    produce_exception()
except Exception, err:
    print 'format_exception():'
    exc_type, exc_value, exc_tb = sys.exc_info()
    pprint(traceback.format_exception(exc_type, exc_value, exc_tb))


import traceback
import sys

def produce_exception(recursion_level=2):
    sys.stdout.flush()
    if recursion_level:
        produce_exception(recursion_level-1)
    else:
        raise RuntimeError()

def call_function(f, recursion_level=2):
    if recursion_level:
        return call_function(f, recursion_level-1)
    else:
        return f()


# - funções de stack:

print "\n\n ---- print_stack()\n"

import traceback
import sys

def f():
    traceback.print_stack(file=sys.stdout)

print 'Calling f() directly:'
f()
print
print 'Calling f() from 3 levels deep:'
call_function(f)

print "\n ---- format_stack()\n"
import traceback
import sys
from pprint import pprint

def f():
    return traceback.format_stack()

formatted_stack = call_function(f)
pprint(formatted_stack)

print "\n ---- extract_stack()\n"
import traceback
import sys
from pprint import pprint

def f():
    return traceback.extract_stack()

stack = call_function(f)
pprint(stack)


