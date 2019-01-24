class Rational:
	def __init__(self,x,y):
		self.x = x
		self.y = y
	def get_numerator(self):
		return self.x
	def get_denominator(self):
		return self.y
	def to_float(self):
		return (1.0*self.x)/self.y
	def reciprocal(self):
		return Rational(self.y,self.x)
	def gcd(self,a,b):
		if(b==0):
			return a
		else:
			return self.gcd(b,a%b)
	def reduce(self):
		a = self.x
		b = self.y
		while(self.gcd(a,b) != 1):
			c = self.gcd(a,b)
			a /= c
			b /= c
		return Rational(int(a),int(b))
	def __add__(self,other):
		if isinstance(other,int):
			return Rational(self.x+self.y*other,self.y)
		if isinstance(other, Rational):
			return Rational(self.x*other.get_denominator()+other.get_numerator()*self.y,self.y*other.get_denominator())
		if isinstance(other,float):
			return self.to_float() + other
		return None
	def __mul__(self,other):
		if isinstance(other,int):
			return Rational(self.x*other,self.y)
		if isinstance(other, Rational):
			return Rational(self.x*other.get_numerator(),self.y*other.get_denominator())
		if isinstance(other,float):
			return self.to_float() * other
		return None
	def __truediv__(self,other):
		if isinstance(other,int):
			return Rational(self.x,self.y*other)
		if isinstance(other, Rational):
			return self.__mul__(other.reciprocal())
		if isinstance(other,float):
			return self.to_float() / other
		return None
	def __sub__(self,other):
		if isinstance(other,int):
			return Rational(self.x-self.y*other,self.y)
		if isinstance(other, Rational):
			return Rational(self.x*other.get_denominator()-other.get_numerator()*self.y,self.y*other.get_denominator())
		if isinstance(other,float):
			return self.to_float() - other
		return None

