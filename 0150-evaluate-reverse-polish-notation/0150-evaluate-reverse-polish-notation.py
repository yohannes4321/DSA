class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            if i =='+':
                stack.append(int(stack.pop())+int(stack.pop()))
            elif i=='*':
                stack.append(int(stack.pop())*int(stack.pop()))
            elif i=='-':
                a,b=stack.pop() ,stack.pop()
                stack.append(int(b)-int(a))
            elif i =='/':
                a,b=stack.pop(),stack.pop()
                stack.append(int(b)/ int(a))
            else:
                stack.append(i)
        return int(stack[0])