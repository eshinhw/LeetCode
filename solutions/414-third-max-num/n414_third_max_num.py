from typing import List

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        # remove duplicates
        
        toList = list(set(nums))
        
        # sort the list in descending order (largest to smallest)
        
        toList.sort(reverse=True)
        
        if len(toList) == 1:
            return toList[0]
        
        elif len(toList) == 2:
            return toList[0]
        
        # return the third element from the beginning
        else:
            return toList[2]

    def thirdMax(self, nums: List[int]) -> int:
        
        sorted_set = sorted(set(nums), reverse=True)
        
        if len(sorted_set) >= 3:
            return sorted_set[2]
        else:
            return sorted_set[0]
        
        
        


sol = Solution()
print(sol.thirdMax([1,2]))