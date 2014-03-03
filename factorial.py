# Factorial function. 

def fact(): 
	''' Returns the factorial of n recursively '''
	ret = 1
	n = raw_input("Enter number: ")
	num = int(n)
	for i in range(num):
		ret *= num
		num -= 1
	return ret	
	
print fact()