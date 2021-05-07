
class Solution:

    def twoSum(self, nums, target):

        loc = {}

        for i in range(len(nums)):
            remainder = target - nums[i]
            if remainder in loc:
                return [i, loc[remainder]]
            else:
                loc[nums[i]] = i


sol = Solution()

print(sol.twoSum([2,7,11,15], 9))
# returns [1,0]
# target = 9 = nums[1] + nums[0] = 7 + 2 = 9

print(sol.twoSum([11,7,2,15], 9))
# returns [2,1]
# target = 9 = nums[2] + nums[1] = 2 + 7 = 9

print(sol.twoSum([11,5,2,15], 9))
# returns None





