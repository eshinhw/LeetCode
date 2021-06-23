
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        for _ in range(k):            
            nums.insert(0, nums.pop())
            

    def rotateV2(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """        
        
        k = k % len(nums)
        if k == 0:
            return nums
        
        nums[:k], nums[k:] = nums[-k:], nums[:-k]
        
      
