poly = [0,0,1/2]
const = 1
new_poly = [const]
for i in range(len(poly)):
	new_poly.append(poly[i]/(i+1))
print(new_poly)