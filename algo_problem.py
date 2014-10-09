import math

def while_greater():
	n = 2; 
	func1 = n
	func2 = 6 * math.log(n, 2)
	count = 0
	
	while (func1 < func2):
		count += 1
		n += 1
		func1 = n
		func2 = 6 * math.log(n, 2)
	
	return count
	
print while_greater()