

def multiples():
    
    sumThree = 0
    sumFive = 0
    sumFifteen = 0
    
    k = 1
    
    while True:
        
        multipleThree = 3 * k        
        
        if multipleThree < 1000:
            sumThree += multipleThree
            k += 1
        else:
            break
    
    k = 1
        
    while True:
        multipleFive = 5 * k
        
        if multipleFive < 1000:
            sumFive += multipleFive
            k += 1
        else:
            break
        
    k = 1
        
    while True:
        multipleFift = 15 * k
        
        if multipleFift < 1000:
            sumFifteen += multipleFift
            k += 1
        else:
            break        
    
    return sumThree + sumFive - sumFifteen
    
        
        
        
    
    
    

multiples()
    
    