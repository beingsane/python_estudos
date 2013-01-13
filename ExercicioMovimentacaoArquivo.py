#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
#-------------------------------------------------------------------------------
# -- Exercicio de Movimentação em arquivos --
#-------------------------------------------------------------------------------

import os.path as path
import zipfile
import glob as go 

arq=None
filename=""

def carregar():
    ''' - Carrega arquivo no programa '''
    global arq
    global filename
    print "\n---- Carregando Arquivo Texto ----\n"
    while True:
        filename = raw_input("- Entre com o nome do arquivo texto:")
        if '.txt' not in filename: filename= filename+'.txt'
        if not path.exists(filename):
            print "- Arquivo não encontrado."
            continue
        arq = file(filename)
        print "- Carregado com sucesso."
        break 

def carregado():
    if arq==None or filename=="":
        print "! Nenhum arquivo carregado !"
        return False
    return True

def visualizando():
    #if carregado():return None
    print "-"*60
    i=0
    for line in arq.readlines():
        print "%d %s"%(i,line)
    print "-"*60

def captura(base=0,deslocamento=0):  
    if base not in [0,1,2]: base=0
    arq.seek(deslocamento,base)
    print "%d %s"%(arq.tell(),arq.read())

def capturar():  
    #if carregado():return None
    seek = int(raw_input("- Entre com a posição desejada no arquivo: "))
    base = int(raw_input("- Em relação ao inicio (0), final(2) ou posição atual (1)?"))
    captura(base,seek)

def menu():
    menu={1:carregar,2:visualizando,3:capturar}
    while True:
        print
        print "---- Menu: ----"
        print "1) Carregar arquivo texto"
        print "2) Ver arquivo texto"
        print "3) Capturar posição no arquivo"
        print "0) Sair"
        op = int(raw_input("- Entre com a opção:"))
        if op==0: break
        if op not in menu.iterkeys():
            print "- Opção inválida."
            continue
        print
        menu[op]()
    print "- Obrigado por utilizar o sistema."
    if arq!=None : 
        if not arq.closed: arq.close()

print " "
menu()


