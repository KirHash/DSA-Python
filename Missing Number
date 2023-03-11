#Leetcode

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """


        n = len(nums)

        hashTable = {}

        for i in nums:
            hashTable[i] = True

        for i in range(n+1):
            if i not in hashTable:
                return i
