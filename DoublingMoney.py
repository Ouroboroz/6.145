interest_rate = 1
def time_taken():
	if(interest_rate == 0):
		return "NEVER"
	start = 1
	time = 0
	while start < 2:
		start *= (1+interest_rate)
		time += 1
	return time
print(time_taken())
