

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minimum = float('inf')

    def push(self, x: int) -> None:
        
        self.stack.append(x)
        
        if x < self.minimum:
            self.minimum = x        

    def pop(self) -> None:
        
        if len(self.stack) > 0:
            p = self.stack.pop()
        
        if len(self.stack) == 0:
            self.minimum = float('inf')
        
        elif len(self.stack) > 0 and p == self.minimum:
            self.minimum = min(self.stack)          

    def top(self) -> int:
        return self.stack[-1]        

    def getMin(self) -> int:
        return self.minimum

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
        
    
    
    