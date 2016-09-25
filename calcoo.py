#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

class Calculadora:
	def plus(self, op1, op2):	
		""" Function to sum the operands """
		return op1 + op2


	def minus(self, op1, op2):
		""" Function to substract the operands """
		return op1 - op2

if __name__ == "__main__":
	try:
		operando1 = int(sys.argv[1])
		operando2 = int(sys.argv[3])
	except ValueError:
		sys.exit("Error: Non numerical parameters") 

	Operacion = Calculadora()
	
	if sys.argv[2] == "suma":
		result = Operacion.plus(operando1, operando2)
	elif sys.argv[2] == "resta":
		result = Operacion.minus(operando1, operando2)
	else:
		sys.exit('Operación sólo puede ser sumar o restar.')

	print(result)
