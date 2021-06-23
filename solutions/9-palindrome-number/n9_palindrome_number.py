
class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        original = x
        temp = 0
        
        if x < 0:
            return False
        
        while (x != 0):
            temp = (temp * 10)  + (x % 10)
            x = x // 10
            
            print("temp: {} | x: {}".format(temp,x))        

        return (temp == original)
    
    def isPalindromeV2(self, x: int) -> bool:
        
        numStr = str(x)
        numList = list(numStr)
        print(numList)
        
        start = 0
        end = len(numList) - 1
        
        while (start < end):
            if numList[start] != numList[end]:
                return False
            else:
                start += 1
                end -= 1
        
        return True
        
    

sol = Solution()
#sol.isPalindrome(123)

# print out
# -----------------
# temp: 3 | x: 12
# temp: 32 | x: 1
# temp: 321 | x: 0

#sol.isPalindrome(121)

# print out
# -----------------
# temp: 1 | x: 12
# temp: 12 | x: 1
# temp: 121 | x: 0

sol.isPalindromeV2(123)




