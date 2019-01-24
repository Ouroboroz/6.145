a = 1
b = 2
c = 3

d = b**2 - 4*a*c
if(a == 0):
	print(-c/b)
else:
	if(d == 0):
		print(-b/(2*a))
	else:
		print((-b+d**0.5)/(2*a))
		print((-b-d**0.5)/(2*a))