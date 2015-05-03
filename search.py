print "******************************************************************"
print "********************** Linear Search *****************************"
print "******************************************************************\n"
#linear search algorithm
def linear_search(x, nums):
    for i in range(len(nums)):
        if nums[i] == x:
            return i
    return "Number Not Found" 
nums = [1,23,45,6,7,8,99,76]  

print "Then index of the number is :",linear_search(99,nums),"\n"

#Time complexity 
	#Best case:		1 step (Bigoh(1))
	#Average case:	n/2 steps(Bigoh(n))
	#Worse case:    n steps(Bigoh(n))

#binary search algorithms
print "******************************************************************"
print "********************** Binary Search ****************************"
print "******************************************************************\n"

list =[1,2,3,4,5,6,7,8,9]
def binary_search(x, nums):
    low = 0
    high = len(nums) - 1
    while low <= high: 
        mid = (low + high) / 2 
        item = nums[mid]
        if x == item : 
            return mid
        elif x < item: 
            high = mid - 1 
        else: 
            low = mid + 1 
    return "Number not found"

print "Then index of the number is :",binary_search(4,list),"\n"    

#Time complexity 
    #Best case:     Bigoh(1)
    #Average case:  Bigoh(logn)
    #Worse case:    Bigoh(logn)

    