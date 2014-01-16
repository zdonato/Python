# Function to calculate a simple derivative. 

def derivative():
	''' Function returns the derivative '''
	# Initialize variables.
	coefficients = []
	powers = []
	deriv = []
	out = ""
	s = ""
	# Find number of terms.
	num_terms = raw_input("How many terms: ")
	# For each term, get the coefficient and power. Store in arrays. 
	for i in range(int(num_terms)):
		term = raw_input("Enter term " + str(i+1) + "'s coefficient: ")
		pow = raw_input("Enter the power of term " + str(i+1) + ": ")
		coefficients += [term]
		powers += [pow]
		
	# Calculate the derivative of each individual term.
	for j in range(len(coefficients)):
		if powers[j] == "1": 
			deriv += [str(int(powers[j]) * int(coefficients[j]))]
		elif powers[j] == "0": 
			deriv += ["0"]
		else: 
			new_pow = int(powers[j]) - 1
			temp = int(powers[j]) * int(coefficients[j])
			if new_pow == 0:
				s =  str(temp) + " + "
				deriv += [s]
			elif new_pow == 1: 
				s = str(temp) + "x" + " + "
				deriv += [s]
			else: 
				s = str(temp) + "x^"+ str(new_pow) + " + "
				deriv += [s] 
				
	# Form an output string			
	for k in range(len(deriv)):
		if deriv[k] == "0": 
			continue
		else: 
			out += deriv[k]
	
	# Get rid of the trailing + sign and white space. 
	if out[-3:] == " + ":
		print out[:-3]
	else:
		print out

derivative()
			
		
		
		
 
