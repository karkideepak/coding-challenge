# 1. Two Sum
"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""
# Brute Force Approach
"""
We take the value of first index and check with the values of rest of indices to 
see if the sum adds upto the target.
nums = 3,4,7,11,14, target=21
3+5=8
3+7=10
..... 7+14=21 which satisfies the requirement or condition
Time complixiety = O(n^2)
Space comlixiety = O(1)
"""
# One pass approach
"""
We are going through the loop only once. We will take a dictionary to check 'target-num[0]'
nums = 3,5,7,11,14, target=21
21-3=18
21-5=16
21-7=14
21-11=10
21-14=7
Value:Index
3:0
5:1
7:2 <----- this exists in the dictionray for (21-14)
11:3
    <----- return the indices
[2,4]
Time complixiety of insertiona and searching:O(n)
Space complixiety: O(n)
"""

# Solution 1
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} # val : index

        for i, n in enumerate(nums):
            diff = target -n
            if diff in prevMap:
                return[prevMap[diff], i]
            prevMap[n] = i
        return
"""
# Solution 2
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums:List[int]
        :type target:[int]
        :rtype: List[int]
        """
        dic = {}
        for i, v in enumerate(nums):
            if(target - v in dict):
                return dic[target - v], i
            dic[v] = i