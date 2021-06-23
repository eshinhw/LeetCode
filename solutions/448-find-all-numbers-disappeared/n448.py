
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        correctSet = set(range(1, len(nums)+1))
        
        nums = set(nums)
        
        return correctSet - nums
    

