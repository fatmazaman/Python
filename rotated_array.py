#Searching an Element in a Rotated Sorted Array
'''Suppose a sorted array is rotated at some pivot unknown to you beforehand.
   How do you find an element in the rotated array efficiently? 
   You may assume no duplicate exists in the array'''

def rotated_array(arr, key):
	N = len(arr)
	L = 0
	R = N-1
	while (A[L] < A[R]):
        M = L + ((R - L) / 2)
        if A[M] == key:
        	return M
        #the bottom half is sorted	
        if (A[L] <= A[M]):
        	if (A[L] <= key && key < A[M]):
        	    R = M - 1
            else:
                L = M + 1	
        #the upper half is sorted
        else: 
            if (A[M] < key && key <= A[R]):
                L = M + 1;
            else: 
                R = M - 1;
    return -1


print  rotated_array([4,5,6,7,8,1,2,3], 5) 


       


    
  

