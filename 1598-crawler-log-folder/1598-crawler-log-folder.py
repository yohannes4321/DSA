class Solution:
    def minOperations(self, logs: List[str]) -> int:
        res=0
        stack=[]
        for i in range(len(logs)):
            if logs[i]=='../':
                if stack:
                    stack.pop()
                
            elif logs[i]=='./':
                continue
            else:
                stack.append(logs[i])
             
        return len(stack)
            