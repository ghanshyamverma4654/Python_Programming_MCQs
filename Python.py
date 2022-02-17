

a = '2'
b = '2'
print(a + b)

#Output: 22

#--------------------------------->

a  = "python"
b = "pythoN"
print(a > b)

#Output: True

#---------------------------------->

def function():
	a = 100
	return a
a = function() + 1	
print(a)

#OutputL: 101

#---------------------------------->

list = [5, 10, 15, 25]
print(list[::-2])

#Output: [25, 10]

#---------------------------------->

a = 1
b = 0
print(any(a, b))

#Output: TypeError: any() takes exactly one argument (2 given)

#----------------------------------->

stuffs = ["q", "b", "c"]
stuffs.clear(1)
print(stuffs)

#Output:  TypeError: list.clear() takes no arguments (1 given)

#------------------------------------>

for variable in range(-2, -5, -1):
	print(variable, end=", ")

	#Output: -2, -3, -4,

#------------------------------------>

b = 30
def function(a, b=b):
	return a+b
print(function(1))	

#Output: 31

#------------------------------------>

index = 2
for index in range(index < 2):
	index = index + 3
print(index)

#Output: 2

#------------------------------------>

l1 = [1, 2, 3]
l2 = l1
print(l1 is l2,  l1 == l2)

#Output: True True

#------------------------------------>

def add(a, b):
	return a + 5, b + 5
result = add(3, 2)
print(result)


# Output: (8, 7)

# ------------------------------------->

def function(a=12, b=12):
	print(a // 9)
	return (a * b)


function(a=9, b=2)


# Output: 1

# -------------------------------------->

# PYTHON RECURSION EXAMPLES

def sum(n):
	total = 0
	for index in range(n + 1):
		total += index
	return total


result = sum(100)
print(result)


# Output: 5050

# =====================================

def countdown(n):
	print(n)


if n == 0:
	return
else:
	countdown(n - 1)
countdown(5)

# Output: SyntaxError: 'return' outside function

# -------------------------------------->
