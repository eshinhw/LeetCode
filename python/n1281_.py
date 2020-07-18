
def subtractProductAndSum(n: int) -> int:
        
   
    digits = []
    
    str_input = str(n)
    
    print(str_input)
    
    for i in range(len(str_input)):
        digits.append(int(str_input[i]))
    
    
    print(digits)       

    
    product = 1
    total_sum = 0

    
    for i in range(len(digits)):
        
        product = product * digits[i]
        total_sum = total_sum + digits[i]
    
    return product - total_sum



print(subtractProductAndSum(20))