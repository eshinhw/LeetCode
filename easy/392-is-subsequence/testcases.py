

def isSubsequence(s: str, t: str) -> bool:
    
        
    i = 0
    
    for ch in t:
        
        if i >= len(s):
            return True
        
        if ch == s[i]:
            print(ch)
            i += 1
        

    print(i)
    return i == len(s)
        
        
    

# print(isSubsequence("twn", "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxtxxxxxxxxxxxxxxxxxxxxwxxxxxxxxxxxxxxxxxxxxxxxxxn"))

print(isSubsequence("axc", "ahbgdc"))