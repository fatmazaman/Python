import time

# Method.
def square1(n):
   return n ** 2

# Lambda method.
square2 = lambda n: n ** 2
x = time.time()

print(x)
# Use def method.
i = 0
while i < 10000000:
   square1(1)
   i += 1
y = time.time()
print "time for def method:", y-x

# Use lambda method.
i = 0
while i < 10000000:
   square2(1)
   i += 1
z = time.time()
print "time for lambda method:", z-y
print "\nThe results show that both methods(def & lambda)are close in performance.\n"



