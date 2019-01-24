import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to_origin(self):
        return (self.x**2 + self.y**2)**0.5

    def euclidean_distance(self, other):
        return ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5

    def manhattan_distance(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)

    def angle_between(self, other):
        vert = other.y - self.y
        horiz = other.x - self.x
        return math.atan2(vert, horiz)

class Triangle:
    def __init__(self,A,B,C):
        self.A = A
        self.B = B
        self.C = C
    def equal(self,float1, float2):
        if (float1-float2)**2 < 10**(-6):
            return True
        return False
    def abs(i):
        if i < 0:
            return -i
        return i
    def side_lengths(self):
        return (self.A.euclidean_distance(self.B),self.A.euclidean_distance(self.C),self.B.euclidean_distance(self.C))
    def angles(self):
        z = self.side_lengths()[0]
        x = self.side_lengths()[1]
        c = self.side_lengths()[2]
        q = math.acos((z**2+x**2-c**2)/(2.0*z*x))
        w = math.acos((z**2-x**2+c**2)/(2.0*z*c))
        e = math.acos((-z**2+x**2+c**2)/(2.0*c*x))
        return (q,w,e)
    def side_classification(self):
        q = self.side_lengths()
        if self.equal(q[0],q[1]) or self.equal(q[0],q[2]) or self.equal(q[1],q[2]):
            if self.equal(q[0]+q[1],2*q[2]):
                return "equilateral"
            return "isosceles"
        return "scalene"
    def is_right(self):
        if self.equal(self.angles()[0],math.pi/2) or self.equal(self.angles()[1],math.pi/2) or self.equal(self.angles()[2],math.pi/2):
            return True
        return False
    def angle_classification(self):
        if self.is_right():
            return "right"
        if self.equal(self.angles()[0],self.angles()[1]) and self.equal(self.angles()[1],self.angles()[2]):
            return "equiangular"
        if self.angles()[0] < math.pi/2 and self.angles()[1] < math.pi/2 and self.angles()[2] < math.pi/2:
            return "acute"
        return "obtuse"
    def area(self):
        s = (self.side_lengths()[0]+self.side_lengths()[1]+self.side_lengths()[2])/2
        return math.sqrt(s*(s-self.side_lengths()[0])*(s-self.side_lengths()[1])*(s-self.side_lengths()[2]))
    def perimeter(self):
        return self.side_lengths()[0] + self.side_lengths()[1] + self.side_lengths()[2]