class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        paths=path.split('/')
        for i in paths:
            if i =="" or i=='.':
                continue
            if i =='..':
                if stack:
                    stack.pop()
            else:
                stack.append(i)
        return "/" + '/'.join(stack)