
import sys
sys.setrecursionlimit(100000)
n=0
def Ack(x, y):
	global n
	n += 1
	if x == 0:
		return y+1
	elif x > 0 and y == 0:
		return Ack(x-1, 1)
	elif x > 0 and y > 0:
		return Ack(x-1, Ack(x, y-1))
	else:
		return None
print(Ack(3,0))
print(n)
n=0
print(Ack(3,6))
print(n)