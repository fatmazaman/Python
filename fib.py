#normal method
def fibonacci(N):
	if N < 2:
		return N
	else:
		return fibonacci(N-1)+fibonacci(N-2)
fibonacci(8)

for i in range(8):
    print(fibonacci(i))

fibonacci(8)   

#efficient method

def fibonacci(n):
    fibs = [0, 1]
    for i in range(2, n+1):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs


print fibonacci(10)
print fibonacci(10)[8]

#efficient
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
    return a
print fib(10)    