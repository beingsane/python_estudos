#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
#-------------------------------------------------------------------------------
# -- Sistema cadastro pizza em CSV --
#-------------------------------------------------------------------------------
import sys
try:
    import os
    import csv
except ImportError:
    print "- Erro ao importar Módulos: os e csv não encontrados!"
    sys.exit()

pizzas={}
#----------------------------------
# -- Gera Tuplas para gravar CSV --
#----------------------------------
def geraTupla():
    lista=[]
    for cod in pizzas.iterkeys():
        pizza = pizzas[cod]
        lista.append( (pizza["cod"],pizza["nome"],pizza["ingredientes"],pizza["preco"]) )
    return tuple(lista)
#-------------------------------
# -- Abre CSV e importa dados --
#-------------------------------
def openCSV():
    try:
        with open('pizzas.csv') as fi:
            out = csv.reader(fi,delimiter=';')
            for [cod,nome,ingredientes,preco] in out:
                pizzas[int(cod)] = {"cod":int(cod),
                                    "nome":nome, 
                                    "ingredientes":ingredientes, 
                                    "preco":float(preco.replace(",","."))} 
    except IOError:
        print "- Erro ao abrir banco de dados, arquivo pizzas.csv necessário ao programa."
        sys.exit()       
#-----------------
# -- Gravar CSV --
#-----------------
def gravarCSV():
    try:
        with open('pizzas.csv','w+') as fi:
            out = csv.writer(fi, delimiter=';')
            out.writerows(geraTupla())
    except IOError:
        print "- Erro ao salvar dados no banco, arquivo pizzas.csv necessário ao programa."
#-----------------------------
# -- Cadastro de nova pizza --
#-----------------------------
def novo():
    global pizzas
    while True:
        print "---- Cadastrando uma nova Pizza ----"
        # - Recebendo código
        while True:
            try:
                cod=int(raw_input("- Código.: "))
                assert cod not in pizzas.iterkeys()
                break
            except ValueError: print "- Favor entre com um código numérico."
            except AssertionError: print "- Código já existente..."
        # - Recebendo nome
        while True:
            nome=raw_input("- Nome.: ")
            if nome!="": break
            print "- Nome vazio..." 
        # - Recebendo ingredientes
        while True:
            ingredientes=raw_input("- Ingredientes.: ")
            if ingredientes!="": break
            print "- Ingrediente vazio..." 
        # - Recebendo preco
        while True:
            try:
                preco=float(raw_input("- Preço.: ").replace(",","."))
                break
            except ValueError:
                print "- O preço deve ser um número."
        # - Adicioanndo pizza ao 'banco'
        pizzas[cod] = {"cod":cod,
                       "nome":nome, 
                       "ingredientes":ingredientes, 
                       "preco":preco} 
        
        op = raw_input("- Deseja cadastrar mais alguma pizza? (s) ou (n): ")
        if op!='s' : break
#---------------------------------
# -- Alterar dados de uma pizza --
#---------------------------------
def altera(cod):
    global pizzas
    try:
        pizza = pizzas[cod]
    except (KeyError,IndexError): 
        return "- Erro inesperado."
    print "---- Alterando os dados da pizza %s ----"%pizza["nome"]
    # - Recebendo nome
    while True:
        nome=raw_input("-Nome ou 0 para pular.: ")
        if nome=="0": break
        if nome!="": 
            pizza["nome"]=nome
            break
        print "- Nome vazio..." 
    # - Recebendo ingredientes
    while True:
        ingredientes=raw_input("- Ingrediente ou 0 para pular.: ")
        if ingredientes=="0": break
        if ingredientes!="":  
            pizza["ingredientes"]=ingredientes
            break
        print "- Ingredientes vazios..." 
    # - Recebendo preco
    while True:
        try:
            preco=float(raw_input("- Preco ou 0 para pular: ").replace(",","."))
            if preco==0: break
            else: 
                pizza["preco"]=preco
                break
        except ValueError:
            print "- O Preço deve ser um número."
#-----------------------------------------------
# -- Receber o código da pizza a ser alterada --
#-----------------------------------------------
def alterar():
    global alunos    
    while True:
        print "---- Alterando os dados da pizza ----"
        while True:
            try:
                cod=int(raw_input("- Código ou 0 para cancelar: "))
                if cod==0: return None
                assert cod in pizzas.iterkeys()
                break
            except ValueError:
                print "- O código deve ser um número"
            except AssertionError:
                print "- Pizza inexistente..."
        altera(cod)
        print
#-------------------------------
# -- Mostra pizzas no 'Banco' --
#-------------------------------
def mostrar():
    global pizzas
    try:
        print "---- Relatório de Pizzas ----"
        print "Cod\tNome\tPreço(R$)\tIngredientes"
        for cod in pizzas.iterkeys():
            pizza = pizzas[cod]
            print "%d\t%s\t%.2f\t%s"%(cod,pizza["nome"],pizza["preco"],pizza["ingredientes"])
        print "- No total: %d pizzas"%(len(pizzas))
    except (IndexError,KeyError):
        print "- Ocorreu um erro inesperado."
#-----------------------
# -- Exclui uma pizza --
#-----------------------
def excluir(): 
    global pizzas
    print "---- Excluir pizza ----"
    while True:
        try:
            cod=int(raw_input("- Código ou 0 para cancelar: "))
            if cod==0: return None
            assert cod not in pizzas.iterkeys()
            break
        except ValueError:
            print "- O código deve ser um número."
        except AssertionError:
            print "- Pizza inexistente.."
    print "%d- %s, %s"%(cod,pizzas[cod]["nome"],pizzas[cod]["preco"])
    op = raw_input("- Deseja realmente excluir a pizza acima? (s) ou (n): ")
    if op=="s":
        pizzas.pop(cod)
        print "Excluida com sucesso."
    print
#-----------------------
# -- Menu Principal --
#-----------------------
def menu():
    menu={1:novo,2:alterar,3:excluir,4:mostrar}
    try:
        openCSV()
        while True:
            try:
                print "\n---- Menu: ----"
                print "1) Cadastrar nova pizza"
                print "2) Alterar pizza existente"
                print "3) Excluir pizza existente"
                print "4) Mostrar pizzas cadastrados"
                print "0) Sair"
                op = int(raw_input("- Opção.: "))
                if op==0: break
                menu[op]()
                gravarCSV()
            except (ValueError,AssertionError,KeyError):
                print "- Opção inválida."
    except (KeyboardInterrupt,SystemExit):pass
    finally:
        print "\n- Obrigado por utilizar o sistema."

print " "
menu()

