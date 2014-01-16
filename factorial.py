# Factorial function. 

def fact(n): 
	''' Returns the factorial of n recursively '''
	if n == 1: 
		return 1
	else: 
		return n * fact(n-1)
		
print fact(5)