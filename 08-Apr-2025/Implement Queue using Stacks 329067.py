# Problem: Implement Queue using Stacks - https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue:

    def __init__(self):
        self.stack = []
        

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        inplace = []
        for i in range(1, len(self.stack)):
            inplace.append(self.stack[i])
        
        x = self.stack[0]
        self.stack = inplace

        return x
     
    def peek(self) -> int:
        return self.stack[0]

    def empty(self) -> bool:
        return not self.stack


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()