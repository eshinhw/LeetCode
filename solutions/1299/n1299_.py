

def replaceElements(arr):
    
    maxIdx = -1
    
    
    for i in range(len(arr)):
        maxVal = 0
        for j in range(i+1,len(arr)):
            
            if arr[j] >= maxVal:
                maxVal = arr[j]
                maxIdx = j
        
        arr[i] = arr[maxIdx]
        
    arr[-1] = -1
    
    print(arr)
    


replaceElements([17,18,5,4,6,1])            