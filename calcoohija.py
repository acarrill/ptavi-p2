#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys 
from calcoo import Calculadora #Importamos suma y resta

class CalculadoraHija(Calculadora):
	def div(self, op1, op2):
		"""Function to divide the operands"""
		try:
			return op1 / op2
		except ZeroDivisionError:
			sys.exit ("Division by zero is not allowed")

	def mult(self, op1, op2):
		"""Function to multiply the operands"""
		return op1 * op2

if __name__ == "__main__":
	try:
		operando1 = int(sys.argv[1])
		operando2 = int(sys.argv[3])
	except ValueError:
		sys.exit("Error: Parametros no numéricos")
	
	Operacion = CalculadoraHija()
	
	if sys.argv[2] == "suma":
		result = Operacion.plus(operando1, operando2)
	elif sys.argv[2] == "resta":
		result = Operacion.minus(operando1, operando2)
	elif sys.argv[2] == "divide":
		result = Operacion.div(operando1, operando2)
	elif sys.argv[2] == "multiplica":
		result = Operacion.mult(operando1, operando2)
	else:
		sys.exit("Operaciones permitidas: suma, resta, division, multiplicacion")
		
		
	print (result)

