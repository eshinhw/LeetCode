

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
         
        counts = {}
         
        for num in nums:
             
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
         
        for k,v in counts.items():
             
            if v == 1:
                return k