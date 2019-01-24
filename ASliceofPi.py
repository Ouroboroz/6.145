p_d = 5
circle_cell = 0
for i in range(-int(p_d/2),int(p_d/2)+1):
	for j in range(-int(p_d/2),int(p_d/2)+1):
		if (i**2+j**2)**(1/2) <= p_d/2:
			circle_cell += 1
print(circle_cell/p_d**2*4)