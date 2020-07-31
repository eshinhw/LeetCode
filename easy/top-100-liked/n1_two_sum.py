"""
#1. Two Sum (Top 100 Liked Questions)

When constructing a dictionary to store index information,
We have to construct it when we are in the first for loop.

If we attempt to construct a dictionary first,
then try to access the right two indices,
there is a problem of duplicates and things get more complicated.
"""


def twoSum(nums: List[int], target: int) -> List[int]:
    
    loc = {}
    
    for i in range(len(nums)):            
        remainder = target - nums[i]            
        if remainder in loc:
            return [i, loc[remainder]]            
        else:
            loc[nums[i]] = i
            

