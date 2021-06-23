
class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # empty string
        if s == "":
            return True
        
        s = s.strip().lower()
        
        newString = ""
        
        for ch in s:
            if ch.isalnum():
                newString = newString + ch

        start = 0
        end = len(newString) - 1
        
        while (start < end):
            
            if newString[start] != newString[end]:
                return False
            else:
                start += 1
                end -= 1
        
        return True
    
    def isPalindromeV2(self, s: str) -> bool:
        
        # empty string
        if s == "":
            return True
        
        s = s.strip().lower()
        
        newString = ""
        
        for ch in s:
            if ch.isalnum():
                newString = newString + ch
                
        return newstring[::-1] == newString
    


