"""
53. Maximum Subarray

Used Kadane's algorithm to find the maximum sum of sub-array with
linear complexity of O(n).
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        globalSum = currSum = nums[0]
        
        for i in range(1,len(nums)):

            currSum = max(nums[i],currSum+nums[i])
            globalSum = max(globalSum,currSum)
        
        return globalSum
    
    