
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        
        outList = []
        
        count = 1
        
        while (count <= n):
            # multiple of both three and five            
            if count % 15 == 0:
                outList.append("FizzBuzz")            
            # multiple of three
            elif count % 3 == 0:
                outList.append("Fizz")
            # multiple of five
            elif count % 5 == 0:
                outList.append("Buzz")
            else:
                outList.append(str(count))
            
            count += 1
        
        return outList
