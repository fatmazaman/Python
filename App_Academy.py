# Crazy Sum

def crazy_sum(numbers):
	sum =0
	for i in range(len(numbers)):
		sum += numbers[i]*i
	return sum

print crazy_sum([2])	

print crazy_sum([2,3])

print crazy_sum([2,3,5])

print crazy_sum([2,3,5,2])	


# Square Number
def square_numbr(max):
	x = 1
	sqr = [ ]
	for x in range(1, max):
		if x * x < max:
			sqr.append(x * x)
		else:
			break
	return len(sqr)

print square_numbr(5)
print square_numbr(10)
print square_numbr(15)
print square_numbr(25)

# Crazy Number
def crazy_nums(max):
    number  = []
    for num in range(1,max):
  		if num%3 == 0 or num%5 ==0:
  			number.append(num)
  			if num%3 == 0 and num%5 ==0:
  				number.remove(num)
    return number

print  crazy_nums(3)
print  crazy_nums(10)
print  crazy_nums(20)
