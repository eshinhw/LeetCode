
class Solution:
    def reverseWords(self, s: str) -> str:
        
        
        toList = s.split(' ')
        print(toList)
        outString = ''
        
        for i in range(len(toList)):
            if i != (len(toList) - 1):
                outString = outString + toList[i][::-1]
                outString = outString + ' '
            else:
                outString = outString + toList[i][::-1]
        
        print(outString)
        return outString
    
    def reverseWords(self, s: str) -> str:
        
        return ' '.join(t[::-1] for t in s.split(' '))

sol = Solution()
sol.reverseWords("Let's take LeetCode contest")