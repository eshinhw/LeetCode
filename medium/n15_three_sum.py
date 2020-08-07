

class Solution:
    def threeSum(self, nums):
        
        output = []
        
        nums.sort()
        
        #print(nums)
        
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            
            left = i + 1
            right = len(nums) - 1
            
            while (left < right):
            
                sumTotal = nums[i] + nums[left] + nums[right]
                
                if sumTotal == 0:
                    
                    output.append([nums[i], nums[left], nums[right]])
                    while nums[left] == nums[left+1]:
                        left += 1
                    while nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
                
                elif sumTotal < 0:
                    
                    left += 1
                
                else:
                    
                    right -= 1
            
        return output
        


a = Solution()
print(a.threeSum([-1, 0, 1, 2, -1, -4]))

print("Hello")
            
            