# Problem: Fizz Buzz - https://leetcode.com/problems/fizz-buzz/description/

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        list_t=[]
        for i in range(1,n+1):
            
            if i %3==0 and i%5==0:
                list_t.append("FizzBuzz")
            elif i %3==0:
                list_t.append("Fizz")
            elif i %5==0:
                list_t.append("Buzz")
            else:
                list_t.append(str(i))
        return list_t     