# In Python, we don't actually assign values to the variables. Instead, Python gives the reference of the object(value) to the variable.

# type-inferred = dynamic language = (a=10) no type defined.

#In reality, we don't use constants in Python. Naming them in all capital letters is a convention to separate them from variables

# Numeric literals in Python?
a = 0b1010 #Binary Literals
b = 100 #Decimal Literal 
c = 0o310 #Octal Literal
d = 0x12c #Hexadecimal Literal

#Float Literal
float_1 = 10.5 
float_2 = 1.5e2

#Complex Literal 
x = 3.14j

print(a, b, c, d)
print(float_1, float_2)
print(x, x.imag, x.real)

# When we print the variables, all the literals are converted into decimal values.
# output
# 10 100 200 300
# 10.5 150.0
# 3.14j 3.14 0.0

# A floating-point number is accurate up to 15 decimal places.

# List is an ordered sequence of items. It is one of the most used datatype in Python and is very flexible.
# All the items in a list do not need to be of the same type.
# Lists are mutable, meaning, the value of elements of a list can be altered.

a = [1, 2.2, 'python']


# Tuple is an ordered sequence of items same as a list. The only difference is that tuples are immutable.

t = (5,'program', 1+3j)

# Strings, however, are immutable.
# s[5] ='d' # Generates error


# Set is an unordered collection of unique items. The only difference is that tuples are immutable.
a = {5,2,3,1,4}
# We can perform set operations like union, intersection on two sets. Sets have unique values. They eliminate duplicates.
# Since, set are unordered collection, indexing has no meaning. Hence, the slicing operator [] does not work.

# Dictionary is an unordered collection of key-value pairs.

# he actual syntax of the print() function is:
# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False) sys.stdout (screen)

print(1, 2, 3, 4)
print(1, 2, 3, 4, sep='*')
print(1, 2, 3, 4, sep='#', end='&')

print('Hello {name}, {greeting}'.format(greeting = 'Goodmorning', name = 'John'))

x = 12.3456789
print('The value of x is %3.2f' %x) # try %3.4f


int('10')
float('10')
# This same operation can be performed using the eval() function. But eval takes it further. 
# It can evaluate even expressions, provided the input is a string
# int('2+3') #ValueError
eval('2+3')

#  Everything in Python is an object. Name is a way to access the underlying object.
# when we do the assignment a = 2, 2 is an object stored in memory and a is the name we associate it with. 
# We can get the address (in RAM) of some object through the built-in function id().


# Note: You may get different values for the id

a = 2
print('id(2) =', id(2))

print('id(a) =', id(a))

# a namespace is a collection of names.
# In Python, you can imagine a namespace as a mapping of every name you have defined to corresponding objects.


# range(start, stop,step_size)

# The range object is "lazy" in a sense because it doesn't generate every number that it "contains" when we create it. 
# However, it is not an iterator since it supports in, len and __getitem__ operations.
# This function does not store all the values in memory; it would be inefficient. 
# So it remembers the start, stop, step size and generates the next number on the go.


# To force this function to output all the items, we can use the function list().
print(range(10))

print(list(range(10)))

print(list(range(2, 8)))

print(list(range(2, 20, 3)))

# A for loop can have an optional else block as well. The else part is executed if the items in the sequence used in for loop exhausts.
# The break keyword can be used to stop a for loop. In such cases, the else part is ignored.
# Same for while loop

# In Python programming, the pass statement is a null statement. The difference between a comment and a pass statement 
# in Python is that while the interpreter ignores a comment entirely, pass is not ignored.
# However, nothing happens when the pass is executed. It results in no operation (NOP).

# https://www.programiz.com/python-programming/function
# In python, the function definition should always be present before the function call. Otherwise, we will get an error.

# The lifetime of a variable is the period throughout which the variable exists in the memory.
# The lifetime of variables inside a function is as long as the function executes.

# Having a positional argument after keyword arguments will result in errors
# greet(name="Bruce","How do you do?")

# (x * factorial(x-1))

# By default, the maximum depth of recursion is 1000. If the limit is crossed, it results in RecursionError

# Advantages of Recursion

    # Recursive functions make the code look clean and elegant.
    # A complex task can be broken down into simpler sub-problems using recursion.
    # Sequence generation is easier with recursion than using some nested iteration.


# Disadvantages of Recursion

    # Sometimes the logic behind recursion is hard to follow through.
    # Recursive calls are expensive (inefficient) as they take up a lot of memory and time.
    # Recursive functions are hard to debug.

# An anonymous function is a function that is defined without a name.
# While normal functions are defined using the def keyword in Python, anonymous functions are defined using the lambda keyword.
# lambda arguments: expression

# Program to show the use of lambda functions
double = lambda x: x * 2

print(double(5))

# This function has no name. It returns a function object which is assigned to the identifier double

# The function is called with all the items in the list and a new list is returned which contains items 
# for which the function evaluates to True.

# Program to filter out only the even items from a list
my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(filter(lambda x: (x%2 == 0) , my_list))

print(new_list)

# The map() function in Python takes in a function and a list.
# The function is called with all the items in the list and a new list is returned which contains items returned by 
# that function for each item.

