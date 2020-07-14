
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
            
        
        for i in range(len(numbers)):
            
            remainder = target - numbers[i]
            if remainder in numbers:
                return [i+1, numbers.index(remainder,i+1)+1]