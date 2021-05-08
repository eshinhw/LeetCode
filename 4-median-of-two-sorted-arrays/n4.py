from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:


        if nums1 == [] and nums2 == []:
            return 0

        if nums1 == [] and len(nums2) == 1:
            return nums2[0]

        if len(nums1) == 1 and nums2 == []:
            return nums1[0]

        merged = []

        i = 0
        while (len(nums1) > 0 and len(nums2) > 0):
            print(nums1[i], nums2[i])
            if nums1[i] > nums2[i]:
                merged.append(nums2[i])
                merged.append(nums1[i])
            if nums1[i] < nums2[i]:
                merged.append(nums1[i])
                merged.append(nums2[i])

            if nums1[i] == nums2[i]:
                merged.append(nums1[i])
                merged.append(nums2[i])
            nums1.pop(0)
            nums2.pop(0)




        if len(nums1) != 0:
            merged.extend(nums1)

        if len(nums2) != 0:
            merged.extend(nums2)

        print(merged)

        if len(merged) % 2 == 0:

            idx = int(len(merged) / 2)

            return (merged[idx-1] + merged[idx]) / 2

        else:
            idx = int(len(merged) / 2)

            return merged[idx]


x = Solution()

print(x.findMedianSortedArrays([1,2], [3,4]))