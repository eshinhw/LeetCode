from typing import List

class Solution1:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # if len(nums2) == 0, no need to change with nums1
        if n == 0:
            return None
        
        else:
            j = 0
            for i in range(m, len(nums1)):
                nums1[i] = nums2[j]
                j += 1
        
        nums1.sort()

class Solution2:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        
        """
        if len(nums1)==0:
            return nums2
        elif len(nums2)==0:
            return nums1
        
        res = []
    
        for i in range(m):
            res.append(nums1[i])
        
        for i in range(len(nums2)):
            res.append(nums2[i])
            
        
        res.sort()
        for i in range(len(nums1)):
            nums1[i] = res[i]
            


        

        


