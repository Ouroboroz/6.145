import math
class Vector:
	def __init__(self,vec):
		self.vec = vec
	def as_list(self):
		return self.vec
	def size(self):
		return len(self.vec)
	def magnitude(self):
		total = 0
		for i in self.vec:
			total += i*i
		return total**(0.5)
	def euclidean_distance(self,other):
		total = 0
		for i in range(len(self.vec)):
			total += (self.vec[i]-other.as_list()[i])**2
		return total**(0.5)
	def normalized(self):
		mag = self.magnitude()
		vec = self.vec
		for i in range(len(vec)):
			vec[i] /= mag
		return Vector(vec)
	def cosine_similarity(self,other):
		total = 0
		for i in range(len(self.vec)):
			total += self.vec[i]*other.as_list()[i]
		return total/(self.magnitude()*other.magnitude())
	def __add__(self,other):
		if not isinstance(other,Vector):
			return None
		if self.size() != other.size():
			return None
		vec = []
		for i in range(len(self.vec)):
			vec.append(self.vec[i]+other.as_list()[i])
		return Vector(vec)
	def __sub__(self,other):
		if not isinstance(other,Vector):
			return None
		if self.size() != other.size():
			return None
		vec = []
		for i in range(len(self.vec)):
			vec.append(self.vec[i]-other.as_list()[i])
		return Vector(vec)
	def __mul__(self,other):
		vec = []
		if isinstance(other,int) or isinstance(other,float):
			for i in self.vec:
				vec.append(i*other)
			return Vector(vec)
		elif isinstance(other,Vector):
			if self.size() != other.size():
				return None
			tot = 0
			for i in range(len(self.vec)):
				tot += self.vec[i]*other.as_list()[i]
			return tot
		else:
			return None
	def __truediv__(self,other):
		if isinstance(other,int) or isinstance(other,float):
			if(other == 0):
				return None
			vec = []
			for i in self.vec:
				vec.append(i/other)
			return Vector(vec)
		return None