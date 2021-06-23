
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
            
        
        for i in range(len(numbers)):
            # for every element, 
            # find remainder from target (the diff between current element and target)
            remainder = target - numbers[i]
            # check if remainder is in numbers
            if remainder in numbers:
                # if remainder is in numbers, 
                # return i+1 as the instruction suggests to start from index 1
                return [i+1, numbers.index(remainder,i+1)+1]



    def twoSumBinarySearch(self, numbers: List[int], target: int) -> List[int]:
        
        low, high = 0, len(numbers) - 1
        
        while (low < high):
            
            current_sum = numbers[low] + numbers[high]
            
            if target == current_sum:
                return [low + 1, high + 1]
            
            elif current_sum > target:
                high -= 1
            
            else:
                low += 1
                
    
    