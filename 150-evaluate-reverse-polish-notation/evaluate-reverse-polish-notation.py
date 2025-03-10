class Solution:
    def evalRPN(self, nums: List[str]) -> int:
        stack=[]
        for i in range(len(nums)):
            if nums[i] not in "+-*/":
                stack.append(int(nums[i]))
            else:
                if nums[i]=="*":
                    b=stack.pop()
                    a=stack.pop()
                    stack.append(int(a*b))
                elif nums[i]=="/":
                    b=stack.pop()
                    a=stack.pop()
                    stack.append(int(a / b))
                elif nums[i]=="+":
                    b=stack.pop()
                    a=stack.pop()
                    stack.append(int(a+b))
                elif nums[i]=="-":
                    b=stack.pop()
                    a=stack.pop()
                    stack.append(int(a-b))
            #print(stack)
        return stack[0] 
                 
            