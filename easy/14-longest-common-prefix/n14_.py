

def longestCommonPrefix(strs):
    
    if len(strs) == 0:
        
        return ""
    
    
    
    
    output = ""
    
    # Find the shortest length
    
    shortestLen = len(strs[0])
    
    for i in range(len(strs)):
        shortestLen = min(len(strs[i]),shortestLen)
    
    print(shortestLen)
    
    # Compare each letter through for loop
    i = 0
    while (i < shortestLen):
        
        char = strs[0][i]
        
        for j in range(1,len(strs)):
            
            if strs[j][i] != char:
                return output
            
        output = output + char
        i += 1
        
        
            
            
            
            

            

            
print(longestCommonPrefix(["flower","flow","flight"]))
        