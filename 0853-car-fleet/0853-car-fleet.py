class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack=[]
        s=[[p,s] for p ,s in zip(position,speed) ]
        for p,s in sorted(s)[::-1]:# we have put in sorteing order  in reversed 
            stack.append((target-p)/s) # we have append the time in the stack
            if len(stack) >1 and stack[-1] <= stack[-2]: #becuase less time 
                stack.pop()
        return len(stack)
            
    