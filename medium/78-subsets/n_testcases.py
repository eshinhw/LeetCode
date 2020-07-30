

def subsets(nums):
    
    
    if len(nums) == 0:
        return []
    else:
        output = []
        output.append([])
    
    for i in range(len(nums)):
        nl = []
        nl.append(nums[i])
        output.append(nl)
        
        for j in range(i+1,len(nums)):
            nl = nl.copy()
            nl.append(nums[j])
            output.append(nl)
            
    
    print(output)


subsets([1,2,3])