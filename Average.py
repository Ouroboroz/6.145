numbers = [2,7,3,9,13]
def mean(input):
	if(input == []):
		return "None"
	sum = 0
	for num in numbers: 
		sum += num
	return sum/len(numbers)

print(mean(numbers))