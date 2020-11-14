class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        
        # Base case: numRows == 0
        
        if (numRows == 0):
            return []
        
        # If input numRows > 0
        # output list containing row lists starts with one element in it which is [1]        
        triangle = [[1]]
        
        for i in range(1,numRows):
            
            prev_row = triangle[i-1]
            current_row = []
            # Every row has 1 as the first element
            current_row.append(1)
            
            # Elements between the first and the last are determined
            # based on values from a previous row            
            for j in range(1,i):
                current_row.append(prev_row[j-1] + prev_row[j])
                
            # Every row has 1 as the last element
            current_row.append(1)
            
            # current row should be added our output list
            triangle.append(current_row)
        
        return triangle
        
        
        