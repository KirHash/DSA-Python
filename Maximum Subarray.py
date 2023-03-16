#Leetcode

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxSub = nums[0]
        currSum = 0

        for i in nums:
            if currSum < 0:
                currSum = 0
            currSum += i
            maxSub = max(maxSub, currSum)
        return maxSub
