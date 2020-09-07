

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        numSet = set(nums)
        fullSet = set()
        
        n = 1
        
        while (n <= len(nums)):
            fullSet.add(n)
            n += 1
        
        return (list(fullSet - numSet))
    

class AlternativeSolution1:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
    
        marked = set(nums)
        return [i for i in range(1, len(nums)+1) if i not in marked]