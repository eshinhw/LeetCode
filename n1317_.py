

def getNoZeroIntegers(n: int) -> List[int]:
    
    digits = []

    k = 1

    while (n - k >= 10):

        k += 1


    digits.append(k)
    digits.append(n-k)

    return digits