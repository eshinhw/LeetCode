

class MySolution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        if 0 not in nums:
            return None
        
        for i in range(len(nums)):
            
            if nums[i] == 0:
                nums.remove(0)
                nums.append(0)

