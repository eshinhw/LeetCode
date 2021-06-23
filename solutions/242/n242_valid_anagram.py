class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        s_letters = {}
        t_letters = {}
        
        for ch in s:
            
            
            if ch not in s_letters:
                s_letters[ch] = 1
            else:
                s_letters[ch] = s_letters[ch] + 1
        
        for ch in t:
            
            if ch not in t_letters:
                t_letters[ch] = 1
            else:
                t_letters[ch] = t_letters[ch] + 1
            
        return s_letters == t_letters
    
        

a = Solution()

a.isAnagram("anagram", "nagaram")