#!usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import csv
from calcoohija import CalculadoraHija #Clase que contiene operaciones básicas aritméticas

operaciones = CalculadoraHija() #functions: plus,minus,mult y div

if __name__ == "__main__":
	with open('operar.csv') as fich:
		operlist = csv.reader(fich)
		
		for currentline in operlist:
			currentoper = currentline[0]
			operandos = currentline[1:]
			result = int(operandos[0])
			indice = 1
			while indice < len(operandos): 
				oper2 = int(operandos[indice])
				if currentoper == 'suma':
					result = operaciones.plus(result,oper2)
				elif currentoper == 'resta':
					result = operaciones.minus(result,oper2)
				elif currentoper == 'multiplica':
					result = operaciones.mult(result,oper2)
				elif currentoper == 'divide':
					result = operaciones.div(result,oper2)
				else:
					sys.exit("Operaciones permitidas: suma, resta, division, multiplicacion")
				indice = indice + 1	
			print(result)
