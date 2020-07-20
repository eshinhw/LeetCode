

def containsNearbyDuplicate(nums, k: int) -> bool:
    

    count = {}

    for i in range(len(nums)):
        
        if nums[i] not in count:
            
            count[nums[i]] = [i]
        
        elif i - count[nums[i]][len(count[nums[i]]) - 1] <= k:
            
            print("Second condition")
            
        else:
            count[nums[i]].append(i)
            
    print(count)
    
    return False


print(containsNearbyDuplicate([1,2,3,1,2,3], 2))