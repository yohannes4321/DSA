class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        value=path.split('/')
        for i in value :
            if i=='' or i =='.':
                continue
            elif i =='..':
                if stack :
                    stack.pop()
            else:
                stack.append(i)
        return '/'+ '/'.join(stack)
 