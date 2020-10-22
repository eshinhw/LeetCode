
class Solution:
    def numIdenticalPairs(self, nums) -> int:
        
        sizeMapping = []
        
        
        
        count = 0
        increment = 0
        
        for i in range(1,len(nums)):
            
            if i == 1:
            
                sizeMapping.append((i,count))
            else:
                sizeMapping.append((i,sizeMapping[i-1][1]+increment))
            
            increment += 1        
        
        print(sizeMapping)
        
        # numIndex = {}
        
        # for i in range(len(nums)):
            
        #     if str(nums[i]) in numIndex:
        #         numIndex[str(nums[i])].append(i)
        #     else:
        #         numIndex[str(nums[i])] = [i]
        
        # print(numIndex)
        
        # total = 0
        
        # print(numIndex.values())
        
        # for indexList in numIndex.values():
        #     indexList = list(indexList)
            
        #     if len(indexList) > 1:
        #         length = str(len(indexList))
        #         total = total + sizeMapping[length]

                
        # print(total)
        

                
            
            



s = Solution().numIdenticalPairs([1,1,1,1])
        
        