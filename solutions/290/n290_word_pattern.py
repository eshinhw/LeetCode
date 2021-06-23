
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        
        pattern_set = set(pattern)
        str_set = set(str.split(' '))
        
        if len(pattern_set) != len(str_set):
            return False
        
        words_list = str.split(' ')
        words_dict = {}
        
        for word in words_list:
            
            if word not in words_dict:
                words_dict[word] = 'a'
            
    
        


a = Solution()

a.wordPattern("abba", "dog cat cat dog")

print(set("abba"))