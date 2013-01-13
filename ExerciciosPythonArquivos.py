#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
#-------------------------------------------------------------------------------
# -- Lista Arquivos --
#-------------------------------------------------------------------------------
print "-"*60+"\n1)Faça um programa que leia um arquivo texto contendo uma lista de endereços IP e gere um outro arquivo, contendo um relatório dos endereços IP válidos e inválidos.\nO arquivo de entrada possui o seguinte formato: \n\
200.135.80.9\n192.168.1.1\n8.35.67.74\n257.32.4.5\n85.345.1.2\n\
1.2.3.4\n9.8.234.5\n192.168.0.256\n\
O arquivo de saída possui o seguinte formato:\n\
[Endereços válidos:]\n200.135.80.9\n192.168.1.1\n8.35.67.74\n1.2.3.4\n[Endereços inválidos:]\n257.32.4.5\n85.345.1.2\n9.8.234.5\n192.168.0.256  \n"+"-"*60
#-------------------------------------------------------------------------------
validos=[]
invalidos=[]

def ler():
    #Leitura do arquivos
    arq = file("ips.txt",'r')
    ips= arq.readlines()
    arq.close()
    return ips

def gravar():
    #gravando os ips
    global validos
    global invalidos
    arq = file("ipsResultado.txt",'w')
    arq.write("[Endereços válidos:]\n")
    arq.write("".join(validos))
    arq.write("[Endereços inválidos:]\n")
    arq.write("".join(invalidos))
    arq.close()

def validar(ip):
    if '.' not in ip:
        print "Endereço IP inválido. (sem '.')"
        return False
    ipL=ip.split(".")
    if len(ipL)>4:
        print "Endereço IP inválido. (conjunto de números a mais)"
        return False
    if len( [p for p in ipL if int(p)>255] ):
        print "Endereço IP inválido. (bandas de 0 a 255 apenas)"
        return False
    return True

ips=ler()
for i in ips:
    if validar(i):
        validos.append(i)
    else:
        invalidos.append(i)
gravar()

#-------------------------------------------------------------------------------
print "-"*60+"\n2) A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no seu servidor de arquivos. Para tentar resolver este problema, o Administrador de Rede precisa saber qual o espaço ocupado pelos usuários, e identificar os usuários com maior espaço ocupado. Através de um programa, baixado da Internet, ele conseguiu gerar o seguinte arquivo, chamado 'usuarios.txt': \n\
alexandre       456123789\n\
anderson        1245698456\n\
antonio         123456456\n\
carlos          91257581\n\
cesar           987458\n\
rosemary        789456125\n\
Neste arquivo, o nome do usuário possui 15 caracteres. A partir deste arquivo, você deve criar um programa que gere um relatório, chamado 'relatório.txt', no seguinte formato: \n\
ACME Inc.               Uso do espaço em disco pelos usuários\n\
------------------------------------------------------------------------\n\
Nr.  Usuário        Espaço utilizado     % do uso\n\
1    alexandre       434,99 MB             16,85%\n\
2    anderson       1187,99 MB             46,02%\n\
3    antonio         117,73 MB              4,56%\n\
4    carlos           87,03 MB              3,37%\n\
5    cesar             0,94 MB              0,04%\n\
6    rosemary        752,88 MB             29,16%\n\
Espaço total ocupado: 2581,57 MB\n\
Espaço médio ocupado: 430,26 MB\n\
O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em memória, caso sejam necessários, de forma a agilizar a execução do programa. A conversão da espaço ocupado em disco, de bytes para megabytes deverá ser feita através de uma função separada, que será chamada pelo programa principal. O cálculo do percentual de uso também deverá ser feito através de uma função, que será chamada pelo programa principal.\n"+"-"*60
#-------------------------------------------------------------------------------
dic={}
#Conversão para MB
def toMB(bytes):
    return float(bytes/1024)
#Calculo Porcentagem
def perCent(bytes,total):
    return float(toMB(bytes)*100/toMB(total))
#Calculo media
def calAVG(bytes,totalF):
    return float(toMB(bytes)/totalF)
#Trazendo arquivo
filename= "usuarios.txt"
f = open(filename,'r')
allLines=f.readlines()
f.close()
#montando dicionario de dados
totalSpace, totalF = 0, 0
for eachLine in allLines:
    nome = eachLine[:16]
    use=int(eachLine[16:])
    dic[nome]=use
    totalSpace+=use
    totalF+=1
#geração do relatório
print "ACME Inc.               Uso do espaço em disco pelos usuários"
print "-----------------------------------------------------------------------"
print "Nr.  Usuário\t\tEspaço utilizado\t% do uso"
i=0
for k,v in dic.items():
    print i,"  ",k,"\t",toMB(v)," MB\t\t"+str(perCent(v,totalSpace))+"%"
print "Espaço total ocupado: ",toMB(totalSpace)," MB"
print "Espaço médio ocupado: ",calAVG(totalSpace,totalF)," MB"

