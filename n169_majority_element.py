

class MySolution:
    def majorityElement(self, nums: List[int]) -> int:
        
        counts = {}
        
        for num in nums:
            
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        
        majority = len(nums) // 2
        
        for k,v in counts.items():
            
            if v > majority:
                return k
            

            
class AlternativeSolution1:
    def majorityElement(self, nums):
        
        nums.sort()
        return nums[len(nums)//2]


    
from collections import Counter
    
class AlternativeSolution2:
    def majorityElement(self, nums):
        majority = len(nums) // 2
        count_dic = Counter(nums)
        for k,v in count_dic.items():
            if v > majority:
                return k