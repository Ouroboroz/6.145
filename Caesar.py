def caesar_cipher(string, integer):
	string = string.lower()
	nospace = string
	newstring = []
	for i in range(len(nospace)):
		for j in nospace[i]:
			if(j.isalpha()):
				newstring.append(chr((ord(j)-97+integer)%26+97))
			elif(j.isdecimal()):
				newstring.append(str((int(j)+integer)%10))
			else:
				newstring.append(j)
	return "".join(newstring)