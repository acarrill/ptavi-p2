#!usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from calcoohija import CalculadoraHija #Clase que contiene operaciones básicas aritméticas

def separarlista(cadena):
	""""""
	newlist = cadena.split(',')
	lastelem = newlist[-1].split('\n')
	newlist[-1] = lastelem[0]
	newlist.append('\n')
	return newlist
	
operaciones = CalculadoraHija() #functions: plus,minus,mult y div

if __name__ == "__main__":
	fich = open('operar.txt','r') 
	operlist = fich.readlines() # guardamos las operaciones del fichero en una lista
	fich.close
	
	for operline in operlist:
		currentline = separarlista(operline) # separamos una linea en una nueva lista
		currentoper = currentline[0]
		currentline.pop(0) # Devuelve operación a realizar y la elimina
		indice = 1
		while currentline[indice] != '\n': #iteramos en los operandos hasta fin de linea
			preindice = indice -1
			if preindice == 0:
				oper1 = int(currentline[preindice])
			else:
				oper1 = result
			oper2 = int(currentline[indice])
			if currentoper == 'suma':
				result = operaciones.plus(oper1,oper2)
			elif currentoper == 'resta':
				result = operaciones.minus(oper1,oper2)
			elif currentoper == 'multiplica':
				result = operaciones.mult(oper1,oper2)
			elif currentoper == 'divide':
				result = operaciones.div(oper1,oper2)
			else:
				sys.exit("Operaciones permitidas: suma, resta, division, multiplicacion")
			indice = indice + 1	
			
		print(result)
