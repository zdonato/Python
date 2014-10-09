import math
EPSILON = 1.9 * 10 ** -9

def nlogn(c):
	lower = 0.0
	upper = c
	while True:
		middle = lower + (upper-lower)/2
		val = middle * math.log(middle, 2)
		if abs(c-val) < EPSILON:
			return int(middle)
		if val > c:
			upper = middle
		else:
			lower = middle

print nlogn(3600000)
