class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        hash_map={")":"(","}":"{","]":"["}
        #the key is the closed parthesisi and value is open
        for i in s:
            if i in hash_map :
                if stack and hash_map[i]==stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        if not stack:
            return True
            