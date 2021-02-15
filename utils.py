# utils.py
# Math library
# Author: Sébastien Combéfis
# Version: February 8, 2018
from math import sqrt
from scipy.integrate import quad

def fact(n):
	"""Computes the factorial of a natural number.
	
	Pre: -
	Post: Returns the factorial of 'n'.
	Throws: ValueError if n < 0
	"""
	if n >= 0 : 
		count = 1
		for num in range(1,n+1):
			count *= num
		return count
	else :
		raise ValueError



def roots(a, b, c):
	"""Computes the roots of the ax^2 + bx + x = 0 polynomial.
	
	Pre: -
	Post: Returns a tuple with zero, one or two elements corresponding
		to the roots of the ax^2 + bx + c polynomial.
	"""
	delta = b**2 - 4*a*c
	if delta > 0 :
		root1 = (-b+sqrt(delta))/2*a
		root2 = (-b-sqrt(delta))/2*a
		return (root1,root2)
	if delta == 0 : 
		return (-b/2*a)
	if delta < 0 :
		return("No roots")



def integrale(function, lower, upper):
	"""Approximates the integral of a fonction between two bounds
	
	Pre: 'function' is a valid Python expression with x as a variable,
		'lower' <= 'upper',
		'function' continuous and integrable between 'lower‘ and 'upper'.
	Post: Returns an approximation of the integral from 'lower' to 'upper'
		of the specified 'function'.

	Hint: You can use the 'integrate' function of the module 'scipy' and
		you'll probably need the 'eval' function to evaluate the function
		to integrate given as a string.
	"""
	def f(x):
		return eval(function)
	int = quad(f,lower,upper)
	return int[0]

if __name__ == '__main__':
	print(fact(5))
	print(roots(1, 3, 1))
	print(integrale('x+1', -1, 1))
