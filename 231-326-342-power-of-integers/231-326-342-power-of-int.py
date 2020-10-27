"""
Power of Integer Series
"""

class Solution:
    def isPowerOfTwo(self, num: int) -> bool:
        
        if num == 1:
            return True
        
        n = 1
        
        while (n < num):
            n *= 2
        
        return n == num
    

    def isPowerOfThree(self, num: int) -> bool:
        
        if num == 1:
            return True
        
        n = 1
        
        while (n < num):
            n *= 3
        
        return n == num
    
    def isPowerOfFour(self, num: int) -> bool:
        
        if num == 1:
            return True
        
        n = 1
        
        while (n < num):
            n *= 4
        
        return n == num

        

a = Solution()


print(a.isPowerOfTwo(64))
print(a.isPowerOfThree(64))
print(a.isPowerOfFour(64))