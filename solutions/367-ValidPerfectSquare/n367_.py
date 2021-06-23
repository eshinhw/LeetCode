class Solution:
    def isPerfectSquareBinarySearch(self, num: int) -> bool:
        
        
        low = 1
        high = 2**31 - 1
        mid = (low + high) // 2
        
        
        
        while (low <= high):
            
            mid = (low + high) // 2
            
            if mid * mid == num:
                return True
            elif mid * mid < num:
                low = mid+1
            else:
                high = mid-1
        
        return False
    
    def isPerfectSquare(self, num: int) -> bool:
    
    
        n = 1
        
        while (n*n <= num):
            
            if n*n == num:
                return True
            elif n*n > num:
                return False
            else:
                n += 1
                
                
    