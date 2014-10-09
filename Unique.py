def Unique(L):
	if L == []:
		return True
	if L[0] in L[1:]:
		return False
	else: 
		return Unique(L[1:])
		
print Unique([1,2,3,4])