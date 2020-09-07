

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def helper(left, right):
        
            while (left >= 0 and right < len(s) and s[left] == s[right]):
                left -= 1
                right += 1
            
            #print("i: ",i,"substring: ",s[left+1:right])

            return s[left+1:right]
        
        output = ""
        
        for i in range(len(s)):
            test = helper(i,i)
            if len(test) > len(output): output = test
            test = helper(i,i+1)
            if len(test) > len(output): output = test
        
        return output
    

a = Solution()
a.longestPalindrome("babad")
