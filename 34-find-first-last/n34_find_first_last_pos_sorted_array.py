

class Solution:
    def searchRange(self, nums, target: int):
        
        left, right = 0, len(nums) - 1
        
        while (left <= right):
            mid = (left + right) // 2
            
            if target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
            else:
                return [self.find_left(nums, target, 0, mid), self.find_right(nums, target, mid, len(nums)-1)]
        
        return[-1,-1]
    
    def find_left(self, nums, target, left, right):
        
        while (left < right):
            mid = (left + right) // 2
            
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid-1] < target:
                return mid
            else:
                right = mid - 1
                
        return left   
    
    def find_right(self, nums, target, left, right):
        
        while (left < right):
            mid = (left + right) // 2
            
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid+1] > target:
                return mid
            else:
                left = mid + 1
        
        return right
    
    