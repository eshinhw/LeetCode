from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        count = {}
        
        for num in nums:
            
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        threshold = len(nums) // 3
        outList = []
        
        for k,v in count.items():
            
            if v > threshold:
                outList.append(k)
        
        return outList
    

