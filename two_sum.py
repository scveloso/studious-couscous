"""
TWO SUM

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nummap = {}
        i = 0
        for num in nums:
            nummap[target - num] = i
            i += 1

        j = 0
        for num in nums:
            if num in nummap and j != nummap[num]:
                return [nummap[num], j]
            j += 1

        return []
        
