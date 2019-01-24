kwh_used = 1000
if(kwh_used <= 500):
	print((kwh_used*0.57)*1.2)
else:
	if(kwh_used <= 1500):
		print((500*0.57 + (kwh_used-500)*0.77)*1.2)
	else:
		if(kwh_used <= 2500):
			print((500*0.57 + 1000*0.77 + (kwh_used-1500)*1.30)*1.2)
		else:
			print((500*0.57 + 1000*0.77 +1000*1.30+(kwh_used-2500)*1.74)*1.2)