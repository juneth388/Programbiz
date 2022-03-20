class Parrot:

	# class attribute
	species = "bird"

	# instance attribute
	def __init__(self, name, age):
		self.name = name
		self.age = age

	# instance method
	def sing(self, song):
		return "{} sings {}".format(self.name, song)

	# instance method
	def dance(self):
		return "{} is dancing now".format(self.name)

# instantiate the parrot classs
blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)

# access the class attributes
print("Blu is a {}".format(blu.__class__.species))
print("Woo is also a {}".format(woo.__class__.species))

# access the instance attributes
print("{} is {} years old".format(blu.name, blu.age))
print("{} is {} years old".format(woo.name, woo.age))

# call our instance methods
print(blu.sing("'Happy'"))
print(blu.dance())

# Inheritance
# parent class
class Bird:

	"""docstring for Bird"""
	def __init__(self):
		print("Bird is ready")

	def whoisThis(self):
		print("Bird")

	def swim(self):
		print("Swim faster")


# child class
class Penguin(Bird):

	"""docstring for Penguin"""
	def __init__(self):
		# call super() function
		super().__init__()
		print("Penguin is ready")

	def whoisThis(self):
		print("Penguin")

	def run(self):
		print("Run faster")

peggy = Penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()


# Encapsulation
class Computer:

	def __init__(self):
		self.__maxprice = 900

	def sell(self):
		print("Selling price: {}".format(self.__maxprice))

	def setMaxPrice(self,price):
		self.__maxprice = price

dell = Computer()
dell.sell()

# change the price
dell.__maxprice = 1000
dell.sell()

# using the setter method
dell.setMaxPrice(1000)
dell.sell()

# Polymorphism
class Parrot:

	def fly(self):
		print("Parrot can fly")

	def swim(self):
		print("Parrot can't swim")

class Penguin:

	def fly(self):
		print("Penguin can't fly")

	def swim(self):
		print("Penguin can swim")

# common interface
def flying_test(bird):
	bird.fly()

def swim_test(bird):
	bird.swim()

# instantiate objects
blu = Parrot()
peggy = Penguin()

# passing the object
flying_test(blu)
flying_test(peggy)
swim_test(blu)
swim_test(peggy)

# Constructors
class ComplexNumber():
	"""docstring for ComplexNumber"""
	def __init__(self, r=0, i=0):
		self.real = r
		self.imag = i

	def get_data(self):
		print(f'{self.real}+{self.imag}j')

# Create a new Complex Number object
num1 = ComplexNumber(2,3)

num1.get_data()

# Create another Complex Number object
num2 = ComplexNumber(5)
num2.attr = 10

print((num2.real, num2.imag, num2.attr))

#print(num1.attr) #error

#del num1.imag
#del ComplexNumber.get_data
#del c1

class Polygon:
	"""docstring for Polygon"""
	def __init__(self, no_of_sides):
		self.n = no_of_sides
		self.sides = [0 for i in range(no_of_sides)]

	def inputSides(self):
		self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]

	def dispSides(self):
		for i in range(self.n):
			print("Side",i+1,"is", self.sides[i])

class Triangle(Polygon):

	def __init__(self):
		# super().__init__(3)
		Polygon.__init__(self,3)

	def findArea(self):
		a, b, c = self.sides
		# calculare the semi-perimeter
		s = (a + b + c) / 2
		area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
		print('The area of the triangle is %0.2f' %area)

t = Triangle()
# t.inputSides()
# t.dispSides()
# t.findArea()

isinstance(t,Triangle)
isinstance(t,Polygon)
isinstance(t,int)
isinstance(t,object)
issubclass(Polygon,Triangle)
issubclass(Triangle,Polygon)
issubclass(bool,int)

# Every class in Python is derived from the object class. It is the most base type in Python.
print(issubclass(list,object))

# Demonstration of Method Resolution Order (MRO).
class X:
	pass

class Y:
	pass

class Z:
	pass

class A(X,Y):
	pass

class B(Y,Z):
	pass

class M(B, A, Z):
	pass

print(M.mro())  #M.__mro__

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


p1 = Point(1, 2)
p2 = Point(2, 3)
# print(p1+p2)

class Point(object):
	"""docstring for Point"""
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y

	def __str__(self):
		return "({0}, {1})".format(self.x, self.y)

	def __add__(self, other):
		x = self.x + other.x
		y = self.y + other.y
		return Point(x, y)

p1 = Point(1, 2)
p2 = Point(2, 3)
print(p1)

# What actually happens is that, when you use p1 + p2, Python calls p1.__add__(p2) which in turn is Point.__add__(p1,p2)
print(p1+p2)

str(p1)
format(p1)
