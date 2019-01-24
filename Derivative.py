poly = [0,0,1/2]
new_poly = []
for index in range(1,len(poly)):
	new_poly.append(poly[index]*index)
print(new_poly)