class Solution:
    def reverse(self, x: int) -> int:
        
        # determine negative flag
        
        if x < 0:
            is_neg = True
        else:
            is_neg = False
        
        x = abs(x)
        reverse = 0
        
        while (x != 0):
            reverse = reverse * 10 + (x % 10)
            x = x // 10
        
        # check max boundaries of int
            
        if (reverse < (-(2**31))) or (reverse > (2**31)-1):
            return 0
        
        # if input was negative, return with negative
        # otherwise, return reverse
        
        if is_neg:
            return reverse * (-1)
        else:
            return reverse
        
        
            