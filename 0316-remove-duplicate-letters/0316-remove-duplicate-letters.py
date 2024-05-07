class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
       # first is stack is monotonically increasing because with lexicorgraphical order
    # if the stack[-1] before we pop() we have to chaeck if it does occur in the future unless we donot pop() it also contradict we increading monotonic stack
        # when we pop() we must change the seen to false
    # before we add to stack we have to check if the seen is false becuase it is uniq charcters
        freq=[0]*26
        for i in range(len(s)):
            freq[ord(s[i])- ord('a')] +=1 # from 0 to 25 
        seen=[False] *26
        stack=[]
        for i in range(len(s)):
            if seen[ord(s[i])- ord('a')]:
                freq[ord(s[i]) -ord('a')] -=1
                continue
            while stack and stack[-1] > s[i] and freq[ord(stack[-1])-ord('a')] >0:
                seen[ord(stack[-1])- ord('a')] = False
                stack.pop()
            stack.append(s[i])
            freq[ord(s[i])-ord('a')]-=1
            seen[ord(s[i])-ord('a')]=True
        return ''.join(stack)