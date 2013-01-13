#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
#-------------------------------------------------------------------------------
# -- Lista Strings --
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
print "-"*60+"\n6) Data por extenso. Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o nome do mês por extenso.\
Data de Nascimento: 29/10/1973\
Você nasceu em  29 de Outubro de 1973.\n"+"-"*60
#-------------------------------------------------------------------------------
mes={1:"Janeiro",2:"Fevereiro",3:"Março",4:"Abril",5:"Maio",6:"Junho",7:"Julho",8:"Agosto",9:"Setembro",10:"Outubro",11:"Novembro",12:"Dezembro"}

while True:
    data= raw_input(" - Entre com uma data(dd/mm/aaaa): ")
    comp=data.split("/")
    if len(comp)!=3 or len(comp[0])>2 or len(comp[1])>2 \
       or len(comp[0])==0 or len(comp[1])==0 or len(comp[2])!=4 \
       or int(comp[0])>31 or int(comp[1])>12:
        print " -Você entrou com uma data inválida"
        continue

    print "- A data é: ",comp[0]," de ",mes[int(comp[1])]," de ",comp[2]
    break
#-------------------------------------------------------------------------------
print "-"*60+"\n7) Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:\
a. quantos espaços em branco existem na frase.\
b. quantas vezes aparecem as vogais a, e, i, o, u.\n"+"-"*60
#-------------------------------------------------------------------------------
qntB, qntV, vogais = 0, 0, 'aeiou'
str1 = raw_input(" - Entre com uma frase: ")

for s in str1:
    if s==" ": qntB+=1
    if s in vogais: qntV+=1

print "- Na frase: ",str1
print "- Existem ",qntV," vogais"
print "- Existem ",qntB," espaços em branco"
#-------------------------------------------------------------------------------
print "-"*60+"\n8) Palíndromo. Um palíndromo é uma seqüência de caracteres cuja leitura é idêntica se feita da direita para esquerda ou vice−versa. Por exemplo: OSSO e OVO são palíndromos. Em textos mais complexos os espaços e pontuação são ignorados. A frase SUBI NO ONIBUS é o exemplo de uma frase palíndroma onde os espaços foram ignorados. Faça um programa que leia uma seqüência de caracteres, mostre−a e diga se é um palíndromo ou não. \n"+"-"*60
#-------------------------------------------------------------------------------
def isPalindromic(stri):
    ''' Verifica se a string é um palindromo '''
    stri = stri.lower();
    stri = stri.replace(" ","");
    o = range(0,len(stri)/2,1)
    p = range(-1,-len(stri)/2,-1)
    for i,y in zip(o,p):
        if stri[i]!=stri[y]:
            return False
    return True

string = raw_input("- Entre com uma palavra possivelmente palidroma: ")
if isPalindromic(string):
    print "- %s é um palindromo."%(string)
else:
    print "- %s não é um palidromo."%(string)
#-------------------------------------------------------------------------------
print "-"*60+"\n9)  Verificação de CPF. Desenvolva um programa que solicite a digitação de um número de CPF no formato xxx.xxx.xxx-xx e indique se é um número válido ou inválido através da validação dos dígitos verificadores e dos caracteres de formatação.  \n"+"-"*60
#-------------------------------------------------------------------------------
def validarCPF(cpf): 
    cpf = cpf.replace(".","").replace("-","")
    add=0;
    for i in range(0,9,1):
        add+=int(cpf[i])*(10-i)
    rev=11-(add%11)
    if rev==10 or rev==11: rev=0
    if rev!= int(cpf[9]): return False
    add=0;
    for i in range(0,10,1):
        add+=int(cpf[i])*(11-i) 
    rev=11-(add%11)
    if rev==10 or rev==11: rev=0
    if rev!= int(cpf[10]): return False
    return True

while True:
    cpf = raw_input("- Entre com um número de CPF no formato xxx.xxx.xxx-xx: ")
    if len(cpf)<14:
        print "- O CPF deve conter 14 caracteres..."
        continue
    if '.' not in cpf or '-' not in cpf:
        print "- Formato do CPF deve ser: xxx.xxx.xxx-xx..."
        continue
    if validarCPF(cpf):
        print "- CPF válido!"
    else:
        print "- CPF não válido!"
    break
#-------------------------------------------------------------------------------
print "-"*60+"\n10)  Número por extenso. Escreva um programa que solicite ao usuário a digitação de um número até 99 e imprima-o na tela por extenso.\n"+"-"*60
#-------------------------------------------------------------------------------
num_dic={'1':'um','2':'dois','3':'tres',\
             '4':'quatro','5':'cinco','6':'seis',\
             '7':'sete','8':'oito','9':'nove','0':'zero',\
             '10':'dez','12':'doze','13':'treze',\
             '14':'quarenta','15':'quinze','16':'dezesseis',\
             '17':'dezessete','18':'dezoito','19':'dezenove',\
             '20':'vinte','30':'trinta',\
             '40':'quarenta','50':'cinquenta','60':'sessenta',\
             '70':'setenta','80':'oitenta','90':'noventa',}

num = int(raw_input("- Entre com um número de 0 a 99"))
if num<0 or num>100:
    print "- Apenas números entre 0 e 99..."
else:
    if num<=20: 
        print num_dic[str(num)]
    for i in range(20,100,10):
        if num>i and num<=(i+10):
            if num == (i+10): 
                print num_dic[str(i+10)]
            else:
                print num_dic[str(i)]+' e '+num_dic[str(num-i)]
