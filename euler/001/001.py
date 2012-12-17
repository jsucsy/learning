'''
jsu
created 16 Dec 2012
last edited 16 Dec 2012
*** correct solution***
'''

def sum_multiples(multiplier, limit):
	'''sum the multiples of multiplier under limit'''      
	values = []
	x = 1
	while (x * multiplier) < limit:
#		print "added 	
		values.append(x * multiplier)
		x += 1

	return values

if __name__ == '__main__':
	'''run as main'''
	LIMIT = 1000
	three = sum_multiples(3, LIMIT) 
	five = sum_multiples(5, LIMIT)
	
	for f in five:
		if f not in three: 
			three.append(f)

	sum = 0
	for val in three:
		sum += val

	print sum
	

