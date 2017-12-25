
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

class Solution:
    def twoSum(self, nums, target):
        dic = {}
        for i in range(len(nums)):
            num = nums[i]
            if target-num in dic:
                return sorted([i, dic[target-num]])
            dic[num] = i


solution = Solution()
print(solution.twoSum([3, 2, 4], 6))







