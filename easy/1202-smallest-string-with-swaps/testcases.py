

def smallestStringWithSwaps(s: str, pairs) -> str:
    
    if s == "":
        return ""
    
    if not pairs:
        return s

    slist = list(s)
    smallest = s
    
    print("slist: ", slist, "smallest: ", smallest)
    
    for i in range(len(pairs)):
        copy = slist
        copy[pairs[i][0]], copy[pairs[i][1]] = copy[pairs[i][1]], copy[pairs[i][0]]
        
        print(str(copy))
        
        copy = ''.join(copy)
        
        #print("copy: ", copy)
            
        if copy < smallest:
            smallest = copy
            
    print(smallest)
            
    return ''.join(smallest)


smallestStringWithSwaps("dcab", [[0,3],[1,2],[0,2]])