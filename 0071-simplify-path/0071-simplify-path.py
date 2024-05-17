class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        my_st=path.split('/')
        
        for i in my_st:
            if stack and i=='..':
                stack.pop()
            elif i !='.' and i !="" and i !="..":
                stack.append(i)
        return "/"+ "/".join(stack)