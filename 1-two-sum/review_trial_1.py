

class Solution:
    def twoSum(self, nums, target):

        location = {}

        for i in range(len(nums)):

            remainder = target - nums[i]

            if remainder in location:

                return [i, location[remainder]]
            else:

                location[nums[i]] = i


