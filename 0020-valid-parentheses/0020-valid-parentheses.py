class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        hash_map={')':'(', '}':'{', ']' :'['}
        for i in s :
            if i in hash_map:# only the closing partenssis is the key of the hashmap so if found in hash map it is closed parthiesis 
            # this is for the closing breackts
                if stack and stack[-1]==hash_map[i]:
                    stack.pop()
                else:

                    return False
            else:
                stack.append(i)
        if stack: 
            return False
        else:
            return True