from typing import List

class Solution:

    def removeDuplicatesV1(nums: List[int]) -> int:
        
        if len(nums) == 0:
                return 0
        else:
            i = 0
            while i < len(nums)-1:
                if nums[i] == nums[i+1]:
                    del nums[i]
                else:
                    i += 1
        return len(nums)
    
    
    def removeDuplicatesV2(nums: List[int]) -> int:
        
        temp = set(nums)        
        nums.clear()        
        nums.extend(temp)
        nums.sort()
        return len(nums)
    
    def removeDuplicatesV3(nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        i=0
        for j in range(1,len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        
        return i+1




print (Solution.removeDuplicatesV1([1,1,2]))
