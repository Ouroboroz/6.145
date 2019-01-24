def second_largest_number(x):
	if(len(x) == 0 or len(x) == 1):
		return None
	else:
		#This is largest first then second largest
		if(x[0] > x[1]):
			snek = [x[0],x[1]]
		else:
			snek = [x[1],x[0]]
		for i in range(2,len(x)):
			if(x[i] > snek[0]):
				snek[0] = x[i]
			elif(x[i] > snek[1]):
				snek[1] = x[i]
		return snek[1]