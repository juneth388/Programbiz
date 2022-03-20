# Decorators

# Functions and methods are called callable as they can be called.

# In fact, any object which implements the special __call__() method is termed callable.
# So, in the most basic sense, a decorator is a callable that returns a callable.

# Basically, a decorator takes in a function, adds some functionality and returns it.

def make_pretty(func):
	def inner():
		print("I got decorated")
		func()

	return inner

def ordinary():
	print("I am ordinary")

ordinary()

# let's decorate this ordinary function
pretty = make_pretty(ordinary)
pretty()

# In the example shown above, make_pretty() is a decorator
# pretty = make_pretty(ordinary)
# The function ordinary() got decorated and the returned function was given the name pretty.

@make_pretty
def ordinary():
    print("I am ordinary")
# is equivalent to
def ordinary():
    print("I am ordinary")
ordinary = make_pretty(ordinary)

# Decorating Functions with Parameters

def smart_divide(func):
	def inner(a, b):
		print("I am going to divide", a , "and", b)
		if b == 0:
			print("Whoops! cannot divide")
			return

		return func(a, b)
	return inner

@smart_divide
def divide(a, b):
	print(a/b)

divide(2, 5)
divide(2, 0)

# Multiple decorators can be chained in Python.
def star(func):
	def inner(*args, **kwargs):
		print("*" * 30)
		func(*args, **kwargs)
		print("*" * 30)
	return inner

def percent(func):
	def inner(*args, **kwargs):
		print("%" * 30)
		func(*args, **kwargs)
		print("%" * 30)
	return inner

@star
@percent
def printer(msg):
	print(msg)

printer("Hello")

# is equivalent to
def printer(msg):
    print(msg)
printer = star(percent(printer))



def operate(func):
	def rr(x):
		print('in deco')
		return func(x)
	return rr

def inc(x):
    return x + 1

@operate
def dec(x):
    return x - 1

print(dec(3))

# Python @property decorator

# Python programming provides us with a built-in @property decorator which makes usage of getter and setters 
# much easier in Object-Oriented Programming.

# Basic method of setting and getting attributes in Python
class Celsius(object):

	"""docstring for Celsius"""
	def __init__(self, temperature = 0):
		self.temperature = temperature

	def to_fahrenheit(self):
		return (self.temperature * 1.8) + 32

# Create a new object
human = Celsius()

# Set the temperature
human.temperature = 37

# Get the temperature attribute
print(human.temperature)

# Get the to_fahrenheit method
print(human.to_fahrenheit())
# The extra decimal places when converting into Fahrenheit is due to the floating point arithmetic error.

# Whenever we assign or retrieve any object attribute like temperature as shown above, 
# Python searches it in the object's built-in __dict__ dictionary attribute.
print(human.__dict__)

# human.temperature internally becomes human.__dict__['temperature']


# Making Getters and Setters methods
class Celsius:
	def __init__(self, temperature = 0):
		self.set_temperature(temperature)

	def to_fahrenheit(self):
		return (self.get_temperature() * 1.8) +32

	# getter method
	def get_temperature(self):
		return self._temperature

	# setter method
	def set_temperature(self, value):
		if value < -273.15:
			raise ValueError("temperature below -273.15 is not possible.")
		self._temperature = value


# Create a new object, set_temperature() internally called by __init__
human = Celsius(37)

# Get the temperature attribute via a getter
print(human.get_temperature())

# Get the to_fahrenheit method, get_temperature() called by the method itself
print(human.to_fahrenheit())


# new constraint implementation
#human.set_temperature(-300)

# Get the to_fahreheit method
print(human.to_fahrenheit())

# The private variables don't actually exist in Python. There are simply norms to be followed. 
# The language itself doesn't apply any restrictions.

# using property class
class Celsius(object):
	"""docstring for Celsius"""
	def __init__(self, temperature = 0):
		self.temperature = temperature

	def to_fahrenheit(self):
		return (self.temperature * 1.8)+ 32

	# getter
	def get_temperature(self):
		print("Getting value...")
		return self._temperature

	# setter
	def set_temperature(self, value):
		print("Setting value...")
		if value < -273.15:
			raise ValueError("temperature below -273.15 is not possible")
		self._temperature = value

	# creating a property object
	temperature = property(get_temperature, set_temperature)

human = Celsius(37)

print(human.temperature)
print(human.to_fahrenheit())
# human.temperature = -300

# Any code that retrieves the value of temperature will automatically call get_temperature() instead of a dictionary (__dict__) look-up.
# Similarly, any code that assigns a value to temperature will automatically call set_temperature().


# The reason is that when an object is created, the __init__() method gets called. 
# This method has the line self.temperature = temperature. This expression automatically calls set_temperature().

# Similarly, any access like c.temperature automatically calls get_temperature(). This is what property does.

human.temperature

human.temperature = 37

# The actual temperature value is stored in the private _temperature variable. 
# The temperature attribute is a property object which provides an interface to this private variable.

# In Python, property() is a built-in function that creates and returns a property object.
# The syntax of this function is:
# property(fget=None, fset=None, fdel=None, doc=None)

# fget is function to get value of the attribute
# fset is function to set value of the attribute
# fdel is function to delete the attribute
# doc is a string (like a comment)

# A property object has three methods, getter(), setter(), and deleter() to specify fget, fset and fdel at a later point.

# We can even not define the names get_temperature and set_temperature as they are unnecessary and pollute the class namespace.

# For this, we reuse the temperature name while defining our getter and setter functions


class Celsius(object):
	"""docstring for Celsius class with property decorator"""
	def __init__(self, temperature = 0):
		self.temperature = temperature

	def to_fahrenheit(self):
		return (self.temperature * 1.8) + 32

	@property
	def temperature(self):
		print("Getting value...")
		return self._temperature

	@temperature.setter
	def temperature(self, value):
		print("Setting value...")
		if value < -273.15 :
			raise ValueError("Temperature below -273.15 is not possible")
		self._temperature = value

print('property decorater')
# create an object
human = Celsius(37)

print(human.temperature)

print(human.to_fahrenheit())

# coldest_thing = Celsius(-300)