def findNumbers(nums) -> int:
    
    if not nums:
        return 0
    
    even_count = 0
    
    for i in range(len(nums)):
        
        if len(str(nums[i])) % 2 == 0:
            even_count += 1
    
    return even_count
            

        
    



findNumbers([12,345,2,6,7896])        


    