#Add two number without using '+' operator
print "******************************************************************"
print "**********Add two number without using '+' operator***************"
print "******************************************************************\n"

def Add_number(x,y):
	if(x>y):
		return x*2 - (x-y)
	else:
	    return y*2 - (y-x)
print "The Addition of two number are:",Add_number(8,5)

#Add two number without using any arithmetic operators
print "\n******************************************************************"
print "******Add two number without using any arithmetic operator********"
print "******************************************************************\n"

def Add(x,y):
    while (y):
        carry = x & y
        x = x ^ y
        y = carry << 1
    return x 
print "The Addition of two number are:", Add(8,5)

#Sub two number without using any arithmetic operators
print "\n*******************************************************************"
print "*****Subtract two number without using any arithmetic operator*****"
print "*******************************************************************\n"

def Sub(a,b):
	while (b==0):
		borrow = (~a) & b
		a = a ^ b
		b = borrow << 1
	return b
print "The Subtraction of two number are:", Sub(8,5) 

#Sub two number using add function 
print "\n*******************************************************************"
print "*****Subtract two number with Add function ************************"
print "*******************************************************************\n"  	

def sub(a,b):
    return Add(a, Add(~b, 1))
print "The Subtraction of two number are:", Sub(8,5) 


#Multiply two number without using '*' operator.
print "\n*******************************************************************"
print "*****Multiplication of two number without '*' operators ***********"
print "*******************************************************************\n"  	

def mul(a,b):
	c = 0
	c =sum(a for i in range(b))
	return c

print "The Multiplication of two number are:", mul(8,5) 

#Division two number without using '/' operator.
print "\n*******************************************************************"
print "*****Division of two number without '/' operators ***********"
print "*******************************************************************\n"  	

def div(x,y): 
    quotient = 0;
    while (x >= y):
        x  -=  y #(if numerator is not equal or less than the divisor)
        quotient +=1
    return quotient;
print "The Division of two number are:", div(10,5),"\n" 