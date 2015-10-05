# add two number
def add(a,b):
	print "Adding %d and %d :" % (a,b)
	return a + b

#subtract two number	
def subtract(a,b):	
	print "subtracting %d and %d:" % (a,b)
	return a + b

#Multiply two number
def multiply(a,b):
	print "Multiplying %d and %d:" % (a,b)
	return a * b

#Divide two number
def divide(a,b):
	print "Dividing %d and %d:" % (a,b)
	return a / b

print "Let's play with some math function!"

age = add (25,2)
height = subtract(27,2)
weight = multiply(5,6)
iq = divide(74,2)

print "Puzzle time!"

what = add(age,subtract(height,multiply(weight,divide(iq,2))))

print "That become", what, "can you do it by hands"



