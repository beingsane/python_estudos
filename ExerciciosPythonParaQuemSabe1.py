#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#-------------------------------------------------------------------------------
# -- 1. Baralho polimórfico
#-------------------------------------------------------------------------------
'''Para os exercícios desta seção, use como base o código do exemplo baralho.py.

1.1. Implemente uma subclasse de Baralho chamada BaralhoInverso com um método __iter__ que produz um iterador para fornecer as cartas na ordem inversa, ou seja, sem embaralhar, a primeira carta deve ser o <K de paus> em vez do <A de copas>, como acontece na implementação atual.

Bônus: implemente três métodos, iter_genexp, iter_genfun e iter_obj, usando (respectivamente) uma expressão geradora, uma função geradora e um objeto iterador.'''
import time

class Carta(object):
    def __init__(self,valor,naipe):
        self.valor=valor
        self.naipe=naipe
    def __repr__(self):
        return '<%s de %s>'%(self.valor,self.naipe)

class Baralho(object):
	naipes = 'copas ouros espadas paus'.split()
	valores = 'A 2 3 4 5 6 7 8 9 10 J Q K'.split()
	def __init__(self):
		self.cartas = [Carta(v, n) for n in self.naipes for v in self.valores]
	def __getitem__(self, pos):
		return self.cartas[pos]
	def __len__(self):
		return len(self.cartas)

class BaralhoInverso(Baralho):
    def __init__(self):
        Baralho.__init__(self)
    def __iter__(self):
        for carta in reversed(self.cartas):
            yield carta
    def iter_genlisComp(self):
        return [cartas for cartas in reversed(self.cartas)]
    def iter_genexp(self):
        return (cartas for cartas in reversed(self.cartas))

#-------------------------------------------------------------------------------
b= Baralho()
br = BaralhoInverso()

#lazy...
timebegin= time.time()
for car in br: 
    print car
print
itertime = time.time() - timebegin
print
timebegin= time.time()
#all first...
for car in br.iter_genlisComp(): 
    print car
print
listcomptime =  time.time() - timebegin 
print
timebegin= time.time()
#lazy...
for car in br.iter_genexp(): 
    print car
print
gentime = time.time() - timebegin
print
print "- iter: %f\n- List: %f\n- GemE: %f"%(itertime,listcomptime,gentime)

'''1.2. Implemente uma subclasse de Baralho chamada BaralhoMisturado com um método __iter__ que produz um iterador para fornecer as cartas em uma ordem aleatória. Note que este iterador deverá produzir exatamente 52 cartas, e nenhuma deverá ser repetida. Seguindo a filosofia do padrão de projeto Iterator, o iterador não deve alterar o estado interno do baralho, de modo que possam existir vários iteradores ao mesmo tempo, cada um percorrendo as cartas embaralhadas em uma ordem diferente.

Dicas: (1) não embaralhe a estrutura interna que contém as cartas, mas gere uma série embaralhada de índices, e use esta série para determinar a próxima carta; (2) use a função shuffle do módulo random para embaralhar os índices.
'''

class BaralhoMisturado(Baralho):
    def __init__(self):
        Baralho.__init__(self)
    def __iter__(self):
        import random
        indices = range(len(self.cartas))
        random.shuffle(indices)
        for index in indices: yield self.cartas[index] 

bm = BaralhoMisturado()
for cartas in bm: print cartas


#-------------------------------------------------------------------------------
# -- 2. List comprehensions (listcomps) -- 
#-------------------------------------------------------------------------------
'''Para estes exercícios, usaremos as listas abaixo:'''

mulheres = ['Mariana', 'Ana', 'Paula']
homens = ['Pedro', 'Juca', 'Tom', 'Joaquim'] 

'''2.1. Use uma listcomp para gerar uma lista de homens com nomes de 4 ou menos letras.'''

print [h for h in homens if len(h)<=4]

'''2.2. Use uma listcomp para gerar uma lista de duplas (também conhecida em computação como uma lista associativa) formada pela letra inicial e o nome de cada homem. Por exemplo, a resposta para a lista mulheres seria:
[('M', 'Mariana'), ('A', 'Ana'), ('P', 'Paula')]'''

print [ (m[0],m) for m in mulheres]
print [ (h[0],h) for h in homens]

'''2.3. Use o resultado do exercício 2.2 para gerar um dicionário associando iniciais aos nomes de homens. Quantos itens terá o dicionário assim produzido?'''
print
dicM=dict([(m[:2],m) for m in mulheres])
print dicM

print
dicH=dict([ (h[:2],h) for h in homens])
print dicH

'''2.4. Use a função zip para gerar uma lista associativa, e com ela carregar um dicionário associando cada mulher a um homem. Quantos itens terá o dicionário assim produzido?'''

dicCasais= dict([ (m,h) for [m,h] in zip(mulheres,homens)])
print "Formados %d casais."%len(dicCasais)
print dicCasais

'''2.5. Bônus: Gere uma lista associativa para organizar uma aula de dança na qual todos devem dançar com todos. Quantos casais serão formados?
   Dica: o nome da operação a ser feita neste exercício é produto cartesiano, e para fazer isso em uma listcomp ou genexp você precisa usar mais de um for dentro da expressão.'''

casais = [ (m,h) for m in mulheres for h in homens] 
print "Formados %d casais."%len(casais)
for m,h in casais:
    print "%s -s2- %s"%(m,h)

'''2.6. Bônus: Repita o exercício 2.5, acrescentando um filtro com if para remover os nomes com menos de 4 letras das duas listas. Quantos casais serão formados? '''

