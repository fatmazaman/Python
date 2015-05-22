#Searching an Element in a Rotated Sorted Array
'''Suppose a sorted array is rotated at some pivot unknown to you beforehand.
   How do you find an element in the rotated array efficiently? 
   You may assume no duplicate exists in the array'''

def rotated_array(arr, key):
	N = len(arr)
	L = 0
	R = N-1
	while A[L] < A[R]:
        M = (L+R)/2
        if A[M] == key:
        	return M
        elif A[M] < key:
        	




  

