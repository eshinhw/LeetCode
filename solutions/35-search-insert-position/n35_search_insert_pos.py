class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        for i in range(len(nums)):
            
            if target < nums[0]:
                return 0
            elif (nums[i] == target) or (target < nums[i]):
                return i
            elif nums[len(nums) - 1] < target:
                return len(nums)
    
        return 0

    def searchInsertV2(self, nums: List[int], target: int) -> int:
        
        if target in nums:
            return nums.index(target)
        
        if target < nums[0]:
            return 0
        
        elif target > nums[len(nums) - 1]:
            return len(nums)
        
        else:
            start = 0
            end = len(nums) - 1
            
            while (start < end):
                middle = (start + end) // 2
                
                if nums[middle] < target:
                    start = middle + 1
                else:
                    end = middle
        
        return start
    
