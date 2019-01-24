def ndoors(n):
	doors = [False]*n
	for i in range(1,n+1):
		for j in range(i,n+1,i):
			doors[j-1] = not doors[j-1]
	count = []
	for i in range(len(doors)):
		if(doors[i]):
			count.append(i+1)
	return count
print(ndoors(100))