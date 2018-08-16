import random
import re
import this

#BASIC CONCEPTS

#FIRST PROGRAM

#Print
print('hello jesus')

#SIMPLE OPERATIONS

#First level arithmetics
print(5+5)
print(8-4)
print(5*8)
print(8/4)

#Parentheses
print(8*(4-6))

#Negatives
print(-7)

#Zero division error
try:
	print(7/0)
except:
	print('zero div')

#FLOATS

#Floats
print(7.0)
print(8+7.0)
print(4/1)

#OTHER NUMERICAL OPERATIONS

#Second level arithmetics
print(8//3)
print(8**9)
print(67%5)

#STRINGS

#Make a string
print('boy')

#Escape a character 
print('new \n line')
print('escape \' quote')
print('use "alternate" quotes')

#Multi-line strings
print('''this 
	is
	a 
	multi
	line
	string ''')

#Raw strings
print(r'this is a raw string \c\docs\newfile')


#SIMPLE INPUT AND OUTPUT
#Input
i = input('please enter name:')
print(i)

#Input with escape

#STRING OPERATIONS
#Add two strings
print('jack and ' + 'jill')
o = 'john '
p = 'james'
print(o + p)

#Add string and non-string, causes typeerror
try:
	print('jack' + 8)
except:
	print('typeerror')

#Repeat string
print(o * 99)

#TYPE CONVERSION
#Convert between variety of types
a = 22
b = 4.0
print(float(a))
print(int(b))
print(str(a))
print(str(b))

#Take two inputs, convert to int, convert result float
a = int(input('please enter first number:'))
b = int(input('please enter second  number:'))
ans = float(a + b)
print(ans)

#VARIABLES
#Assign a value to a variable and print it out
p = 67
print(p)

#Simultaneously assign values to several variables
a,b,c = 6575, 46476, 'jesus'
print(a)
print(b)
print(c)

#Multiply two or more variables
q = 89
print(p * q)

#In succession, use same variable for two different types
o = 8
print(o)

o = 'jou'
print(o)

#Create a bad variable name, gives syntax error
#try:
	#8i = 89
	#print(8i)
#except:
	#print('syntax')

#Reference non-existent variable
try:
	print(ghg)
except:
	print('nameeror')

#Delete variable
del o

try:
	print(o)
except:
	print('nameeror')

#Take value of variable from user input

u = input('please enter a variable: ')
print(u)

#IN-PLACE OPERATORS

#In-place operator
u = 9
print(u)
u+=756
print(u)

#In-place operator to manipulate strings
u = 'mum'
print(u)
u+='and dad'
print(u)

#CONTROL STRUCTURES

#BOOLEANS AND COMPARISONS

#Boolean
u = False
print(u)
print(u == True)
print(u == False)

#Boolean by comparing values
print(9 == 8)
print(4/5 == 0.8)

#Print Boolean

#All comparison operators 
print(4<5)
print(4<=5)
print(4==5)
print(4>=5)
print(4>5)
print(4!=5)

#IF STATEMENTS

#If statement
if 4 < 5:
	print('halleluyah')

#Nested if statement
if 4 < 5:
	print('continue')
	if 3 < 4:
		print('continue')
		if 2 > 3:
			print('no')

#ELSE STATEMENTS

#If-else statement
if 2 > 3:
	print('abnormal')
else:
	print('normal')

#Chain of if-else statements
if 'f' == 'g':
	print('f == g')
else:
	if 2 > 3:
		print('yes')
	else:
		if 56 > 89:
			print('no')
		else:
			print('56 !>')

#If-elif-else statement
if 'f' == 'g':
	print('f == g')
elif 2 > 3:
	print('yes')
elif 56 > 89:
	print('no')
else:
	print('56 !> 89')

#BOOLEAN LOGIC

#All Boolean logical operators

#OPERATOR PRECEDENCE

#Write operation to illustrate operator precedence

#WHILE LOOPS

#While loop
i = 8

while i > -56:
	print('hooray')
	i -= 1

#Infinite while loop
#i = 8

#while i==8:
	#print('hooray')
	#i -= 1

#Infinite while loop
#while True:
	#print('hooray')
	#i -= 1

#Break statement
i = 8

while i < 899:
	print(i)
	i += 1 # BEST POSITION the increment can occur before the 'if..break' construction
	if i == 65:
		break

#Break statement
u = 90

while u > 0:
	print (u)
	if u == 57:
		break
	u -= 1 # the increment can occur after the 'if..break' construction


#Break statement #this achieves the same thing as the above
u = 90

while u > 0:
	print (u)
	u -= 1
	if u == 56:
		break
	

#Continue statement
u = 98

while u > -87:
	u -= 1 #the increment must occur before the 'if...continue' construction
	if u % 2 == 0:
		continue
	print(u) # the 'if..continue' construction above determines what is printed out here


#Continue statement
u = 98

while u > -87:
	u -= 1 #the increment must occur before the 'if...continue' construction
	print(u) # the 'if..continue' construction below has no effect on this statement
	if u % 2 == 0:
		continue


#continue statement
u = 87

while u>-87: #is u greater than -87?
	if u%2 ==0: #is u an even number?
		continue
	print(u)
	u -= 1 #When using the continue statement, this is the wrong position for increment/decrement. Increment/decrement must come before the 'if..continue' construction. In this position, the 'continue' instruction loops infinitely


#LISTS

#List
mylist = [1,2,3,4,5,3,3,4,5,3,5,5,4]
print(mylist)

#Print item from list
print(mylist[5])

#Empty list
emptlist = []

#Print empty list
print(emptlist)

#List containing list
nestlist = [[1,2,3], 4,5,6]
print(nestlist)

#Index out of bounds of a list
#print(nestlist[9])

#Index a string
mystring = 'jesus'
print(mystring[3])

#Index an integer
myint = 8976786788
try:
	print(myint[4])
except:
	print('typeerror')

#LIST OPERATIONS

#Reassign list index
mylist = [5,6,7,88,6,6,5,5,4,5,4,4]
print(mylist)
mylist[5] = 'jesus'
print(mylist)
mylist.insert(0, 'jesus')
print(mylist)

#Add two or more lists
list1 = [5,6,7,6,7,7]
list2 = [9,8,9,8,9,7,7,6]
print(list1 + list2)

#Replicate list
print(list1 * 8)

#Check if value is in list
print('jesus' in mylist)

#Check if value is not in list#
print('jesus' not in mylist)

#LIST FUNCTIONS

#Find length of list
print(len(mylist))

#Find largest value in list
print(max(list1))

#Find smallest value in list
print(min(list2))

#Find position of first occurrence of item in list
print(mylist.index('jesus'))

#Count quantity of an item in the list
print(mylist.count('jesus'))

#LIST METHODS

#Append item to list
mylist.append('joshua')
print(mylist)

#Insert item into list
mylist.insert(4, 'mar')

#Extend list with another list
h=[1,2,3,4,5,6]
print(h)
h.extend(h)
print(h)
e=[6,7,6,7,8,7,8,8]
h.extend(e)
print(h)

#Remove item from list, remove
print(mylist)
mylist.remove('mar')
print(mylist)

#Remove item from list, pop
mylist.pop(0)
print(mylist)

#Reverse order of list's items
mylist.reverse()
print(mylist)

#RANGE

#Range, a range is an iterable object
u = range(10)
print(u)
print(list(u))

#List using range function, one argument
u = range(10)
print(u)
print(list(u))

#List using range function, two arguments
u = range(10, 156)
print(u)
print(list(u))

#List using range function and interval argument
u = range(10, 234, 23)
print(u)
print(list(u))

#FOR LOOPS

#Iterating through a list using a while loop requires more code
mylist = [5,6,7,88,6,6,5,5,4,5,4,4]
p = 0
while p < (len(mylist)):
	print(mylist[p])
	p += 1	

#Iterating through a list using a for loop requires less code
h = ['g', 'g', 'hkhkh', 'rtrtr', 'd', 'ddd']
for i in h:
	print(i)

#Iterate through for loop using range function
for i in range(12, 455, 23):
	print(i)

#continue statement
for i in range(89):
	print(i)
	if i == 67:
		continue # this continues after printing the value of i specified in the if conditional

#continue statement
for i in range(89):
	if i == 67:
		continue
	print(i) # this continues wihtout printing the value of i specified in the if conditional



#break statement
for i in range(23):
	print (i)
	if i == 6:
		break # this breaks after using the value of i specified in the if conditional

#break statement
for i in range(23):
	if i == 6:
		break
	print (i) # this breaks without using the value of i specified in the if conditional


#for else
for item in range(2, 13): # this takes all the integers between 2 and 10
	if 13 % item == 0: # if this is true, then the item is a factor of 10
		print (item, 'is a factor of', 13)
		break

else:
	print(13, 'is a prime number')


for number in range (2, 40):
	for divisor in range (2, number):
		if number % divisor == 0:
			print(number, 'is equal to', number/divisor, '*' , divisor)
			break

		elif divisor == (number - 1):
			print(number, 'is a prime')

for number in range (2, 100):
	for divisor in range (2, number):
		if number % divisor == 0:
			print(number, 'is equal to', number/divisor, '*' , divisor)
			break

	else:
		print(number, 'is a prime')


#SIMPLE CALCULATOR

#Calculator
#while True:

i=0
while i<4:

	print('to add please type add')
	print('to multiply please type multiply')
	print('to subtract please type subtract')
	print('to divide please type divide')
	print('to exit please type quit')
	usrinput = input('enter selecton')
	i += 1

	if usrinput == 'add':

		a = int(input('enter first number'))
		b = int(input('enter second number'))
		print(a + b)

	elif usrinput == 'subtract':

		a = int(input('enter first number'))
		b = int(input('enter second number'))
		print(a - b)

	elif usrinput == 'multiply':

		a = int(input('enter first number'))
		b = int(input('enter second number'))
		print(a * b)

	elif usrinput == 'divide':

		a = int(input('enter dividend'))
		b = int(input('enter divisor'))
		print(a / b)

	elif usrinput == 'quit':

		break

#FUNCTIONS AND MODULES

#FUNCTIONS WITHOUT ARGUMENTS

#Functions without arguments
#parameters are the variables in a function definition, and arguments are the values put into parameters when functions are called.
def myfun():
	print(9**2)

myfun()

#FUNCTIONS WITH ARGUMENTS

#Functions with arguments
#parameters are the variables in a function definition, and arguments are the values put into parameters when functions are called.
def myfun(c): #c is the only parameter of the function
	return c**2

print(myfun(30)) #30 is the argument passed into the function

#RETURNING FROM FUNCTIONS

#Return values from functions
def myfun2(r):
	g = ((r ** 8)/45)*0.67
	return g

print(myfun2(1))

#COMMENTS AND DOCSTRINGS

#Comments
#this is a comment

#Docstrings
'''
a docstring explains the purpose of a function
below the function's first line
'''

#FUNCTIONS AS OBJECTS

#Reassignment of a function
def myfun4():
	p = 'jesus'
	return p
myfun5 = myfun4
print(myfun5())

#Functions as objects
def myfun3(a,b):
	return a(b)

def myfun6(a):
	return a**9

print(myfun3(myfun6, 2))

#MODULES

#Import modules
p = random.randint(3, 678)
print(p)

#From modules import submodules
import random
from math import sqrt as square_rt

#From modules import submodules as aliases
while True:

	h = random.randint(4, 234)
	i = square_rt(h)
	print('squar root of', h, 'is', i)
	if i<5:
		break

#From modules import submodules as aliases
import random
from math import sqrt as square_rt

#From modules import submodules as aliases
while True:

	h = random.randint(4, 234)
	i = square_rt(h)
	print('squar root of', h, 'is', i)
	if i<5:
		break

#STANDARD LIBRARY AND PIP

#Pip install library statement

#EXCEPTIONS AND FILES

#EXCEPTIONS

#Try/except statement
try:
	print(7/0)
except ZeroDivisionError:
	print('error')

#Try/except statement with multiple except blocks
try:
	print(7/0)
	print(a)
except ZeroDivisionError:
	print('error')
except NameError:
	print('name')

#Try/except statement with multiple exceptions per block
h = 'hello'
try:
	h[2] = 'y'
	print(h)
	print(7/0)
	print(a)
except (ZeroDivisionError, TypeError):
	print('tyerror')
except NameError:
	print('name')

#Try/except statement with no exception specified
try:
	print(8/0)
except:
	print('error')

#FINALLY

#Finally block with caught exceptions
try:
	print(7/0)
except ZeroDivisionError:
	print('error')
finally:
	print('why do we need a finally block?')

#Finally block with uncaught exceptions
try:
	print(a)
except ZeroDivisionError:
	print('error')
finally:
	print('why do we need a finally block?')


#RAISING EXCEPTIONS

#Raise exception
"""
h = 9
if h < 10:
	raise NameError
"""

#Raise exception inside try/except statement
try:
	raise Exception('na him')
except Exception as myex:
	print('caught', myex)

#Raise exception inside try/except statement
try:
	print(7/0)
except ZeroDivisionError:
	print('err')
	#raise TypeError

#Raise exception in if block
"""
if True:
	raise ZeroDivisionError
"""

#Raise exception with argument
#raise TypeError ('this argument belongs to the raise statement')

#Raise exception without arguments
#raise NameError

#ASSERTIONS

#Assertion without arguments
d = 10
assert d < 11

#Assertion with arguments
d = 10
#assert d < 1, 'not true'

#OPENING FILES

#Open file
file = open('tom.txt')

#Open file using (‘file.txt’, r)
file = open('tom.txt', 'r')

#Open file using (‘file.txt’, w)
file = open('tom.txt', 'w')

#Open file using (‘file.txt’, a)
file = open('tom.txt', 'a')

#Open file using (‘file.txt’, rb)
file = open('tom.txt', 'rb')

#Open file using (‘file.txt’, wb)
file = open('tom.txt', 'wb')

#Open file using (‘file.txt’, ab)
file = open('tom.txt', 'ab')

#Close file
file.close()

#READING FILES

#Open and read file
file = open('tom.txt', 'r')
text = file.read()

#Read only specific number of bytes from file
file = open('tom.txt', 'r', encoding='utf-8')
text = file.read(160)
print(text)
file.close()

#Read only specific number of lines from file each containing specific number of bytes
file = open('tom.txt', 'r', encoding='utf-8')

for i in range(5):
	print(file.read(32))

file.close()

#Find number of characters in file
file  = open('98-0.txt', 'r', encoding='utf-8')
text = file.read()
print(len(text))

#Turn file into a list of lines using readlines() 
file = open('tom.txt', 'r', encoding='utf-8')
mylist = file.readlines()
print(mylist)

#Print file one character at a time
fileobject  = open('tom.txt', 'r', encoding='utf-8')
text = fileobject.read()
for i in text:
	print(i)

#Print file one line at a time #ie print without reading
fileobject = open('tom.txt', 'r', encoding='utf-8')
for i in fileobject:
	print(i)

#WRITING FILES

#Write to file
file = open('tom.txt', 'a', encoding='utf-8')
file.write('hey!!! what\'s gwannning on people!!!!!')
file.close()

with open('tom.txt', 'r', encoding='utf-8') as file:
	print(file.read())

#Display number of bytes written to file
file = open('tom.txt', 'a', encoding='utf-8')
text = 'yippee!!!!!!!! jesus'
quantity = file.write(text)
file.close()
print(quantity)

with open('tom.txt', 'r', encoding ='utf-8') as file:
	print(file.read())

#WORKING WITH FILES

#try/finally can be used to close file but won't catch errors unless specified
try:
	file = open('tom.txt', 'r', encoding='utf-8')
	print(file.read(160))
finally:
	file.close()

#with statement will close file but won't catch errors
with open('tom.txt', 'r', encoding='utf-8') as file:
	print(file.read(320))

#with statement will close file, try/except will catch errors
try:
	with open('98-0', 'r', encoding='utf-8') as file:
		print(file.read(640))
except:
	print('error')

#MORE TYPES

#NONE

#Print(None == None)
print(None==None)

#Print empty line
print()

#Print a function that returns nothing
def func1():
	a=9+8

print(func1())

#DICTIONARIES

#Print and index dictionary key
mydict = {1:'jon', 2:'jef', 3:'jim', 4:'jes'}
print(mydict[1])

#Index incorrect dictionary key, catch error with try/except block
try:
	mydict = {1:'jon', 2:'jef', 3:'jim', 4:'jes'}
	print(mydict[8])
except:
	print('er')

#Print empty dictionary
mydict = {}
print(mydict)

#Dictionary with mutable key
try:
	mydict = {[3,4,5]:4, [1,2,3]:8}
except:
	print('no')

#Dictionary with repeated key
mydict = {1:4, 1:8}
print(mydict)

#Reassign dictionary key
mydict={1:'koi', 2:'ken', 3:'kav', 4:'kie'}
print(mydict)
mydict[1]='gbos'
print(mydict)

#Append new key/value pair to dictionary
mydict={1:'koi', 2:'ken', 3:'kav', 4:'kie'}
print(mydict)
mydict[8]='gbios'
print(mydict)

#DICTIONARY KEYWORDS AND METHODS

#find if a key is in or not in a dictionary
mydict={1:'koi', 2:'ken', 3:'kav', 4:'kie'}
print(1 in mydict)

#find if a key is in or not in a dictionary
mydict={1:'koi', 2:'ken', 3:'kav', 4:'kie'}
print(2 not in mydict)

#Dictionary get method
print(mydict[1])
try:
	print(mydict[8])
except:
	print('haba')
o = mydict.get(1)
print(o)
o = mydict.get(8)
print(o)

#Dictionary items method
mydict={1:'koi', 2:'ken', 3:'kav', 4:'kie'}
for i,j in mydict.items():
	print(i,j)

#Dictionary pop method
mydict={1:'koi', 2:'ken', 3:'kav', 4:'kie'}
mydict.pop(1)
print(mydict)

#Simultaneously pop and iterate through dictionary
mydict={1:'koi', 2:'ken', 3:'kav', 4:'kie'}
mylist = []
for i in mydict:
	mylist.append(i)
print(mylist)
for i in mylist:
	mydict.pop(i)
print(mydict)

#Enumerate dictionary keys
mydict={1:'koi', 2:'ken', 3:'kav', 89:'kie'}
for i in  enumerate(mydict):
	print(i)

#TUPLES

#Create tuple with parentheses
mytuple = (4,5,4,3,4,4,5,6,6)
print(mytuple)

#Create Tuple without parentheses
mytuple = 4,5,4,3,4,6,7,8,6,6
print(mytuple)

#Index a tuple
print(mytuple[6])

#Reassign tuple key
try:
	mytuple[5] = 67
except:
	print('er')

#Print empty tuple
mytuple = ()
print(mytuple)


#LIST SLICES

#List slicing
mylist = [3,4,4,5,6,7,5,5,6,6,5,4,5,6,7,6,5,5]
print(mylist[:6])

#List slicing featuring interval argument
print(mylist[:6:3])

#Reverse list slicing
print(mylist[-1:-7:-1])

#LIST COMPREHENSION

#List comprehension
mylist = [i for i in range(23)]
print(mylist)

#List comprehension featuring conditional statement
#List comprehension
mylist = [i for i in range(23) if i%3 == 0]
print(mylist)

#‘Out of memory’ list comprehension
"""
mylist = [i**100 for i in range(1000000,1000000000)]
print(mylist)
"""

#STRING FORMATTING

#format method, unnamed arguments
y = 'this is {0} {1}'
z = y.format('a', 'sentence')
print(z)

#format method, named arguments
u = 'what should {c} {d} {a}'
i = u.format(c = 'put', d= 'in', a='here')
print(i)

#STRING FUNCTIONS

#Join
u = '\n'.join(['water', 'is', 'good'])
print(u)

#Split
u = 'water is good'.split(' ')
print(u)

#Replace
y = 'this is bad'
u = y.replace('bad', 'good')
print(u)

#Startswith
o = 'this is good'
print(o.startswith('this'))

#Endswith
o = 'this is good'
print(o.endswith('this'))

#Upper
u = 'this is upper'
i = u.upper()
print(i)

#Lower 
u = 'LWER LOWER'
i = u.lower()
print(i)

#Title
name = 'oyega'
o = name.title()
print(o)

#Capwords
#Capitalise

#%s
name = 'Gboyega'
o = 'what is your %s' % name
print(o)

#%i
u = 9
print('my integer is %i' % u)

#%d
y = 9.0
print('my intege is %d' % y)

#%f
u = 9.7474747
print('int is %f' %u)

#%x
y = 200
print('my intege is %x' % y)

#%c
i = 45
print('ascii is %c' %i)

#NUMERIC FUNCTIONS

#Round
f=0.8484848484884
g = round(f, 3)
print(g)

#Min
u=[4,556,7,0,8,7,45,67]
print(min(u))

#Max
u=[4,556,7,0,8,7,45,67]
print(max(u))

#Abs
u=-7272626
print(abs(u))

#Sum
u=[4,556,7,0,8,7,45,67]
print(sum(u))

#LIST FUNCTIONS

#All
u = [9,8,7,6,7,8,6,6,8]
if all(i > 2 for i in u):
	print(True)
else:
	print(False)

#Any
mylist = [4,5,6,7,6,7,6,5,4]
print(mylist)
if any([i%5 == 0 for i in mylist]):
	print(True)
else:
	print(False)

#Enumerate
mylist = [4,5,6,7,6,7,6,5,4]
print(mylist)
for i in enumerate(mylist):
	print(i)

#TEXT ANALYSER

#Text analyser
filename = input('enter a filename ')

with open(filename, 'r', encoding='utf-8') as file:
	mytext = file.read()

def mycounter(text, character):
	count = 0
	for c in text:
		if c == character:
			count +=1
	return count

mytext = mytext.lower()

p = 0

for i in 'abcdefghijklmnopqrstuvwxyz':
	print(i, mycounter(mytext, i))
	p += mycounter(mytext, i)

print(p)
print(len(mytext))

#FUNCTIONAL PROGRAMMING

#INTRO

#Functions as objects
def addagain(f, var):
	return f(f(var))

def add(var2):
	return var2 + 5

print(addagain(add, 23))

#Lower order function
def add(var2):
	return var2 + 5

print(addagain(add, 23))

#Higher order function, takes other functions as arguments or returns them as results
def addagain(f, var):
	return f(f(var))

def add(var2):
	return var2 + 5

print(addagain(add, 23))

#Pure function
def puref(var):
	return var * 2

print(puref(7))

#Impure function
def puref(var):
	return var * 2

j = 9
print(puref(j))

j = 99
print(puref(j))

#memoization #A technique in which partial results are recorded (forming a memo) and then can be re-used later without having to recompute them.
def puref(var):
	return var * 2

a = puref(9)

print(a)

#LAMBDAS

#Named function 
def fun1(u):
	return u*8
print(fun1(76))

#Anonymous or Unnamed function
g = lambda v: v*9
print(g(78))

#Anonymous or Unnamed function
print((lambda p:p**8 + p*3 + 67)(5))

#Higher order function containing anonymous function
def fun1(r,a):
	return r(a)
print(fun1(lambda t: t**3, 5))

#Assign anonymous function to variable
h = lambda u: u**3
print(h(78))

#MAPS AND FILTERS

#Map function #The map function takes in a function and an iterable, applies the function to the iterable, and returns the result
mylist = [56,433,6,1,0,567,6]

def fun2(y):
	return y**6

print(list(map(fun2, mylist)))

#Map function using anonymous function
mylist = [56,433,6,1,0,567,6]
print(list(map(lambda k:k*7, mylist)))

#Filter function #The filter function takes in a function and an iterable and, from the iterable, retains only the items that match the predicate in the function
mylsit = [3,4,5,443,566,0,1,43]

print(list(filter(lambda b: b%3<1, mylsit)))

mynames = ['jak', 'jenny', 'jude', 'law']
print(list(filter(lambda i: len(i)>3, mynames)))

#GENERATORS #A generator contains a loop. The loop contains a yield statement #The 'yield' keyword does not destroy local variables but the 'return' keyword destroys local variables. #Generators generate values on demand, therefore incur lower memory usage #You have access to some of the values before all of the values are generated

#Iterate through a for generator
def mygen():
	for i in range(78):
		yield i

for i in mygen():
	print (i)

#Iterate through a while generator
def mygen():
	count = 0
	while count < 5:
		yield count
		count +=1

for i in mygen():
	print(i)

#Convert a for generator to a list
def mygen(u):
	for i in range(u):
		if i%2 == 0:
			yield(i)

print(list(mygen(78)))

#convert a while generator to a list
def mygen():
	g = 0
	while g<891:
		if g%3 == 0:
			yield g
		g+=1

print(list(mygen()))

#Infinite generator #A generator can be infinite because it doesnt have the memory restrictions of lists, which is because it yields one item at a time
def infinite():
	while True:
		yield(9)
"""
for i in infinite():
	print(i)
"""

#DECORATORS

#a decorator takes in your function as its argument and returns a wrap as its result

#create the function to be decorated
def my_function():
	print('hey boy!')

#define the decorator
#the decorator takes in your function as an argument
def decorator(a_function):

	#create your wrap and wrap what you like around your function
	def wrap():
		print('@@@@@@@@@@@@@@@@')
		a_function()
		print('@@@@@@@@@@@@@@@@')

	#return the wrap
	return wrap

#simply call the decorator, passing in your function
#decorated_function = decorator(my_function)
#decorated_function()

#OR
(decorator(my_function))()




#pre-pended decorator

#create decorator
def decorator(a_function):

	def wrap():
		print('@@@@@@@@@@@')
		a_function()
		print('@@@@@@@@@@@')

	return wrap

#pre-pend decorator to your function
@decorator	
def my_function():
	print('hallo!hallo!')

#call ur function anytime you want
#it will execute with the decorator implemented
my_function()




#RECURSION

#recursion is a function calling itself
#it is used to solve a problem that can be broken down into easier problems of the same type

#Recursion
def myrec(y):
	if y==1:
		return 100
	else:
		return y * myrec(y-1)

t = int(input('number: '))
print(myrec(t))

#Infinite recursion
def myrec(y):
	return y * myrec(y-1)

#print(myrec(8))

#Indirect recursion
def even(x):
	if x==0:
		return True
	else:
		return odd(x-1)

def odd(x):
	return not even(x)

e=int(input('num:'))
print(even(e))

#SETS

#Set, curly braces
myset = {1,2,2,3,4,5}
print(myset)

#Set, set function
myset=set([3,4,3,4,5,3,3,4,4,3,4,4,3,3])
print(myset)

#In set
print(6 in myset)
print(6 not in myset)

#len(set)
print(len(myset))

try:
	#Indexing a set yields an error
	myset=set([3,4,3,4,5,3,3,4,4,3,4,4,3,3])
	print(myset)
	print(myset[0])
except:
	print('u')

#Set.add
myset = set([3,4,5,6,7])
print(myset)
myset.add(56)
print(myset)

#Set.remove
myset = set([3,4,5,6,7])
print(myset)
myset.add(56)
print(myset)
myset.remove(56)
print(myset)

#Set.pop
myset = set([3,4,5,6,7])
print(myset)
myset.add(56)
print(myset)

mylis = []
for i in myset:
	mylis.append(i)

print(mylis)

for i in mylis:
	myset.pop()
	print(myset)

#Union
myset = {4,5,6,7,8}
myset2 = {8,9,0,1,2}
print(myset | myset2)

#Intersection
myset={2,3,4,5,6}
myset1={1,2,3,4,5,6,7,8}
print(myset & myset1)

#Symmetric difference #opposite of intersection
myset = {1,2,3,4,5,6}
myset1={4,5,6,7,8,9}
print(myset1 ^ myset)

#Difference
myset = {1,2,3,4,5,6}
myset1={4,5,6,7,8,9}
print(myset1 - myset)
print(myset - myset1)

#Advantages of data structures

#dictionary: fast lookup, custom key
#list: easy
#tuple: immutable
#set: no duplicates

#ITERTOOLS

#Count
from itertools import count 

for i in count(5):
	print(i)
	if i >=761:
		break

#Takewhile
#Accumulate
#Chain
#Permutations, product

#OBJECT ORIENTED PROGRAMMING

#CLASSES 
#A CLASS CONTAINS ATTRIBUTES AND METHODS

class Animal():

	age = '15years'

	def __init__(self, name, diet, cover):
		self.name = name
		self.diet = diet
		self.cover = cover


	def sound(self):
		return 'bark'


dog = Animal('dog', 'meat', 'fur')
print(dog.name + '\'s diet is ' + dog.diet)
print(dog.name + ' is covered with ' + dog.cover)
dog.sound()
print(dog.name + '\'s age is ' + dog.age)

print(Animal.age)



class Dog(Animal):

	def bark(self):
		return 'yelp!'


	def sound(self):
		return 'grr'



dalma = Dog('dalma', 'bone', 'skin')
print(dalma.name + '\'s diet is ' + dalma.diet)
print(dalma.name + ' is covered with ' + dalma.cover)




class Mongrel(Dog):
	
	def sound(self):
		return super().sound()


moimoi = Mongrel('moimoi','yam', 'beads')
print(moimoi.name + '\'s diet is ' + moimoi.diet)
print(moimoi.name + ' is covered with ' + moimoi.cover)
print(moimoi.name + ' makes a ' + moimoi.sound() + 'ing sound')





#Create a class containing a constructor
#In the constructor set the initial value of the instance objects of the class's objects
class Animal():

	def __init__(self, category, sound, food, habitat):
		self.name = category
		self.sound = sound
		self.food = food
		self.habitat = habitat

	#Create methods other than the __init__ method
	def bodyfluid(self):
		print('blood')

	#Use self.attribute in one of your methods
	def foodstate(self):
		print('my diet is ' + self.food)



#Create objects of the class using the class name as a function
tilapia = Animal('fish', 'gurgle', 'mites', 'aquatic')


#using the type method verify the type of the object 
print(type(tilapia))


#using the objects created, access the object attributes and object method
print()
print(tilapia.name)
print(tilapia.sound)
print(tilapia.food)
print(tilapia.habitat)
tilapia.foodstate()


lion = Animal('mammal', 'roar', 'meat', 'terrestrial')

print()
print(lion.name)
print(lion.sound)
print(lion.food)
print(lion.habitat)


monkey = Animal('mammal', 'scream', 'banana', 'trees')

print()
print(monkey.name)
print(monkey.sound)
print(monkey.food)
print(monkey.habitat)


ant = Animal('insect', 'unknown', 'leaves', 'soil')

print()
print(ant.name)
print(ant.sound)
print(ant.food)
print(ant.habitat)
ant.bodyfluid()



#Create a class containing a class attribute, this can be called both from the class itself and from an object of the class
class Human():

	headcount = 1

	def __init__(self, gender, food):
		self.gender = gender
		self.food = food


tim = Human('male', 'vegan')
esther = Human('female', 'poultry')


#Access the class attribute from the class itself and from an instance of the class
print(tim.gender)
print(Human.headcount)
print(tim.headcount)


#Cause an AttributeError by trying to access an undefined attribute or undefined method

#From the instances created, access the instance attributes and instance method
try: 
	print()
	print(tilapia.name)
	print(tilapia.sound)
	print(tilapia.food)
	print(tilapia.habitat)
	tilapia.foodstat()
except:
	print('er')



#Create a superclass and two subclasses
class Human():

	def __init__(self, arms, legs, head):
		self.arms = arms
		self.legs = legs
		self.head = head

class Man(Human):
	def womb(self):
		print('none')

class Woman(Human):
	def womb(self):
		print('one')

jane = Woman(2,2,1)
bob = Man(2,2,1)

print(jane.arms)
print(bob.legs)
bob.womb()
jane.womb()
print(jane.head)

#Illustrate overriding of attributes and methods
class Human():

	def __init__(self, arms, legs, head):
		self.arms = arms
		self.legs = legs
		self.head = head

	def sound(self):
		print('talk')

class Man(Human):
	def womb(self):
		print('none')

	def sound(self):
		print('bellow')

class Woman(Human):
	def womb(self):
		print('one')


jane = Woman(2,2,1)
bob = Man(2,2,1)

jane.sound()
bob.sound()

#Illustrate indirect inheritance
class Milk():

	def __init__(self, taste, colour):
		self.taste = taste
		self.colour = colour

	def first(self):
		print('first')

class Whole(Milk):
	def second(self):
		print('second')

class Skim(Whole):
	def thied(self):
		print('thied')


tescomilk = Skim('nice', 'white')
tescomilk.first()
tescomilk.second()
tescomilk.thied()

#Illustrate the super() function
#EXAMPLE 1
class Boy():

	def __init__(self, nation):
		self.nation = nation

	def shoes(self):
		print('brown')

class LagosBoy(Boy):

	def shoes(self):
		print('black')
		super().shoes()

	def shoes2(self):
		super().shoes()

joe = LagosBoy('nigeria')
joe.shoes2()
joe.shoes()

#EXAMPLE 2
class Animal():

	def __init__(self, name, sound):
		self.name = name
		self.sound = sound

	def color(self):
		return 'brown'

dog = Animal('gbosko', 'ye!')

print(dog.name)
print(dog.sound)
print(dog.color())

#inheritance
class Dog(Animal):

	def color(self):
		return 'blue'

mongrel = Dog('ijapa', 'ok nau!')

print(mongrel.color())

#inheritance
class Aja(Dog):

	def color(self):
		return super().color()


ajami = Aja('okunkun', 'mummy!')

print(ajami.color())


#Magic methods, operator overloading 
#if you try to manipulate instances of a class using an operator, Python goes into the class and invokes the magic method corresponding to that operator

#Magic Method Example 1
class Vector():

	def __init__(self, x, y):
		self.x = x
		self.y = y

	#Define your magic method and define what happens when it is invoked
	def __add__(self, other):
		return Vector(self.x * other.x, self.y * other.y)
		#we put the name of the superclass before the parentheses above to convert the result to an instance of the superclass
		#otherwise, the result is merely a tuple, and it can't access any of the attributes x or y

#Create instances of your class
first  = Vector(5, 89)
second = Vector(-45464, 0)

#Manipulate them using the operator that corresponds to the magic method
result = first + second

#Print the results
print(result.x)
print(result.y)

#Magic Method Example 2
class Message():

	def __init__(self, title, body):
		self.title = title
		self.body = body

	def __sub__(self, other):

		deco = '*' * len(other.body)
		return '\n'.join([self.title, deco, other.body])

mess1 = Message('morning', 'good morning')
mess2 = Message('eveing', 'good morning again!')
print(mess1 - mess2)
print(mess2 - mess1)

#Magic Method Example 3
class ClassName(object):
	"""docstring for ClassName"""
	def __init__(self, arg):
		super(ClassName, self).__init__()
		self.message = arg

	def __add__(self, other):

		return '\n'.join([self.message, other.message])

mes1 = ClassName('hi')
mes2 = ClassName('hiiii')
print(mes2 + mes1)

#Magic Method Example 4
class Message():

	def __init__(self, message):

		self.message = message

	def __ge__(self, other):

		for i in range(len(self.message) + 1):
			res = (self.message)[i:] + '>' + other.message
			res += '>' + (self.message)[:i] 
			#return res #you must NEVER use return in a loop, because the loop terminates after encountering return
			print (res)

mes1 = Message('tomatoes')
mes2 = Message('pepperoni')
print(mes1 >= mes2)

#Magic Method Example 5
class Message():

	def __init__(self, lines):
		self.lines = lines

	def __add__(self, other):

		for i in range(len(self.lines) + 1):
			res = self.lines[i:] + '>' + other.lines
			res += '>' + self.lines[:i]
			print(res)

mes1 = Message('maccaronipeperoni')
mes2 = Message('pizza')

mes1 + mes2

#Magic Method Example 6
class ClassName(object):
	"""docstring for ClassName"""

	def __init__(self, mylist):
		super(ClassName, self).__init__()
		self.list = mylist
		
	def __getitem__(self, index):
		return self.list[index + random.randint(-2, -1)]

	def __len__(self):
		return random.randint(0, len(self.list)**8)

list1 = ClassName([1,2,3,4,5,6,7,8,9,0])

print(list1[4])
print(len(list1))

#Magic Method Example 7
class MyLists():

 	def __init__(self, mylist):
 		self.mylist = mylist

 	def __getitem__(self, index):
 		return self.mylist[index]

 	def __setitem__(self, index, item):
 		self.mylist[index] = item

list1 = MyLists(['a', 'f', 'gh', 're', 'ruyriury'])
for i in enumerate(list1):
	print(i)

list1[3] = 'jodash'

print(list1[3])
for i in enumerate(list1):
	print(i)

#OBJECT LIFECYCLE #to reduce the reference count of an object, do any of the following
#delete the object
#reassign its reference
#take its reference out of scope

#DATA HIDING
#private method
#special method
#weakly private method
class ClassName(object):
	"""docstring for ClassName"""

	def __init__(self, arg):
		super(ClassName, self).__init__()
		self.arg = arg
	
	def _sound(self):
		print('bark')

dog = ClassName(23)

dog._sound()

#strongly private method
class Mister():

	def __init__(self, age):
		self.age = age

	def __secret(self):
		print('shhhh!')

boy = Mister(89)

print(boy.age)

try:
	boy.__secret()
except:
	print('no')

boy._Mister__secret()

#name mangling



#CLASS AND STATIC METHODS

#CLASS METHODS, used for creating instances of the class (METHOD DEFINITION TAKES IN THE 'CLS' CONTEXT PARAMETER)

#STATIC METHODS, for creating methods that can be called both by the class and also by the instance, (METHOD DEFINITION DOES NOT TAKE IN ANY CONTEXT PARAMETERS)


#CLASS METHOD

#(CREATED USING THE @CLASSMETHOD DECORATOR)

#class method eg 1
class Animal():

	def __init__(self, sound, diet):
		self.sound = sound
		self.diet = diet
	
	def bmi(self):
		print(self.diet/self.sound)

	@classmethod
	def newanimal(cls, height, weight):
		return cls(height, weight) 
		#1. WHEN RETURNING THE CLS YOU MUST RETURN THE SAME NO. OF PARAMETERS AS ARE CONTAINED IN THE CONSTRUCTOR
		#2. THE ARGUMENT(S) YOU PASS IN WHEN CALLING YOUR CLASS METHOD WILL BE RETURNED ANYTIME YOU TRY TO ACCESS THE PARAMETERS IN THE CONSRUCTOR ABOVE

dog = Animal.newanimal(45, 97897)

print(dog.sound)
dog.bmi()

#class method eg 2
class Mountain():

	def __init__(self, height, base):
		self.height = height
		self.base = base

	def volume(self):
		print(self.height * self.base / 3)

	@classmethod
	def newmount(cls, length, breadth):
		return cls(length, length) 
		#1. WHEN RETURNING THE CLS YOU MUST RETURN THE SAME NO. OF PARAMETERS AS ARE CONTAINED IN THE CONSTRUCTOR
		#2. THE ARGUMENT(S) YOU PASS IN WHEN CALLING YOUR CLASS METHOD WILL BE RETURNED ANYTIME YOU TRY TO ACCESS THE PARAMETERS IN THE CONSRUCTOR ABOVE

acapulco = Mountain(4000, 3000)

print(acapulco.height)
acapulco.volume()

kili = Mountain.newmount(400, 3000)

print(kili.height)
kili.volume()

#class method  eg 3
class Mountain():

	def __init__(self, height, base):
		self.height = height
		self.base = base

	def volume(self):
		print(self.height * self.base / 3)

	@classmethod
	def newmount(cls, width):
		return cls(width, width) 
		#1. WHEN RETURNING THE CLS YOU MUST RETURN THE SAME NO. OF PARAMETERS AS ARE CONTAINED IN THE CONSTRUCTOR
		#2. THE ARGUMENT(S) YOU PASS IN WHEN CALLING YOUR CLASS METHOD WILL BE RETURNED ANYTIME YOU TRY TO ACCESS THE PARAMETERS IN THE CONSRUCTOR ABOVE

ever = Mountain(4666, 900)
ever.volume()

flora = Mountain.newmount(3000)
flora.volume()

Mountain.volume(flora)






#STATIC METHODS, for creating methods that can be called both by the class and also by the instance

#(CREATED USING THE @STATICMETHOD DECORATOR)

#METHOD DEFINITION DOES NOT TAKE IN ANY CONTEXT PARAMETERS

#static method eg 1
class Food():

	def __init__(self, dressing):
		self.dressing = dressing

	@staticmethod
	def toplist(topping):
		print('the topping is ' + topping)

pizza = Food('fish')

print(pizza.dressing)

pizza.toplist('salami')

Food.toplist('salami')

#static method eg 2
class Food():

	def __init__(self, topping):
		self.topping = topping

	@staticmethod
	def check_topping(toplist):
		if toplist=='bacon':
			raise ValueError('no bacon')
		else:
			return True

ingredients=[]

for i in range(3):
	y = input('enter ingredient ' + str(i+1) + ' please, maximum of 3 ingredients')
	ingredients.append(y)

if all(Food.check_topping(item) for item in ingredients):
	pizza = Food(ingredients)

n = ', '.join(ingredients)

print('your pizza consists of %s' % n)
print('your pizza consists of ' + n)

#static method eg 3
class Soup():

	def __init__(self, name):
		self.name = name

	@staticmethod
	def check_content(content):
		if content=='iru':
			raise ValueError('no iru!')
		else:
			return True

ingredients=[]

u = int(input('how many ingredients do you want to enter? '))

for i in range (u):
	y = input('enter ingredient number ' + str(i+1) + ' please, maximum of ' +str(u)+ ' ingredients')
	ingredients.append(y)

if all(Soup.check_content(item) for item in ingredients):
	mysoup = Soup(ingredients)

print('your soup contains ' + (', '.join(ingredients)))


#"static method" eg 4

#THIS IS ACTUALLY NOT A STATIC METHOD, but here a class calls a non-static method

#all you need do is include the name of a class object as an argument when the class calls the method

class Food():

	def __init__(self, dressing):
		self.dressing = dressing

	def toplist(self, topping):
		print('the topping is ' + topping)

pizza = Food('fish')
print(pizza.dressing)

pizza.toplist('salami')

Food.toplist(pizza, 'salami')



#PROPERTIES


#A PROPERTY IS SIMPLY AN ATTRIBUTE THAT IS DEFINED LIKE A METHOD


#THE METHOD IS CALLED THE GETTER BECAUSE IT GETS YOU THE VALUE OF THE PROPERTY


#THE GETTER DEFINITION IS PROTECTED USING THE @PROPERTY DECORATOR



#properties allow you to do two things:

#1. call a method the way you would call an instance attribute
#2. customize/restrict access to the method


#PROPERTY WITHOUT SETTER FACILITY
class Animal():

	def __init__(self, color, age):
		self.color = color #instance attribute
		self.age = age #instance attribute


	@property #quite simply speaking, a property is an instance attribute that is protected (read only, you can't modify it except you have a setter to do so)
	def name(self): 	#THIS IS THE GETTER. THE GETTER GETS CALLED WHEN YOU CALL THE ATTRIBUTE

						#THIS GETTER IS SIMPLY ANOTHER INSTANCE ATTRIBUTE 'name' BUT IT IS DEFINED LIKE A METHOD
		

		return 'olu'  	#HERE IS WHERE THE GETTER GETS YOU THE VALUE OF THE ATTRIBUTE


dog  = Animal('red', 67)

print(dog.name) 	#always remember to call your property like you would an attribute
					#THE GETTER GETS CALLED WHEN YOU CALL THE ATTRIBUTE

dog.age = 788

print(dog.age)





#PROPERTY WITHOUT SETTER FACILITY
class Monkey():

	def __init__(self, sound):
		self.sound = sound
	
	@property
	def color(self): #THIS IS THE GETTER. THE GETTER GETS CALLED WHEN YOU CALL THE ATTRIBUTE
		return 'blue' 

		#WHEN A SETTER IS NOT USED 
		#1. YOU DON'T ASSIGN AN INITIAL VALUE TO THE PROPERTY
		#2. INSTEAD THE GETTER  RETURNS A LITERAL VALUE


koala = Monkey('yelp')

print(koala.sound)
koala.sound = 'chuckle' #YOU CAN ASSIGN A NEW VALUE TO AN ORDINARY ATTRIBUTE
print(koala.sound)


print(koala.color) #THE GETTER GETS CALLED WHEN YOU CALL THE ATTRIBUTE


try:
	koala.color = 'red' #EXCEPT YOU USE A SETTER, YOU CAN'T ASSIGN A NEW VALUE TO A PROPERTY
except:
	print('no')
finally:
	print(koala.color)





#PROPERTY WITH SETTER FACILITY 

class Cabinet():
    def __init__(self, color):
        self.color = color
        self._material = 'wood' #THIS IS THE INITIAL VALUE OF THE PROPERTY

        #1. WHEN A SETTER IS USED, YOU ASSIGN AN INITIAL VALUE TO THE PROPERTY
        #2. HERE FOR EXAMPLE, THE ASSIGNMENT OF THE PROPERTY'S INITIAL VALUE TAKES PLACE IN THE CONSTRUCTOR
        #3. THE PROPERTY IS WRITTEN AS A WEAKLY PRIVATE ATTRIBUTE EVERY TIME IT IS WRITTEN IN THE CONSRUCTOR, THE GETTER OR THE SETTER

    


    @property
    def material(self): #THIS IS THE GETTER. THE GETTER GETS CALLED WHEN YOU CALL THE ATTRIBUTE
        
        return self._material #WHEN A SETTER IS USED THE GETTER MUST RETURN THE PROPERTY ITSELF (AND NOT RETURN A LITERAL VALUE)

    


    #THE SETTER DIRECTLY ASSIGNS A VALUE TO THE PROPERTY, OR IT ASSIGNS A VALUE TO A VARIABLE THAT DETERMINES THE VALUE OF THE PROPERTY
    
    @material.setter
    def material(self, value): #THIS IS THE SETTER. THE SETTER GETS CALLED WHEN YOU TRY TO ASSIGN A VALUE TO A VARIABLE WITHIN THE SETTER METHOD
        
        password = input('enter password (password is kombo): ')
        
        if password=='kombo':
            self._material = value #HERE THE SETTER DIRECTLY ASSIGNS A VALUE TO THE PROPERTY
        
        else:
            raise ValueError('tiff!')



mycab = Cabinet('green')
print(mycab.material)
mycab.material = 'stone'
print(mycab.material)








#A SIMPLE GAME
class Football():

	class_name=''
	description='' 
	objects={}



	def __init__(self, name):
		self.name = name
		Football.objects[self.class_name] = self


	def get_description(self):
		print(self.class_name + '\n' + self.description)




class Striker(Football):

	class_name = 'striker'
	description='scores goals'




class Defender(Football):

	class_name='defender'
	description='stops striker'




class Ball(Football):

	def __init__(self, name):
		self.class_name='ball'
		self._description='hollow spherical inflated with air' #THIS IS THE INITIAL VALUE OF THE PROPERTY
		self.status=0
		super().__init__(name) 	#THIS LINE GOES TO THE CONSTRUCTOR OF THE SUPER CLASS AND DOES TWO THINGS
								#1.	ball1.name = addidas
								#2. Football.objects[ball1.class_name] = ball1

		
		#1. WHEN A SETTER IS USED, YOU MUST ASSIGN AN INITIAL VALUE TO THE PROPERTY
       	#2. HERE FOR EXAMPLE, THE ASSIGNMENT OF THE PROPERTY'S INITIAL VALUE TAKES PLACE IN THE CONSTRUCTOR
        #3. THE PROPERTY IS WRITTEN AS A WEAKLY PRIVATE ATTRIBUTE EVERY TIME IT IS WRITTEN IN THE CONSRUCTOR, THE GETTER OR THE SETTER



	@property
	def description(self): #THIS IS THE GETTER. THE GETTER GETS CALLED WHEN YOU CALL THE PROPERTY

		if self.status==0:
			self._description='hollow spherical inflated with air'
	
		elif self.status==1:
			self._description = 'you beat one defender!'
	
		elif self.status==2:
			self._description = 'you beat another defender!'
	
		elif self.status==3:
			self._description = 'now you beat the goalkeeper!'
	
		elif self.status>3:
			self._description = 'IT\'S IN THE BACK OF THE NET!!!!!! GOALLLLLLLLLLLLLLLLLLLL!!!!!!!!!!!!!!!'
	
		return self._description #WHEN A SETTER IS USED THE GETTER MUST RETURN THE PROPERTY ITSELF (AND NOT RETURN A LITERAL VALUE)

    


    #THE SETTER ASSIGNS A VALUE TO THE PROPERTY, OR IT ASSIGNS A VALUE TO A VARIABLE THAT DETERMINES THE VALUE OF THE PROPERTY
	
	@description.setter 
	def description(self, value): #THIS IS THE SETTER. THE SETTER GETS CALLED WHEN YOU TRY TO ASSIGN A VALUE TO A VARIABLE WITHIN THE SETTER METHOD

		self.status = value 

		#HERE THE SETTER ASSIGNS A VALUE TO A VARIABLE THAT DETERMINES THE VALUE OF THE PROPERTY
	



striker1 = Striker('yekini')
defender1=Defender('uche')
ball1=Ball('addidas')



i=0


def get_input():

	global i

	i += 1

	command = (input('enter command: ')).split(' ')

	verbword = command[0]

	if verbword in verbdict:
		verb = verbdict[verbword]
	else:
		print('unknown')
		return

	if len(command)>1:
		nounword = command[1]
		verb(nounword)
	else:
		verb('nothing')



def say(noun):
	
	print('you said {}'.format(noun))



def examine(noun):
	
	if noun in Football.objects:
		Football.objects[noun].get_description()
	
	else:
		print('there is no {} here'.format(noun))



def kick(noun):

	if noun in Football.objects:
		
		#go to the dictionary in the Football class
		#get the object that corresponds to the noun you kicked
		#assign the object to the word 'item'
		item = Football.objects[noun]


		if type(item) == Ball:

			item.status = item.status + 1 #THIS IS WHERE THE SETTER IS CALLED, BECAUSE YOU TRY TO ASSIGN A NEW VALUE TO ITEM.STATUS
			
			if item.status == 1:
				print('you kicked the ball!')
			
			if 2<= item.status <=3:
				print('you kicked the ball again!')
			
			elif item.status>3:
				print('YOU\'VE SCORED!!!!!!!!!!!')

		else:
			print('you can\'t kick that')

	else:
		print('you can\'t kick that')


verbdict={'say':say, 'examine':examine, 'kick':kick}


while True:
#while i<10:

	get_input()




#SIMPLE GAME 2
class Vehicle():

	vehicles={}



	#constructor
	def __init__(self, kind, speed, material, substance): #MATERIAL WILL NOT BE ASSIGNED WHEN AN OBJECT IS CREATED
		self.kind = kind
		self.speed = speed
		self.material = material #BECAUSE A GETTER AND A SETTER ALREADY HAVE THIS NAME, THIS ASSIGNMENT WILL BE IGNORED
		self.substance = substance
		self.status=0
		self._integrity = 'intact' #INITIAL VALUE OF THE PROPERTY
		Vehicle.vehicles[self.kind] = self




	#getter
	@property
	def material(self): #THE GETTER AND SETTER NEED NOT HAVE THE SAME NAME AS THE PROPERTY
		if self.status==0:
			self._integrity='intact'
		
		elif self.status==1:
			self._integrity='integrity 75%'

		elif self.status==2:
			self._integrity='integrity 50%'

		elif self.status==3:
			self._integrity='integrity 25%'

		elif self.status==4:
			self._integrity='compromised'

		return self._integrity



	#setter
	@material.setter
	def material(self, value): #THE GETTER AND SETTER NEED NOT HAVE THE SAME NAME AS THE PROPERTY

		self.status = value #THE SETTER IS CALLED AT ANY POINT IN THIS CODE WHERE YOU TRY TO ASSIGN A VALUE TO SELF.STATUS

		return 'test' #setter won't return this
		print('test') #setter won't print this


car1 = Vehicle('sports', 600, 'steel', 'tin') #STEEL IS NOT ASSIGNED TO MATERIAL, NEVERTHELESS 4 ARGUMENTS ARE MANDATORY HERE


print(car1.kind)
print(car1.speed)
print(car1.material) #RATHER THAN CALL THE MATERIAL ATTRIBUTE, THIS WILL CALL THE MAETRIAL PROPERTY
print(car1.substance)



def crash(item):

	item.status += 1 #THIS ATTEMPTS TO ASSIGN A VALUE TO A VARIABLE IN THE SETTER, AND THEREFORE CALLS THE SETTER

	print(car1.material)



def getinput():

	command = (input('enter command:')).split(' ')

	if command[0] == 'crash':

		commandment=verbdict[command[0]]

		noun = command[1]

		myarg = Vehicle.vehicles[noun]

		#command[0](myarg) #WRONG. COMMAND[0] IS A STRING. A STRING ISN'T CALLABLE

		commandment(myarg)




verbdict={'crash':crash}


while True:
	getinput()

	



#FOOD FOR THOUGHT 1. CAN A CLASS ACCESS EVERY ATTRIBUTE AND METHOD THAT AN INSTANCE CAN? NO.

class Car():

	size = 'large'

	def __init__(self, speed, color):
		self.speed = speed

	def sound(self):
		return 'vroom'

	@property
	def expiry(self):
		return 23052020

ijapa = Car(45, 'red')

print(ijapa.size)
print(ijapa.speed)
print(ijapa.sound())
print(ijapa.expiry)

print(Car.size)
#print(Car.speed(ijapa)) #error, class can't access instance attributes under any circumstances
print(Car.sound(ijapa))
#print(Car.expiry()) #error, a property object is not callable

print(Car.expiry) #this will tell you there is a property object at a specified location in memory




#FOOD FOR THOUGHT 2. CAN AN INSTANCE ACCESS EVERY ATTRIBUTE AND METHOD THAT A CLASS CAN? YES.

class Dog():

	color = 'blue'

	def __init__(self, name, age):
		pass
		self.name = name
		self.age = age

	@staticmethod
	def sound():
		return 'bark'

	@classmethod
	def newdog(cls, size):
		return cls(size, size)


dog = Dog('ajami', 67)
print(dog.age)
print(dog.name)



print(Dog.color) #A CLASS CAN ACCESS A CLASS ATTRIBUTE
print(dog.color) #YES, AN INSTANCE TOO CAN ACCESS A CLASS ATTRIBUTE



print(Dog.sound()) #A CLASS CAN ACCESS A STATIC METHOD
print(dog.sound()) #YES, AN INSTANCE TOO CAN ACCESS A STATIC METHOD



aja = Dog.newdog(900) #A CLASS CAN ACCESS A CLASS METHOD
print(aja.sound())
print(aja.color)
print(aja.age)
print(aja.name)



ojuju = dog.newdog(8700) #YES, AN INSTANCE TOO CAN ACCESS A CLASS METHOD
print(ojuju.sound())
print(ojuju.color)
print(ojuju.age)
print(ojuju.name)







#REGULAR EXPRESSIONS

#REGULAR EXPRESSIONS
#re.match
pattern = r'onimole'

if re.match(pattern, 'onimolefamily we are here'):
	print('ye')
else:
	print('ha')

#re.search
pattern = r'onimole'

if re.search(pattern, 'oiuafioud onimolefamily we are here'):
	print('ye')
else:
	print('ha')

#re.findall
pattern = 'gbosko'

print(re.findall(pattern, 'lkjalsdfkjgboskolkjsfldsl;gbosko;lakf;ldgboskol;a;kf;ldkgboskolkjl'))

print(re.findall('gbosko', 'lkjalsdfkjgbokolkjsfldsl;gbosko;lakf;ldgboskol;a;kf;ldkgboskolkjl'))

#re.finditer
pattern = r'jobijobi'

for i in re.finditer(pattern, 'kljkljjobijobikljkljkljobijobijkljkljjobijobi'):
	print (i)

#re.search().group()
#re.search().start()
#re.search().end()
#re.search().span()

pattern = r'pastor'

match = re.search(pattern, 'pastorpasturepastorpasturepastorpasturepastorpasturepastorpasture')

if match:

	print(match.group())
	print(match.start())
	print(match.end())
	print(match.span())

#re.sub
string = 'hi ljkljklj! whats up!'
pattern = 'ljkljklj'
newstr = re.sub(pattern, 'ueyeuei', string, 0)
print(newstr)

#re.sub
string = 'davidlkjlkjwaslkjlkjanlkjlkjexcellentlkjlkjking!lkjlkj'
patter = 'lkjlkj'
print(re.sub(patter, ' ', string))
new = re.sub(patter, ' ', string, 2)
print(new)

#re.sub
def re_search_replace():

	phrase_list=[
	'hi <name>!',
	'my name is <name>!'
	]

	persons_dict={
	0:'Ben',
	1:'Sue'
	}

	name_pattern=r'<name>'

	for item in phrase_list:
		item_id = phrase_list.index(item)
		new_str = re.sub(name_pattern, persons_dict[item_id], item)
		print(new_str)

re_search_replace()

#SIMPLE METACHARACTERS
#.metacharacter
#^metacharacter
#$metacharacter

pattern = r'^gb..e$'

string_list = ['gb98e', 'gblle', 'gbcje', 'gb..e', 'gboye', 'gbhde']

print(string_list)

for i in string_list:
	serach = re.search(pattern, i)
	if serach:
		print(serach.group())
	else:
		print('n')

#CHARACTER CLASSES
#square brackets mean match any character
pattern = r"[jdjdkfhf]"

str1 = 'lkqlkjwpo'
str2 = 'ksdoie'
str3 = 'baczbvaabvzbva'

if re.match(pattern, str1):
	print(1)

if re.match(pattern, str2):
	print(2)

if re.match(pattern, str3):
	print(3)

#square brackets single range [A-Z]
pattern = r'[A-Z]'

string = '90-0Gjk'

if re.match(pattern, string):
	print('y')

#square brackets single composite range [A-Za-z]
pattern = r'[A-Za-z]'

string = '987987ayuB'

match = re.search(pattern, string)

if match:
	print(match.start())

#square brackets multiple range [A-Z][a-z]
pattern = r'[A-Z][A-Z][a-z]'

string = '9K0-0PGjkH'

if re.search(pattern, string):
	print('y')
else:
	print('n')

#^ for inverted character class
pattern = r'[^A-Za-z]'

string = 'aSSDSsksk5'

match = re.search(pattern, string)

if match:
	print(match.start())
else:
	print('n')

#match
pattern = r'jim'

string = 'jim alkjaaksdflkjaskljfd'

if re.match(pattern, string):
	print('yes')


#search
pattern = r'jim'

string = 'alkjaaksjimdflkjaskljfd'

if re.search(pattern, string):
	print('yes')

match = re.search(pattern, string)

if match:
	print(match.group())
	print(match.start())
	print(match.span())

#findall
pattern = r'ka'

string = 'kajkahkljlkjkasdoifusdiokasdljfl;jkdklkapoisdopfi'

print(re.findall(pattern, string))



#finditer
pattern = r'ut'

string = 'lkajutlkajkljklutpojasl;kjflakjutlk;jaslkdjut'

match = re.finditer(pattern, string)

for i in match:
	print(i)



#re.sub
pattern = r'girl'

string = 'i am a girl'

repl = 'jam'

new_st = re.sub(pattern, repl, string)

print(new_st)


#.
pattern = r'gb..e'

string = 'gbadegesin'

match = re.search(pattern, string)

if match:
	print(match.group())



#^$
pattern = r'^gb..e$'

string_list = ['kskldsjgbine', 'gbadegesin', 'gbale']

for string in string_list:

	match = re.search(pattern, string)

	if match:
		print(match.group())
	else:
		print('no')


#CHARACTER CLASSES []

#[]
pattern = r'[A-Z]'

string = 'lkajkldjfkljFlkajkljG'

print(re.findall(pattern, string))


#[]
pattern = r'[A-Za-z]'

string = '9890890h987897'

print(re.findall(pattern, string))


#[]
pattern = r'[0-9]'
string = 'l;sdjfkljd8lksjdfkl9'
print(re.findall(pattern, string))


#[]
pattern  = r'[0-9][a-z]'

string = 'ksdkflkd4q'

print(re.findall(pattern, string))


#[^]
pattern = r'[^a-z0-9]'

string='kasdlk3fldAR'

print(re.findall(pattern, string))




#MORE METACHARACTERS *, +, ?, {}


1. #FOR ALL FOUR METACHARACTERS YOU CAN USE PARENTHESES IN YOUR PATTERN



2. #FOR ALL FOUR METACHARACTERS YOUR PATTERN CAN BEGIN WITH PARENTHESES



3. #FOR * IF YOUR PATTERN BEGINS WITH PARENTHESES THEN YOUR PATTERN MUST MATCH THE BEGINNING OF YOUR STRING



4. #FOR * AND + YOU CAN USE SQUARE BRACKETS



5. #FOR * IF YOUR PATTERN BEGINS WITH SQUARE BRACKETS THEN ANY OF THE CHARACTERS IN THE BRACKETS MUST START YOUR STRING. THE REGEX WILL START FROM THE FIRST CHARACTER OF THE STRING AND RETURN THE FIRST CONTINUOUS SEQUENCE OF CHARACTERS THAT CAN BE FOUND IN THE PATTERN.



6. #FOR + IF YOUR PATTERN BEGINS WITH SQUARE BRACKETS THEN YOUR STRING DOES NOT HAVE TO BEGIN WITH ANY OF THE CHARACTERS IN THE BRACKETS. THE REGEX WILL START FROM THE FIRST CHARACTER OF THE STRING AND RETURN THE FIRST CONTINUOUS SEQUENCE OF CHARACTERS THAT CAN BE FOUND IN THE PATTERN.



7. #FOR BOTH * AND + IF YOU AFTER FINDING THE MATCH PYTHON WILL INCLUDE ANY CONTINUOUS SEQUENCE OF CHARACTERS IN THE STRING THAT i, CAN BE FOUND IN THE PATTERN, AND ii, OCCUR IN THE STRING CONTIGUOUS TO THE MATCH



8. #FOR ? AND {,} YOUR PATTERN MUST ALWAYS MATCH THE BEGINNING OF YOUR STRING





#* for 0 or more repititions
#* IF YOUR PATTERN BEGINS WITH PARENTHESES IT MUST MATCH THE BEGINNING OF YOUR STRING
pattern = r'(island)*'

string='islandhislandGGGU'

match = re.search(pattern, string)

if match:
	print(match.group())
	print(match.span())

#* for 0 or more repititions
pattern = r'LKJ(island)*'

string='MHUTLPKP9sLKJislandislandGGGU'

match = re.search(pattern, string)

if match:
	print(match.group())
	print(match.span())

#* for 0 or more repititions
pattern = r'[island]*'

string='sk;lklagosislandlkj'

match = re.search(pattern, string)

if match:
	print(match.group())
	print(match.start())

#* for 0 or more repititions
#* USE SQUARE BRACKETS WITH CAUTION, BECAUSE PYTHON MIGHT INCLUDE ITEMS AFTER FINDING THE MATCH
pattern = r'lagos[island]*'

string='lk;lklagosislandsdanilkj'

match = re.search(pattern, string)

if match:
	print(match.group())

#+ for 1 or more repititions
pattern = r'(island)+'

string='lk;lklagosislandlkj'

match = re.search(pattern, string)

if match:
	print(match.group())

#+ for 1 or more repititions
pattern = r'gos(island)+'

string='lk;lklagosislandlkj'

match = re.search(pattern, string)

if match:
	print(match.group())

#+ for 1 or more repititions
#* IF YOUR PATTERN BEGINS WITH SQUARE BRACKETS PYTHON WILL TREAT YOUR PATTERN AS A CHARACTER CLASS
pattern = r'[island]+'

string='sk;lklagosislandlkj'

match = re.search(pattern, string)

if match:
	print(match.group())
	print(match.start())

#+ for 1 or more repititions
pattern = r'lagos[island]+'

string='lagosislandldsanikiknkkdkjlk'

match = re.search(pattern, string)

if match:
	print(match.group())

#? for 0 or 1 repititions
pattern = r'see-?saw'
string = 'seesaw'
match = re.search(pattern, string)
if match:
	print(match.group())

#{,} for 0 to infinity repititions
pattern = r'h(girl){,6}'
string='hgirlgirlgirl'
match=re.search(pattern, string)
if match:
	print(match.group())
	print(match.start())
	print(match.end())
	print(match.span())

#{,} for 0 to infinity repititions
pattern = r'8(9){0,3}'
string='8999878'
match=re.search(pattern, string)
if match:
	print(match.group())
	print(match.start())
	print(match.end())
	print(match.span())

#{,} for 0 to infinity repititions
pattern = r'(9){0,3}'
string='999878'
match=re.search(pattern, string)
if match:
	print(match.group())
	print(match.start())
	print(match.end())
	print(match.span())

#GROUPS
#groups and nested groups
#match.group(0)
#match.group(n)
#match.groups()
#?P<>
#?:

#SPECIAL SEQUENCES
#\n
#\d, [0-9]
#\s, [\t\n\r\f\v]
#\w, [a-zA-Z0-9]
#\D, non-digit
#\S, non-whitespace
#\W, non- word character

#EMAIL EXTRACTION
# r'([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)'

#PYTHONICNESS AND PACKAGING


#THE ZEN OF PYTHON

#Beautiful is better than ugly.

#Explicit is better than implicit.

#Simple is better than complex.

#Complex is better than complicated.

#Flat is better than nested.

#Sparse is better than dense.

#Readability counts.

#Special cases aren't special enough to break the rules.

#Although practicality beats purity.

#Errors should never pass silently.

#Unless explicitly silenced.

#In the face of ambiguity, refuse the temptation to guess.

#There should be one-- and preferably only one --obvious way to do it.

#Although that way may not be obvious at first unless you're Dutch.

#Now is better than never.

#Although never is often better than *right* now.

#If the implementation is hard to explain, it's a bad idea.

#If the implementation is easy to explain, it may be a good idea.

#Namespaces are one honking great idea -- let's do more of those!

#PEP - python enhancement proposals
#suggestions for improvements, made by developers

#PEP 8
#- modules should have short, all-lowercase names; 
#- class names should be in the CapWords style; 
#- most variables and function names should be lowercase_with_underscores; 
#- constants (variables that never change value) should be CAPS_WITH_UNDERSCORES;
#- names that would clash with Python keywords (such as 'class' or 'if') should have a trailing underscore.
#- using spaces around operators and after commas to increase readability. 
#- lines shouldn't be longer than 80 characters; 
#- 'from module import *' should be avoided; 
#- there should only be one statement per line.
#- use spaces, rather than tabs, to indent.
#- Don't bother with following PEP suggestions when it would cause your code to be less readable; inconsistent with the surrounding code; or not backwards compatible.

#PEP 20: The Zen of Python
#PEP 257: Style Conventions for Docstrings


#MORE ON FUNCTION ARGUMENTS
#arbitrary arguments - *args, print(args) # *args means 'all the other variables'
def myfun(name, *args):
	print(name)
	print(args)

myfun(1,2,3,4,5)

#default arguments
def myfun1(a, b, c=999):
	print(a, b, c)

myfun1(2,3,1000)
myfun1(2,3)

#keyword arguments - **kwargs, print(kwargs)
#a keyword argument is a named argument that you define at the point of calling the function
def myfun1(a,b, **kwargs):
	print(a, b, kwargs)

myfun1(3,4, d=9, c=90 )

#TUPLE UNPACKING
#tuple unpacking
mytuple = (565, -989, 7)
d,g,h = mytuple
print(d)
print(g)
print(h)

#variable swapping
a,b = 56, 0
print(a)
print(b)
b,a = a,b
print(a)
print(b)

#starred assignment
a,b,*c,d = (2,3,4,5,6,7,8,9)
print(a)
print(b)
print(c)
print(d)

#starred assignment
a,b,*c,d = (2,8,9)
print(a)
print(b)
print(c)
print(d)

#TERNARY OPERATOR
#Conditional expressions
a = 23
print(1 if a<20 else 34)

#MORE ON ELSE STATEMENTS
#for...else
#if the loop finishes normally, the else code runs
#if the break statement causes an exit fromthe loop, the else code won't run
for i in range(20):
	if i > 18:
		break
else:
	print(i)

#while...else
#if the loop finishes normally, the else code runs
#if the break statement causes an exit fromthe loop, the else code won't run
i = 0
while i<20:
	i+=1
	if i > 30:
		break
else:
	print(i)

#try except else
try:
	print(1+'1'==6)
except:
	print(2)
else:
	print(3)

#try except else
try:
	print(1/0)
except:
	print(2)
else:
	print(3)

#__MAIN__
if __name__ == '__main__':
	print('main')
else:
	print('mod')

def myfun():
	if __name__ == '__main__':
		print('main')
	else:
		print('mod')

#MAJOR THIRD PARTY LIBRARIES
#Django - web framework
#CherryPy - web framework
#Flask - web framework
#BeautifulSoup - library
#matplotlib - module for creating graphs
#NumPy - module for working with arrays
#SciPy - extends functionality of arrays
#pygame - 2D games
#Panda3D - 3D games


#PACKAGING

#Import Modules required for Packaging
#setuptools
#distutils

#Create directory structure
"""
my_super_parent_directory/
    setup.py
	LICENSE.txt
   	README.txt
   	my_parent_directory/
    	__init__.py
      	myfile.py
      	myfile2.py
"""

#Write setup.py file
from distutils.core import setup

"""
setup(
   name='SoloLearn', 
   version='0.1dev',
   packages=['sololearn',],
   license='MIT', 
   long_description=open('README.txt').read(),
)
"""

#Build source diistribution
#navigate to setup.py
#run 'python setup.py sdist'

#Build binary diistribution (executable installer)
#navigate to setup.py
#run 'python setup.py bdist' or 'python setup.py bdist_wininst'

#Upload package
#1. run python setup.py register
#2. run python setup.py sdist upload

#Install package
#python setup.py install


#PACKAGING FOR USERS WITHOUT PYTHON INSTALLED

#converting scripts to executables:

#PyInstaller and cx_Freeze - windows and mac
#py2exe - windows only
#py2app - mac only