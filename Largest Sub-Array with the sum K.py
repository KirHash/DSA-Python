#GFG

class Solution:
    def lenOfLongSubarr (self, arr, n, k) : 
        #Complete the function
    
        sum_dic={0:-1}
        
        s=0
        res=0
        
        
        for i in range(n):
            s+=arr[i]
            if s not in sum_dic:
                sum_dic[s]=i
            if (s-k) in sum_dic:
                res=max(res,i-sum_dic[s-k])
        return res  
