

class Solution:
    def climbStairs(self, n: int) -> int:
        
        dp = {}
        
        # Base Cases n = 0 or n = 1
        
        dp[0] = 1
        dp[1] = 1
        
        for i in range(2,n+1):
            dp[i] = dp[i-1] + dp[i-2]
            
        
        return dp[n]
        


cs = Solution()

print(cs.climbStairs(4))
        
        