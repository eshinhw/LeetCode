"""

20. Valid Parentheses

Ordering matters!

After opening, there must be the same type of closing shown up

STACK is helpful to solve this problem.

1. Everytime we see the opening, we push into stack

2. Everytime we see the closing, it needs to match the one at the top of stack

3. If it doesn't match, not valid!

4. In the end, the stack must be empty

"""

def isValid(s: str) -> bool:
    
    
    st = []

    
    for ch in s:
        
        if ch == '(' or ch == '[' or ch == '{':
            
            st.append(ch)
        
        elif ch == ')' and len(st) > 0 and st[len(st)-1] == '(':
            
            st.pop()
        
        elif ch == ']' and len(st) > 0 and st[len(st)-1] == '[':
            
            st.pop()
                
        elif ch == '}' and len(st) > 0 and st[len(st)-1] == '{':
            
            st.pop()
        
    
    return len(st) == 0
        
        


print(isValid("()[]{}"))