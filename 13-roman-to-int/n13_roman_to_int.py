"""
13. Roman to Integer

Whenever the previous letter is less than the current letter, we subtract 2 times of the value of previous letter.

IV = 1 + 5 - 2(1) = 4

IX = 1 + 10 -2(1) = 9

X L I X = 10 + 50 - 2(10) + 1 + 10 - 2(1) = 40 + 9 = 49

Solution Review

- Used two pointers to keep track of current value and previous value
- Whenever previous value is smaller than current value, we subtract 2 * prev from total after adding current value.

"""

def romanToInt(s: str) -> int:
    
    
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    prev = 0
    curr = 0
    total = 0
    
    for i in range(0, len(s)):
        
        curr = roman[s[i]]
        
        if prev < curr:
            total = total + curr - 2 * prev
        else:
            total = total + curr
            
        prev = curr
        
    return total


print(romanToInt('XLIX'))
        
print(romanToInt('IV'))
