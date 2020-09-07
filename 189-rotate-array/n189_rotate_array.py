

def rotate(nums, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        
        
        
        for _ in range(k):
            
            nums.insert(0, nums.pop())
        

        

rotate([1,2,3,4,5,6,7], 3)