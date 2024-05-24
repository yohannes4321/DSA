class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        for i in s:
            if i !=']':
                stack.append(i)
            else:
                string=""
                while stack[-1]!='[':
                    
                    string=stack.pop()+string
                #to pop the '['
                stack.pop()
                number=""
                while stack and stack[-1].isdigit():
                    number=stack.pop()+number
                string_mul=string*int(number)
                stack.append(string_mul)
        return ''.join(stack)