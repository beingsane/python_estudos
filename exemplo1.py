#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import pdb

# Criando uma funcao para teste
def mudatudo(nome,sobrenome):
    novonome = nome.replace("Fabio","Dorneles")
    novosobrenome = sobrenome.replace("Rizzo","Tremea")
    return novonome + novosobrenome

# Definindo o rastreamento
pdb.set_trace()

# Definindo as variaveis
nome       = "Fabio"
sobrenome  = "Rizzo"
site       = "http://www.fabiorizzo.com"

# concatenando as variaveis
junto   = "Meu nome eh %s %s, e meu site eh o: %s"%(nome,sobrenome,site)

# Imprimindo a variavel
print junto

junto = mudatudo(nome,sobrenome)

# Imprimindo a variavel
print junto



