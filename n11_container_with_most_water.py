

class Solution:
    def maxArea1(self, height: List[int]) -> int:
        
        maxA = float("-inf")
        
        for i in range(len(height)):
            for j in range(len(height)):
                
                minHeight = min(height[i],height[j])
                maxA = max(maxA, minHeight * (j-i))
        
        return maxA
    
    def maxArea2(self, height: List[int]) -> int:
        
        maxA = float("-inf")
        
        left = 0
        right = len(height) - 1
        
        while (left < right):
            # keep the shorter height as that's the valid one
            minHeight = min(height[left],height[right])
            
            # with the shorter height determined above
            # calculate the area
            maxA = max(maxA, minHeight * (right-left))
            
            # Move the index with shorter height
            # to look for taller one            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return maxA
    
    