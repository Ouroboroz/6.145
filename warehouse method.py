def warehouse_process(dict,transaction):
	if transaction[0] == 'receive':
		if transaction[1] in dict.keys():
			dict[transaction[1]] += transaction[2]
		else:
			dict[transaction[1]] = transaction[2]
	else:
		dict[transaction[1]] -= transaction[2]