#-------------------------------------------------------------------------------
print "-"*60+"\n11) Jogo de Forca. Desenvolva um jogo da forca. O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente. O jogador poderá errar 6 vezes antes de ser enforcado.\
Digite uma letra: A\
-> Você errou pela 1ª vez. Tente de novo!\
Digite uma letra: O\
A palavra é: _ _ _ _ O\
Digite uma letra: E\
A palavra é: _ E _ _ O\
Digite uma letra: S\
-> Você errou pela 2ª vez. Tente de novo!\
Valida e corrige número de telefone. Faça um programa que leia um número de telefone, e corrija o número no caso deste conter somente 7 dígitos, acrescentando o '3' na frente. O usuário pode informar o número com ou sem o traço separador.\n"+"-"*60
#-------------------------------------------------------------------------------
import random
def sortWord():
    lista=['morango','amora','jabuticaba','damasco','malancia','banana','caqui','carambola','tomate','caju','açai','kiwi','laranja','melao','abacaxi','abacate','uva','melancia','maracuja','papagaio','jacare']
    random.shuffle(lista)
    return lista[len(lista)/2]

vet=[]
str1=sortWord()
acertos=0

def popDic(int1):
    for i in int1:
        vet.append(False)
    return vet

def mostraWord(vet,str1):
    str2="A palavra é:"
    for s in str1:
        str2+= s+" " if vet[str1.index(s)] else "_ "
    return str2

vet = popDic(str1)
tent=6
while True:
    print mostraWord(vet,str1)
    l = raw_input("- Digite uma letra: ")
    if l in str1:
        vet[str1.index(l)]=True
        acertos+=1
        if acertos==len(str1)-1: break
    else:
        tent-=1
        if tent==0: break
        print " - Você errou, mais %d tentativas."%(tent)

if tent==0 or acertos<len(str1)-1:
    print "- Você perdeu."
else:
    print "- Você ganhou."
    print "A palavra é:",str1
#-------------------------------------------------------------------------------
print "-"*60+"\n12)  Valida e corrige número de telefone. Faça um programa que leia um número de telefone, e corrija o número no caso deste conter somente 7 dígitos, acrescentando o '3' na frente. O usuário pode informar o número com ou sem o traço separador.\
    Valida e corrige número de telefone\
    Telefone: 461-0133\
    Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.\
    Telefone corrigido sem formatação: 34610133\
    Telefone corrigido com formatação: 3461-0133\n"+"-"*60
#-------------------------------------------------------------------------------
tel = raw_input("- Entre com um número de telefone: ")
if len(tel)==8:
    print "- Esse telefone está correto."
elif  len(tel)>8:
    print "- Esse telefone tem mais que 8 digitos, irei truncá-los."
    tel=tel[:8]  
else:
    print "- Esse telefone tem %s digitos, irei adicionar digitos '3' a sua frente."%(len(tel))
    for i in range(len(tel),8,1):
        tel='3'+tel  

print "- Telefone sem Formatação %s"%(tel)
print "- Telefone sem Formatação %s"%(tel[:4]+"-"+tel[4:])
#-------------------------------------------------------------------------------
print "-"*60+"\n13)  Jogo da palavra embaralhada. Desenvolva um jogo em que o usuário tenha que adivinhar uma palavra que será mostrada com as letras embaralhadas. O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente. O jogador terá seis tentativas para adivinhar a palavra. Ao final a palavra deve ser mostrada na tela, informando se o usuário ganhou ou perdeu o jogo. \n"+"-"*60
#-------------------------------------------------------------------------------
import random
def sortWord():
    lista=['morango','amora','jabuticaba','damasco','malancia','banana','caqui','carambola','tomate','caju','açai','kiwi','laranja','melao','abacaxi','abacate','uva','melancia','maracuja','papagaio','jacare']
    random.shuffle(lista)
    return lista[len(lista)/2]

def sortLetters(string):
    lista=[]
    for s in string: lista.append(s)
    random.shuffle(lista)
    string=''
    for l in lista: string+=l
    return string

palavra=sortWord()
print sortLetters(palavra)
tent=6
while tent>0:
    pal=raw_input("- Que palavra é essa?")
    if pal==palavra:
        print "- Parabens, você acertou!"
        break
    else:
        tent-=1
        print "- Você errou! :( ... tem mais %d tentativas."%(tent)
#-------------------------------------------------------------------------------
print "-"*60+"\n14)  Leet spek generator. Leet é uma forma de se escrever o alfabeto latino usando outros símbolos em lugar das letras, como números por exemplo. A própria palavra leet admite muitas variações, como l33t ou 1337. O uso do leet reflete uma subcultura relacionada ao mundo dos jogos de computador e internet, sendo muito usada para confundir os iniciantes e afirmar-se como parte de um grupo. Pesquise sobre as principais formas de traduzir as letras. Depois, faça um programa que peça uma texto e transforme-o para a grafia leet speak.\n"+"-"*60
#-------------------------------------------------------------------------------

dic={'a':'@','e':'3','i':'|','o':'0','u':'v','b':'5','c':'(','v':'V','l':'£'}

palavra = raw_input("- Entre com uma palavra: ")
leetSpeak=''
for s in palavra:
    if s in dic.iterkeys():
        leetSpeak+=dic[s]
    else: leetSpeak+=s

print "- ",leetSpeak

