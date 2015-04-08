#Format an RGB value (three 1-byte numbers) as a 6-digit hexadecimal string.



#Write a function to reverse a string.
text = 'fatma'
def reverse(text):
	return text[::-1]
	

reverse(text)

#Write function to compute Nth fibonacci number:
#F(n)=F(n-1) + F(n-2)
#Will try to write sequence also

def fibonacci(N):
	if N < 2:
		return N
	else:
		return fibonacci(N-1)+fibonacci(N-2)
fibonacci(8)

for i in range(8):
    print(fibonacci(i))

fibonacci(8)   

#Print out the grade-school multiplication table up to 12x12

def mul(max, min):
    for i in range(1,max):
	    for j in range(min,13):
		    print i*j, '\t',
	    print


mul(13,1)



#Write a function that sums up integers from a text file, one int per line.

def sum_file(filename):
    return (sum(int(l) for l in open(filename).readlines()))


#Write function to print the odd numbers from 1 to 99.

def odd():
	for i in range(1,100):
		if i%2 != 0:
			print i
odd()

def odd1():
	for i in range(1,100,2):
		print i
odd1()	

#Find the largest int value in an int array.'''
array = [1,2,3,4,5,6,7,8,9]
def maxval(array):
	temp= array[0] #1
	for i in array:
		if i>temp:
			temp = i
	print temp
		    
maxval(array)