# Program to double each item in a list using map()

my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(map(lambda x: x * 2 , my_list))

print(new_list)

# Nonlocal variables are used in nested functions whose local scope is not defined.
# This means that the variable can be neither in the local nor the global scope.

def outer():
    x = "local"

    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)

    inner()
    print("outer:", x)


outer()

# output
# inner: nonlocal
# outer: nonlocal


c = 1 # global variable
    
def add():
    c = c + 2 # increment c by 2
    print(c)

# add()

# UnboundLocalError: local variable 'c' referenced before assignment
# This is because we can only access the global variable but cannot modify it from inside the function.
# The solution for this is to use the global keyword.

def foo():
    x = 20

    def bar():
        global x
        x = 25
    
    print("Before calling bar: ", x)
    print("Calling bar now")
    bar()
    print("After calling bar: ", x)

foo()
print("x in main: ", x)
# Before and after calling bar(), the variable x takes the value of local variable i.e x = 20. Outside of the foo() function, 
# the variable x will take value defined in the bar() function i.e x = 25. This is because we have used global 
# keyword in x to create global variable inside the bar() function (local scope).


# While importing a module, Python looks at several places. Interpreter first looks for a built-in module.
# Then(if built-in module not found), Python looks into a list of directories defined in sys.path. The search is in this order.

# The current directory.
# PYTHONPATH (an environment variable with a list of directories).
# The installation-dependent default directory.

# Reload module
# >>> import imp
# >>> import my_module
# This code got executed
# >>> import my_module
# >>> imp.reload(my_module)
# This code got executed
# <module 'my_module' from '.\\my_module.py'>


# We can use the dir() function to find out names that are defined inside a module

dir()
# >>> dir(example)


# package collection of modules we place similar modules in one package and different modules in different packages.
# Python has packages for directories and modules for files

# A directory must contain a file named __init__.py in order for Python to consider it as a package.
# This file can be left empty but we generally place the initialization code for that package in this file.


# We can convert one type of number into another. This is also known as coercion.
# a floating-point number is accurate only up to 15 decimal places (the 16th place is inaccurate).


# >>> 1.1 + 2.2
# 3.3000000000000003

# It turns out that floating-point numbers are implemented in computer hardware as binary fractions as the computer only 
# understands binary (0 and 1). Due to this reason, most of the decimal fractions we know, cannot be accurately stored 
# in our computer.

# Let's take an example. We cannot represent the fraction 1/3 as a decimal number. This will give 0.33333333... 
# which is infinitely long, and we can only approximate it.

# It turns out that the decimal fraction 0.1 will result in an infinitely long binary fraction of 0.000110011001100110011... 
# and our computer only stores a finite number of it.

# This will only approximate 0.1 but never be equal. Hence, it is the limitation of our computer hardware and not an error 
# in Python.

import decimal

print(0.1)

print(decimal.Decimal(0.1))

from decimal import Decimal as D

print(D('1.1') + D('2.2'))

print(D('1.2') * D('2.50'))


# We might ask, why not implement Decimal every time, instead of float? The main reason is efficiency. 
# Floating point operations are carried out much faster than Decimal operations.


import fractions

print(fractions.Fraction(1.5))

print(fractions.Fraction(5))

print(fractions.Fraction(1,3))

# 3/2
# 5
# 1/3

import random

print(random.randrange(10, 20))

x = ['a', 'b', 'c', 'd', 'e']

# Get random choice
print(random.choice(x))

# Shuffle x
random.shuffle(x)

# Print the shuffled x
print(x)

# Print random element
print(random.random())

# When we slice lists, the start index is inclusive but the end index is exclusive. 
# For example, my_list[2: 5] returns a list with elements at index 2, 3 and 4, but not 5.

# A list comprehension consists of an expression followed by for statement inside square brackets.
pow2 = [2 ** x for x in range(10)]

pow2 = []
for x in range(10):
   pow2.append(2 ** x)

[x+y for x in ['Python ','C '] for y in ['Language','Programming']]


# Creating a tuple having one element
my_tuple = ("hello",)

# Changing tuple values
my_tuple = (4, 2, 3, [6, 5])

# However, item of mutable element can be changed
my_tuple[3][0] = 9    # Output: (4, 2, 3, [9, 5])
print(my_tuple)

# Strings are immutable
# my_string[1]  = 'r' error
# del my_string[1] error

# The enumerate() function returns an enumerate object. It contains the index and value of all the items in the string as pairs.
# This can be useful for iteration.

str = 'cold'

# enumerate()
list_enumerate = list(enumerate(str))
print('list(enumerate(str) = ', list_enumerate)

#character count
print('len(str) = ', len(str))

# a set cannot have mutable elements like lists, sets or dictionaries as its elements.

# Sets are mutable. However, since they are unordered, indexing has no meaning.
# Since set is an unordered data type, there is no way of determining which item will be popped. It is completely arbitrary.


my_dict = {'name': 'Jack', 'age': 26}
# Output None
print(my_dict.get('address'))

# KeyError
# print(my_dict['address'])

