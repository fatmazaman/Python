#lambda

'''The lambda operator or lambda function is a way to create 
    small anonymous functions,i.e. functions without a name.''' 

#lambda function : lambda argument_list: expression 
f = lambda x , y : x + y

print "lambda's Magic"
print f(1,2)

# The map()function
'''map() is a function with two arguments:map(func, seq)The first 
   argument func is the name of a function and the second a sequence 
   (e.g. a list) seq. map() applies the function func to all the 
   elements of the sequence seq. It returns a new list with the 
   elements changed by func'''

def fahrenheit(T):
	return ((float(9)/5)*T + 32)

def celcius(T):
	return (float(5)/9) * (T-32)

T = [36.5, 37, 37.5, 100, 50, 49]	

F = map(fahrenheit, T)
C = map(celcius, F)

print F,C

#Another way Around
Celsius = [39.2, 36.5, 37.3, 37.8]
Fahrenheit = map(lambda x: (float(9)/5)*x + 32, Celsius)
print Fahrenheit
C = map(lambda x: (float(5)/9)*(x-32), Fahrenheit)
print C

#Another example of map() function with lambda operator

a = [1,2,3,4]
b = [17,12,11,10]
c = [-1,-4,5,9]
print map(lambda x,y:x+y, a,b)
print map(lambda x,y,z:x+y+z, a,b,c)
print map(lambda x,y,z:x+y-z, a,b,c)


#Filtering:The function filter(function, list) offers an elegant way to 
#filter out all the elements of a list.

fib = [0,1,1,2,3,5,8,13,21,34,55]
result = filter(lambda x: x % 2, fib)
print result
result = filter(lambda x: x % 2 == 0, fib)
print result

#reduce()
'''The function reduce(func, seq) CONTINUALLY applies the function func() 
to the sequence seq. It returns a single value.''' 

print reduce(lambda x,y: x+y, [47,11,42,13])
f = lambda a,b: a if (a > b) else b
print reduce(f, [47,11,42,102,13])
print reduce(lambda x, y: x+y, range(1,101))