casais = [ (m,h) for m in mulheres if len(m)<4 for h in homens if len(h)<4] 
print "Formados %d casais."%len(casais)
for m,h in casais:
    print "%s -s2- %s"%(m,h)

#-------------------------------------------------------------------------------
# -- 3. Biblioteca padrão -- 
#-------------------------------------------------------------------------------
'''
3.1. "The quick brown fox jumps over the lazy dog" é um pangrama, uma frase que usa todas as letras do alfabeto inglês.
O que faz o código abaixo? Qual a resposta que aparece no lugar de «1»?

>>> fox = 'The quick brown fox jumps over the lazy dog.'
>>> fox_letters = set(l.upper() for l in fox if l.isalpha())
>>> len(fox_letters)
«1»
'''
# a função 'quebra' a string em letras e passa cada uma em maiusculo.
# como se trata de um conjunto não occore a repetição das mesmas
# com o uso do filtro if l.isalpha()- provavelmente ela deve ignorar os carateres ' ' e '.'
fox = 'The quick brown fox jumps over the lazy dog.'
fox_letters = set(l.upper() for l in fox if l.isalpha())
len(fox_letters) # retorna a quantidade de caracteres no conjunto das letras, ou seja, a quantidade de caracteres diferentes utilizados para compor a frase e que pertencem ao alfabeto
''' 3.2. Que resposta apareceria no lugar de «1» se não fosse usado o filtro if na expressão geradora acima? '''
#sem o filtro apareceria a mesma quantidade porem acrescida de 2, para ' ' e '.'
'''3.3. Para verificar se o conjunto fox_letters realmente contém todas as letras do alfabeto, podemos verificar se este conjunto é igual ao conjunto das letras ASCII maíusculas que o Python conhece. Para fazer esta verificação, o que devemos escrever no lugar de «1», e que resposta aparecerá em «2»?
>>> import string
>>> letters = set(string.ascii_uppercase)
>>> «1» == letters
«2»
'''
import string
letters = set(string.ascii_uppercase)
fox_letters == letters # retornará True
''' 3.4. O alfabeto português antigamente era menor que o inglês, mas hoje é igual (tirando o cedilha). A frase abaixo aparece como exemplo de pangrama na Wikipédia em português, vamos verificar usando a mesma técnica usada acima, substituindo «1», «2» e «3» pelas expressões apropriadas:
>>> jabuti = 'Um pequeno jabuti xereta viu dez cegonhas felizes.'
>>> jabuti_letras = set(«1» for l in «2» if «3»)
 '''
jabuti = 'Um pequeno jabuti xereta viu dez cegonhas felizes.'
jabuti_letras = set(l.upper() for l in jabuti if l.upper() in letters)
'''Uma vez que temos o conjunto das letras da frase do jabuti, podemos verificar a diferença entre o conjunto de todas as letras e este conjunto. Qual operador usamos em «1» e qual a resposta aparecerá em «2»:
>>> letters «1» jabuti_letras
set(«2»)'''
letters - jabuti_letras
print set(letters - jabuti_letras)
# set(['Y', 'K', 'W'])
''' Bônus: Existem dois operadores de conjunto que podem ser usados no lugar de «1», e neste exemplo ambos produziriam o mesmo resultado em «2». Quais são os operadores, e qual a diferença entre eles? '''
print set(letters.difference(jabuti_letras)) # diferença de letters com jabuti_letras
print set(letters).symmetric_difference(set(jabuti_letras)) # diferença simetrica, tantu letters com jabuti_letras como o contrario

#-------------------------------------------------------------------------------
# -- 4. Funções redutoras -- 
#-------------------------------------------------------------------------------
'''Para os exemplos abaixo, usaremos as listas m e n:'''
m = [5, 3, 7, 2, 0, -1]
n = [10, 20, 30]
'''4.1. Complete as lacunas «?» nestas aplicações simples de funções redutoras:'''
print all(m)
#«1» False - existe um número falso (==0) em m
print all(n)
#«2» True - não existem números Falsos (==0) em n
print any(m)
#«3» True - existe pelo menso um True em m
print any(n)
#«4» True - existe pelo menso um True em n
print sum(n)
#60 =  10+20+30
print sum(n+m)
#76 = 10+20+30 + (5+3+7+2+0+-1)
'''4.4. Calcule o resultado «1»:
>>> sum(a*b for (a,b) in enumerate(n))
«1»'''
# enumerate(n) - retorna enumações, ou uma lista de tuplas (indice,valor) : (0, 10) (1, 20) (2, 30)
# [a*b for (a,b) in enumerate(n)] : multiplica os indices com os seus valores e cria uma lista dos resultados
# a função abaixo retorna  a soma dessa multiplicação = 80
print sum(a*b for (a,b) in enumerate(n))
'''4.3. Explique o resultado abaixo:
>>> all(x for (x,y) in zip(m, n))
True'''
zip(m, n) # retorna uma lista de tuples, criada segundo (ai,bi), sendo aeM e beN, com o mesmo indice, e para no momento que uma das listas não tiver mais elementos no caso:
# [(5, 10), (3, 20), (7, 30)] , os elementos de m : 2, 0, -1, ficam de fora pois não existem mais elementos de n para realizar a correspondencia.
(x for (x,y) in zip(m, n)) # captura apenas os elementos ai da tupla, ou seja, 5,3,7
# com a função all, verifdica se existe algum elemento falso. No caso, não pois nenhum é igual a zero.
'''4.4. Calcule o resultado «1»:
>>> sum(x*y for (x,y) in zip(m, n))
«1»'''
# multiplica as tuplas [(5, 10), (3, 20), (7, 30)] gerando uma lista (50,60,210) e depois soma os elemtos : 50+60=110 , 110+210 = 320




