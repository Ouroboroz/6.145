def prime(x):
	if(x == 0 or x==1):
		return False
	else:
		if(x==2):
			return True
		for i in range(2,int(x**0.5)+2):
			if x % i == 0:
				return False
	return True
