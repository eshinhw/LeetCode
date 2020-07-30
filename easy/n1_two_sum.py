"""
#1. Two Sum (Top 100 Liked Questions)
"""


def twoSum(nums: List[int], target: int) -> List[int]:
    
    loc = {}
    
    for i in range(len(nums)):            
        remainder = target - nums[i]            
        if remainder in loc:
            return [i, loc[remainder]]            
        else:
            loc[nums[i]] = i
            

