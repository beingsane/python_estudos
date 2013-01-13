#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
#-------------------------------------------------------------------------------
# -- Sistema de Cadastro de Alunos --
#-------------------------------------------------------------------------------
import os.path as path
alunos={}
#-----------------------------
# -- Cadastra um novo aluno --
#-----------------------------
def novo():
    global alunos
    while True:
        print "\n---- Cadastrando um novo Aluno ----"
        # - Recebendo RA
        while True:
            try:
                ra=int(raw_input("- RA.: "))
                assert ra in alunos.iterkeys()
                break
            except ValueError:
                print "- RA deve ser um número."
            except AssertionError:
                op= raw_input("- Ra já existente. Deseja alterar o aluno? (s) ou (n):")
                if  op=='s': 
                    altera(alunos[ra])
                    return
        # - Recebendo Nome
        while True:
            nome=raw_input("- Nome.: ")
            if nome!="": break
            print "- Nome vazio."
        # - Recebendo Curso
        while True:
            curso=raw_input("- Curso.: ")
            if curso!="": break
            print "- Curso vazio."
        
        alunos[ra] = { "nome":nome,
                       "curso":curso} 
        op = raw_input("- Deseja cadastrar mais algum aluno? (s) ou (n): ")
        if op!='s' : break
#----------------------------------
# -- Altera os dados de um aluno --
#----------------------------------
def altera(aluno):
    print "\n---- Alterando os dados de %s ----"%aluno["nome"]
    while True:
        nome=raw_input("- Nome ou 0 para pular.: ")
        if nome=="0": break
        if nome!="":
            aluno["nome"]=nome
            break
        print "- Nome vazio..."
    while True:
        curso=raw_input("- Curso ou 0 para pular.: ")
        if curso=="0": break
        if curso!="":
            aluno["curso"]=curso
            break
        print "- Curso vazio..."
#----------------------------------------------
# -- Recebe o código do aluno a ser alterado --
#----------------------------------------------
def alterar():
    global alunos
    print "\n---- Alterando os dados do uma aluno ----"
    while True:
        try:
            ra=int(raw_input("- RA ou 0 para cancelar.: "))
            if ra==0: return
            assert ra in alunos.iterkeys()
            break
        except ValueError:
            print "- RA deve ser um número."
        except AssertionError:
            print "- Aluno inexistente..."
    altera(alunos[ra])
#-----------------------------------
# -- Mostra os alunos cadastrados --
#-----------------------------------
def mostrar():
    global alunos
    print "\n---- Relatório de alunos ----"
    print "Ra\tNome\tCurso"
    for ra in alunos.iterkeys():
        print "%4d\t%s\t%11s"%(ra,alunos[ra]["nome"],alunos[ra]["curso"])
    print "- No total: %d alunos"%(len(alunos))
#----------------------
#-- Excluir um aluno --
#----------------------
def excluir(): 
    global alunos
    print "\n---- Excluir aluno ----"
    while True:
        try:
            ra=int(raw_input("- RA ou 0 para cancelar.: "))
            if ra==0: return
            assert ra in alunos.iterkeys()
            break
        except ValueError:
            print "- RA deve ser um número."
        except AssertionError:
            print "- Aluno inexistente..."
    print "\n%d- %s, %s"%(ra,alunos[ra]["nome"],alunos[ra]["curso"])
    op = raw_input("- Deseja realmente excluir o aluno acima? (s) ou (n): ")
    if op=="s":
        alunos.pop(ra)
        print "Excluido com sucesso."
    print
#--------------------------------------
#-- Verifica a existencia do arquivo --
#--------------------------------------
def fileExiste(filename,op):
    ''' - Verifica se o arquivo existe, caso exista mostra uma opção de sobrescrever ou não o mesmo. Caso seja a opção de importar os dados (op!=0), o mesmo não faz a verificação de sobrescrita. '''
    if op!=0: return False
    if path.exists(filename):
        print "- Arquivo ja existe..."
        op = raw_input("- Deseja sobrescrever? (s) ou (n)")
        return not op=="s"
    return False
#-------------------------------
#-- Salva os dados no arquivo --
#-------------------------------
def gravarFile(filename):
    global alunos
    print "\n- Gravando...."
    try:
        with file(filename,'w') as arq:
            for ra in alunos.iterkeys():
                arq.write("%d,%s,%s;"%(ra,alunos[ra]["nome"],alunos[ra]["curso"]))
                arq.flush()
    except IOError:
        print "- Ocorreu um erro inesperado ao salvar os dados em um arquivo."
    else:
        print "- Foram salvos %d alunos com sucesso"%len(alunos)
#-------------------------------------------------------
#-- Captura o nome do arquivo e aplica a extenção txt --
#-------------------------------------------------------
def catchArquivo(op=0):
    while True:
        try:
            filename = raw_input("- Nome do arquivo: ")
            assert filename!=""
            if ".txt" not in filename: filename+=".txt"
            if  not fileExiste(filename,op) : break
        except AssertionError:
            print "- Nome em branco"
    return filename
#-------------------------------------------------------
#-- Grava o arquivo --
#-------------------------------------------------------
def gravar(): 
    print "\n---- Salvando alunos em arquivo ----"
    filename = catchArquivo()
    gravarFile(filename)
#-----------------------------------------------------
#-- Recebe uma lista de alunos e os adiciona a base --
#-----------------------------------------------------
def popular(alunosA):
    global alunos
    try:
        for line in alunosA:
            dt = line.split(",")
            if len(dt)>3 : continue
            alunos[int(dt[0])] = {"nome":dt[1],"curso":dt[2]} 
        print "- Foram importados %d alunos com sucesso"%len(alunosA)
    except (KeyError,IndexError):
        print "- Erro ao importar os arquivos. Formato de arquivo inválido."
#------------------------------------------
#-- Importa novos alunos a base de dados --
#------------------------------------------
def importar(filename):
    global alunos
    op = raw_input("- Deseja adicionar os arquivos a base existente ou sobrescrever a base? (a - adicionar) ou (s - sobreescrever): ")
    if op=='s': alunos.clear()
    print "---- Importando alunos ----"
    try:
        with file(filename) as arq:
            alunosA = arq.readlines()[0].split(";")
    except IOError:
        print "- Erro ao abrir arquivo."
    else:
        popular(alunosA)
#-----------------------------------------------
#-- Solicta o nome do arquivo a ser importado --
#-----------------------------------------------
def ler():
    print "\n---- Ler alunos de um arquivo ----"
    filename = catchArquivo(1)
    importar(filename)
#--------------------
#-- Menu principal --
#--------------------
def menu():
    menu={1:novo,2:alterar,3:excluir,4:ler,5:gravar,6:mostrar}
    try:
        while True:
            try:
                print "\n---- Menu: ----"
                print "1) Cadastrar novo aluno"
                print "2) Alterar aluno existente"
                print "3) Excluir aluno existente"
                print "4) Ler alunos de um arquivo"
                print "5) Salvar em um arquivo"
                print "6) Mostrar alunos cadastrados"
                print "0) Sair"
                op = int(raw_input("- Entre com a opção:"))
                if op==0: break
                menu[op]()
            except (KeyError,ValueError):
                print "- Opção inválida."
    except (KeyboardInterrupt,SystemExit):
        print "\n- Obrigado por utilizar o sistema."

print " "
menu()







