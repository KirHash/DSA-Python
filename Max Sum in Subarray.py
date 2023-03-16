#GFG

class Solution:
    def pairWithMaxSum(self, arr, N):
        
    	if (N<2):
           return -1
        res = arr[0]+arr[1]
        for i in range(1,N-1):
            res = max(res,arr[i]+arr[i+1])
        return res
