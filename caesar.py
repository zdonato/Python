ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', \
'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
P = 1
MODIFIER = 10 

def findNum(char):
	count = 0; 
	while (ALPHABET[count] != char):
		count += 1
	return count
	
def findLetter(num):
	return ALPHABET[num]

def getNums(text): 
	out = []
	for i in range(0, len(text)):
		if text[i] == " ": 
			out += [" "]
		else:
			out += [findNum(text[i])]
	return out
	
def encrypt(text):
	out = ""
	nums = getNums(text)
	for i in range(0, len(nums)):
		if nums[i] == " ":
			out += " "
		else:
			out += findLetter(((P * nums[i]) + MODIFIER) % 26)
	return out.upper()
	
def decrypt(text):
	out = ""
	nums = getNums(text)
	for i in range(0, len(nums)):
		if nums[i] == " ":
			out += " "
		else:
			out += findLetter(((P * nums[i]) - MODIFIER) % 26)
	return out.upper()
	
print getNums("attack")


		

		
	