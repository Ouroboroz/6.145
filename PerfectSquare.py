def perfect_square(x):
	for i in range(0,int(x**0.5)+2):
		if i**2 == x:
			return True
	return False
