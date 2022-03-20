# Iterators
# define a list
my_list = [4, 7, 0, 3]

# get an iterator using iter()
my_iter = iter(my_list)

# iterate through it using next()

# Output: 4
print(next(my_iter))

# Output: 7
print(next(my_iter))

# next(obj) is same as obj.__next__()

# Output: 0
print(my_iter.__next__())

# Output: 3
print(my_iter.__next__())

# This will raise error, no items left
#next(my_iter)

# Here, we show an example that will give us the next power of 2 in each iteration.
# Power exponent starts from zero up to a user set number.

class PowTwo(object):
	"""docstring for PowTwo"""
	def __init__(self, max=0):
		self.max = max

	def __iter__(self):
		self.n = 0
		return self

	def __next__(self):
		if self.n <= self.max:
			result = 2 ** self.n
			self.n +=1
			return result
		else:
			raise StopIteration


# create an object
numbers = PowTwo(3)

# create an iterable from the object
i = iter(numbers)

# Using next to get to the next iterator element
print(next(i))
print(next(i))
print(next(i))
print(next(i))

# We can also use a for loop to iterate over our iterator class.
for i in PowTwo(5):
	print(i)

# We can also build our own infinite iterators. The following iterator will, theoretically, return all the odd numbers.

class InfIter(object):
	"""Infinite iterator to return all
        odd numbers"""
	def __iter__(self):
		self.num = 1
		return self

	def __next__(self):
		num = self.num
		self.num +=2
		return num

a = iter(InfIter())
print(next(a))
print(next(a))
print(next(a))
print(next(a))

# A simple generator function
def my_gen():
	n = 1
	print('This is printed first')
	yield n

	n += 1
	print('This is printed second')
	yield n

	n += 1
	print('This is printed last')
	yield n

	return n

# It returns an object but does not start execution immediately.
a = my_gen()

# We can iterate through the items using next().
next(a)
next(a)
next(a)
#next(a)

# Using for loop
for item in my_gen():
    print(item)

# the generator object can be iterated only once.

# To restart the process we need to create another generator object using something like a = my_gen().

# Python Generators with a Loop
def rev_str(my_str):
	length = len(my_str)
	for i in range(length-1, -1, -1):
		yield my_str[i]

for char in rev_str("hello"):
	print(char)


# Simple generators can be easily created on the fly using generator expressions. It makes building generators easy.
# Similar to the lambda functions which create anonymous functions, generator expressions create anonymous generator functions.
# The syntax for generator expression is similar to that of a list comprehension in Python. But the square brackets are replaced with round parentheses.
# The major difference between a list comprehension and a generator expression is that a list comprehension produces the entire list while the generator expression produces one item at a time.
# They have lazy execution ( producing items only when asked for ). For this reason, a generator expression is much more memory efficient than an equivalent list comprehension.

# Initialize the list
my_list = [1, 3, 6, 10]

# square each term using list comprehension
list_ = [x**2 for x in my_list]

# same thing can be done using a generator expression
# generator expressions are surrounded by parenthesis ()
generator = (x**2 for x in my_list)

print(list_)
print(generator)

print(next(generator))

# Generator expressions can be used as function arguments. When used in such a way, the round parentheses can be dropped.
print(sum(x**2 for x in my_list))
print(max(x**2 for x in my_list))
print(sum([x**2 for x in my_list]))

# Use of Python Generators
# 1 Easy to Implement
# 2 Memory Efficient
# 3 Represent Infinite Stream
# 4 Pipelining Generators


def PowTwoGen(max=0):
	n = 0
	while n < max:
		yield 2**n
		n +=1

for n in PowTwoGen(3):
	print(n)

a = PowTwoGen(4)
print(next(a))

# Multiple generators can be used to pipeline a series of operations
def fibo(nums):
	x, y = 0,1
	for _ in range(nums):
		x, y = y, x+y
		yield x

# a= fibo(5)
# print(next(a))
# print(next(a))
# print(next(a))

def square(nums):
	for num in nums:
		yield num**2

print(sum(fibo(5)))
print(sum(square(fibo(5))))

# closure in Python
# This value in the enclosing scope is remembered even when the variable goes out of scope or the function itself is removed from the current namespace.

def print_msg(msg):
	# This is the outer enclosing function
	def printer():
		# This is the nested function
		print(msg)

	return printer # returns the nested function

another = print_msg("Hello")
another()

# Here is a simple example where a closure might be more preferable than defining a class and making objects. But the preference is all yours.

def make_multiple_of(n):
	def multiplier(x):
		return x*n

	return multiplier

# Multiplier of 3
times3 = make_multiple_of(3)


# Multiplier of 5
times5 = make_multiple_of(5)

print(times3(9))

print(times5(3))

del make_multiple_of
# works even parent function deleted
print(times5(times3(2)))

# All function objects have a __closure__ attribute that returns a tuple of cell objects if it is a closure function
print(times3.__closure__)
print(times3.__closure__[0].cell_contents)
print(times5.__closure__[0].cell_contents)
# print(make_multiple_of.__closure__)

# Python Decorators
# A decorator takes in a function, adds some functionality and returns it.
# to add functionality to an existing code.
# This is also called metaprogramming because a part of the program tries to modify another part of the program at compile time.

# Functions that take other functions as arguments are also called higher order functions

def inc(x):
	return x+1

def dec(x):
	return x-1

def operate(func, x):
	result = func(x)
	return result

print(operate(inc, 3))
print(operate(dec, 3))

# A function can return another function.
def is_called():
	def is_returned():
		print("Hello")
	return is_returned

new = is_called()
new()
