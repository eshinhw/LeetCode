"""
53. Maximum Subarray

Used Kadane's algorithm to find the maximum sum of sub-array with
linear complexity of O(n).
"""

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        maxSum = nums[0]
        currSum = 0

        for num in nums:

            if (currSum < 0):
                currSum = 0

            currSum += num

            maxSum = max(currSum, maxSum)

        return maxSum

