# -*- coding: iso-8859-1 -*-

u"""Faz a manipulacao de dois numeros, através das funções
soma, diferenca, produto, quociente e potencia"""
def soma(x, y):
	"""Esta função retorna a soma dos dois números passados como parâmetros"""
	return x + y
def diferenca(x, y):
	u"""Esta função retorna a diferença dos dois números passados como parâmetros"""
	return x - y
def produto(x, y):
	u"""Esta função retorna o produto dos dois números passados"""
	return x * y
def quociente(x, y):
	u"""Retorna o quociente dos dois números."""
	return x / y
def potencia(x, y):
	u"""Retorna a potencia dos dois números"""
	potencia = 1
	while y > 0:
		potencia = potencia * x
		y = y - 1
	return potencia

