

class Solution:
    
    def isPowerOfTwo(self, n: int) -> bool:
        if (n == 0):
            return False
        
        power = 0
        
        while ((2**power) <= n):
            
            if (2**power) == n:
                return True
            else:
                power += 1
        
        return False
    


    
    
