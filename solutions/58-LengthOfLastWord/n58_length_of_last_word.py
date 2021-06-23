
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        
        # testcase 1: string is empty
        if s == '':
            return 0
        
        # if input string is not empty,
        # string is splited by whitespace
        # and returned as a list
        s = s.split()
        
        # equivalent to if not s:
        if s == []:
            return 0
        else:
            return len(s[-1])
        