# Dictionary Methods
marks = {}.fromkeys(['Math', 'English', 'Science'], 0)
# {'Math': 0, 'English': 0, 'Science': 0}

# Files are named locations on disk to store related information.

# f = open("test.txt")    # open file in current directory
# f = open("C:/Python38/README.txt")  # specifying full path
# f = open("test.txt", mode='w', encoding='utf-8')   'cp1252' windows
# f.write("my first file\n")
# f.read() f.read(4)
# f.tell()    # get the current file position
# f.seek(0)   # bring file cursor to initial position
# print(f.read())  # read the entire file 
# f.close()
# for line in f:
#     print(line, end = '')
# the lines in the file itself include a newline character \n
# f.readline() 'This is my first file\n'
# f.readlines() a list of remaining lines of the entire file.
# we use the end parameter of the print() function to avoid two newlines when printing.


# r Opens a file for reading. (default)
# w Opens a file for writing. Creates a new file if it does not exist or truncates the file if it exists.
# x Opens a file for exclusive creation. If the file already exists, the operation fails.
# a Opens a file for appending at the end of the file without truncating it. Creates a new file if it does not exist.
# t Opens in text mode. (default)
# b Opens in binary mode.
# + Opens a file for updating (reading and writing)

# f = open("test.txt", mode='r', encoding='utf-8')   'cp1252' windows

# A safer way is to use a try...finally block.

# The best way to close a file is by using the with statement. This ensures that the file is closed when the block inside 
# the with statement is exited.
# with open("test.txt", encoding = 'utf-8') as f:
# We don't need to explicitly call the close() method. It is done internally.



import os
os.getcwd()  # 'C:\\Program Files\\PyScripter'
os.getcwdb() # b'C:\\Program Files\\PyScripter'

# The extra backslash implies an escape sequence. The print() function will render this properly.

print(os.getcwd())

# os.chdir('C:\\Python33')
os.listdir()
# os.listdir('G:\\')
# os.mkdir('test')
# os.rename('test','new_one')
# os.remove('old.txt') A file can be removed (deleted) using the remove()
# os.rmdir('new_one') the rmdir() method removes an empty directory. The rmdir() method can only remove empty directories.

# In order to remove a non-empty directory, we can use the rmtree() method inside the shutil module.
# import shutil
# shutil.rmtree('test')

print(dir(locals()['__builtins__']))

# For example, let us consider a program where we have a function A that calls function B, which in turn calls function C. 
# If an exception occurs in function C but is not handled in C, the exception passes to B and then to A.

# try:
#     print("The entry is", entry)
#     r = 1/int(entry)
#     break
# except:
#     print("Oops!", sys.exc_info()[0], "occurred.")  <class 'ZeroDivisionError'> <class 'ValueError'>

# we print the name of the exception using the exc_info() function inside sys module.
# every exception in Python inherits from the base Exception class,
# we can also perform the above task in the following way:
#except Exception as e:
#    print("Oops!", e.__class__, "occurred.")

# Catching Specific Exceptions in Python
# except ValueError:
# except (TypeError, ZeroDivisionError):

# We can also manually raise exceptions using the raise keyword.
# try:
#     a = int(input("Enter a positive integer: "))
#     if a <= 0:
#         raise ValueError("That is not a positive number!")
# except ValueError as ve:
#     print(ve)

# In some situations, you might want to run a certain block of code if the code block inside try ran without any errors. 
# For these cases, you can use the optional else keyword with the try statement.

# The try statement in Python can have an optional finally clause. This clause is executed no matter what, 
# and is generally used to release external resources.

# try:
#    f = open("test.txt",encoding = 'utf-8')
#    # perform file operations
# finally:
#    f.close()

# This type of construct makes sure that the file is closed even if an exception occurs during the program execution.


# User-defined exception class can implement everything a normal class can do, but we generally make them simple and concise.
# Most implementations declare a custom base class and derive others exception classes from this base class.
# This concept is made clearer in the following example.

# User-Defined Exception in Python
# define Python user-defined exceptions
class Error(Exception):
    """Base class for other exceptions"""
    pass


class ValueTooSmallError(Error):
    """Raised when the input value is too small"""
    pass


class ValueTooLargeError(Error):
    """Raised when the input value is too large"""
    pass


# you need to guess this number
number = 10

# user guesses a number until he/she gets it right
while True:
    try:
        i_num = int(input("Enter a number: "))
        if i_num < number:
            raise ValueTooSmallError
        elif i_num > number:
            raise ValueTooLargeError
        break
    except ValueTooSmallError:
        print("This value is too small, try again!")
        print()
    except ValueTooLargeError:
        print("This value is too large, try again!")
        print()

print("Congratulations! You guessed it correctly.")


class SalaryNotInRangeError(Exception):
    """Exception raised for errors in the input salary.

    Attributes:
        salary -- input salary which caused the error
        message -- explanation of the error
    """
    def __init__(self, salary, message="Salary is not in (5000, 15000) range"):
        self.salary = salary
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.salary} -> {self.message}'

salary = int(input("Enter salary amount: "))
if not 5000 < salary < 15000:
    raise SalaryNotInRangeError(salary)