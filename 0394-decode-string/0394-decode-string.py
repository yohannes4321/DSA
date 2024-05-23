class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        for i in s:
            if i != ']':
                stack.append(i)
            else:
                string=""
                while stack[-1] !='[':
                    
                    string=stack.pop()+string
                stack.pop()
                # this for number 
                number=""
                while stack and stack[-1].isdigit():
                    number=stack.pop()+number
                
                repeting_string=int(number)*string
                stack.append(repeting_string)
        return ''.join(stack)