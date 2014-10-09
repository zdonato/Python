import time
import sys

sys.setrecursionlimit(100000)

def n_cubed_rec(n):
	if n == 1:
		return 1
	else:
		return n_cubed_rec(n-1) + (n ** 3)
		
def n_cubed(n):
	return ((n*(n+1))/2) ** 2
	

def test(n):
	t0 = time.time() 
	print n_cubed_rec(n)
	t1 = time.time()
	print "Time of recursive: " + str(t1-t0)
	t0 = time.time()
	print n_cubed(n)
	t1 = time.time()
	print "Time of non-recursive: " + str(t1-t0)

test(10000)