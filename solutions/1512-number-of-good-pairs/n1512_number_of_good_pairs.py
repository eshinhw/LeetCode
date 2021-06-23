
class Solution:
    def numIdenticalPairs(self, nums) -> int:
        
        """
        list length    # good pairs     increment
        []             0                0
        [1]            0                0
        [1,2]          1                1
        [1,2,3]        3                2
        [1,2,3,4]      6                3
        [1,2,3,4,5]    10               4
        ...
        """

        # creates a list containing length numbers as indices 
        # and their corresponding number of valid pairs as values
        size = [0] * (len(nums) + 1)
        increment = 0

        for i in range(1,len(nums)+1):

            if i == 1:
                size[i] = 0
            else:
                size[i] = size[i-1] + increment

            increment += 1
            
        # collects index information for each element in a given list

        numIndex = {}

        for i in range(len(nums)):

            if nums[i] in numIndex:
                numIndex[nums[i]].append(i)
            else:
                numIndex[nums[i]] = [i]

        
        # counts the total number of good pairs 
        total = 0

        for indexList in numIndex.values():

            total = total + size[len(indexList)]

        return total






s = Solution().numIdenticalPairs([1,1,1,1])

