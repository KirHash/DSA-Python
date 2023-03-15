#Leetcode

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)

        count = 0
        majority = 0

        for i in range(n):
            if count == 0:
                majority = nums[i]
            if nums[i] == majority:
                count += 1
            else:
                count -= 1
        return majority
