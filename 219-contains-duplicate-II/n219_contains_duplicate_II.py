
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        count = {}
        
        for i in range(len(nums)):
            
            # if num element is not in dictionary,
            # create a new index list
            
            if nums[i] not in count:
                count[nums[i]] = [i]
                
            # if the current element is in dictionary and
            # the difference between the closest index, the last element of the list,
            # and the index about to add is less than k,
            # return true
            
            elif i - count[nums[i]][len(count[nums[i]]) - 1] <= k:
                return True
            
            # otherwise, we add the list at the end of the index list
            
            else:
                count[nums[i]].append(i)
            
        return False
    
    def containsNearbyDuplicateV2(self, nums: List[int], k: int) -> bool:
        
        count = {}
        
        for i in range(len(nums)):
            if nums[i] not in count:
                count[nums[i]] = i
            
            else:
                if i - count[nums[i]] <= k:
                    return True
                else:
                    count[nums[i]] = i
        
        return False

