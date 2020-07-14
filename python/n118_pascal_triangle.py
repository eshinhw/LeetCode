
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        if numRows == 0:
            return []
        
        else if numRows == 1:
            return [ [1] ]
        
        else if numRows == 2:
            return [ [1], [1,1] ]
        
        else:
            output = [ [1], [1,1] ]
            
        for _ in range(numRows-2):
            
        
        