#Add two number without using '+' operator
def Add_number(x,y):
	if(x>y):
		return x*2 - (x-y)
	else:
	    return y*2 - (y-x)

#Add two number without using any arithmetic operators
def Add(x,y):
    while (b):
        carry = x & y
        x = x ^ y
        y = carry << 1
    return x 




