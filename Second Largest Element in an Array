#GFG

class Solution:

	def print2largest(self,arr, n):
		if n == 1:
		    return -1
		
        max = float('-inf')
        secondmax = float('-inf')
		
		for i in range(n) :
		    if arr[i] > max:
		        secondmax = max
		        max = arr[i]
		    elif arr[i] > secondmax and arr[i] < max:
		        secondmax = arr[i]
		
		if secondmax > float('-inf'):
		    return secondmax
		else:
		    return -1
