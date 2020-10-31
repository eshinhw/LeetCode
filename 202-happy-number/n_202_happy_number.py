
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = []
            
        
        while (n != 1):
            
            curr = n
            total = 0
            
            while (curr != 0):
                
                total += (curr % 10) * (curr % 10)
                curr = curr // 10
            
            if total in seen:
                return False
        
    
            seen.append(total)
            n = total
                
        return True       


print(Solution().isHappy(19))

