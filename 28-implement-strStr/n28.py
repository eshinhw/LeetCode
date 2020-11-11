
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        if needle == "": return 0
        
        return haystack.find(needle)
    
    def strStr_faster(self, haystack: str, needle: str) -> int:
        if needle == '':
            return 0
        else:
            try:
                return haystack.index(needle)
            except:
                return -1
    

# a = Solution()
print(Solution.strStr(Solution,"hello", "ll"))
        