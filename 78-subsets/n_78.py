
"""
nums = []
output = [[]] (1 subset)

nums = [1]
output = [[], [1]] (2 subsets)

nums = [1,2]
output = [[], [1], [2], [1,2]] (4 subsets)

nums = [1,2,3]
output = [[], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3]] (8 subsets)

"""






class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        
        output = [[]]
        
        for num in nums:
            
            # list comprehension
            output = output + [lst + [num] for lst in output]
        
        return output
    
    



