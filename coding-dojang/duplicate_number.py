

def duplicates(s):
    
    sList = list(s)
    d = {}
    used = []
    
    for i in range(len(sList)):
        
        if sList[i] in d:
            d[sList[i]] += 1
        else:
            d[sList[i]] = 1
            used.append(sList[i])
    
    
    
    for k,v in d.items():
        
        if v != 1 or v :
            return False
        
    return len(used) == 10
        
    
    


print(duplicates("01234"))