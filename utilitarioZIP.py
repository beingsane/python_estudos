#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
#-------------------------------------------------------------------------------
# -- Sistema de Utilitário para arquivos zip --
#-------------------------------------------------------------------------------

import os.path as path
import zipfile
import glob as go 

arq=None
filename=""

def carregar():
    ''' - carrega arquivo no programa '''
    global arq
    global filename
    print "\n---- Carregando Arquivos ----\n"
    while True:
        filename = raw_input("- Entre com o nome do arquivo e sua extensão:")
        if not path.exists(filename):
            print "- Arquivo não encontrado."
            continue
        arq = file(filename)
        print "- Carregado com sucesso."
        break 

def visualizar(): 
    ''' - Mostra informações como nome, caminho, tamanho e conteudo '''
    if arq==None or filename=="":
        print "! Nenhum arquivo carregado !"
        return None
    print "\n---- Relatório do Arquivo ----\n"
    print "- Caminho.: %s/%s"%(path.dirname(filename),path.basename(filename))
    print "- Nome.: %s"%(path.basename(filename))
    print "- Tamanho.: %d bytes"%path.getsize(filename)
    print "- Conteudo.: \n%s\n"%getConteudo(arq)

def getConteudo(ar):
    return "".join(ar.readlines())

def compact(name):
   ''' - Compacta o arquivo em .zip '''
   # Cria um zip novo
   zip = zipfile.ZipFile(name+".zip", 'w',zipfile.ZIP_DEFLATED)
   zip.writestr(filename,getConteudo(arq))
   # Fecha o zip
   zip.close()
   print "- Arquivo compactado  com sucesso, veja '%s' em seu diretório"%(name+".zip")

def compactar():
    ''' - Recebe o nome do arquivo .zip que irá conter o arquivo carregado '''
    print "\n---- Compactando Arquivo ----\n"
    while True:
        name = raw_input("- Entre com o nome do futuro arquivo .zip :")
        if name!="": break
    compact(name)

def visualizarC(): 
    ''' - Mostra informações sobre o arquivo compactado '''
    while True:
        name = raw_input("- Entre com o nome do arquivo .zip :")
        if '.zip' not in name : name = name+'.zip'
        if not path.exists(name):
            print "- Arquivo não encontrado."
            continue
        if name=="":
            print "- Nome vazio..."
            continue
        break
    print "\n---- Relatório do(s) Arquivo(s) ----\n"
    zip = zipfile.ZipFile(name)
    arqs = zip.namelist()
    for ar in arqs:
        print 'Arquivo:', ar
        zipinfo = zip.getinfo(ar)
        print '- Tamanho original:', zipinfo.file_size
        print '- Tamanho comprimido:', zipinfo.compress_size
        print '- Conteudo:\n', getConteudo(file(ar))


def pesquisar(): 
    ''' - Pesquisa arquivos no diretoriao local e mostra as informações: nome e tamanho dos mesmo segundo regra solicitada ao usuario '''
    while True:
        print "\n---- Pesquisando Arquivos ----\n"
        name = raw_input("- Entre com o nome ou extensão ou regra de busca: (ex: *.py, *.txt, al*):")
        for ar in sorted(go.glob(name)):
            print "- %s , tam.: %d bytes"%(ar, path.getsize(ar))
        op = raw_input("-  Deseja realizar outra busca? (s) ou (n): ")
        if op!='s': break


def menu():
    menu={1:carregar,2:compactar,3:visualizar,4:visualizarC,5:pesquisar}
    while True:
        print
        print "---- Menu: ----"
        print "1) Carregar arquivos"
        print "2) Compactar arquivos"
        print "3) Visualizar informações do arquivo carregado"
        print "4) Visualizar informações do arquivo compactado"
        print "5) Pesquisar arquivos em seu diretorio"
        print "6) Sair"
        op = int(raw_input("- Entre com a opção:"))
        if op==6: break
        if op not in menu.iterkeys():
            print "- Opção inválida."
            continue
        print
        menu[op]()
    print "- Obrigado por utilizar o sistema."
    if arq!=None : 
        if not arq.closed: arq.close()
    
print "-- Iniciando... --"
menu()




