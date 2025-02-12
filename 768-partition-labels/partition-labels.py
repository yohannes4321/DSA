class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        occur = defaultdict(int)
        for i in range(len(s) - 1 , -1 , -1):
            if s[i] not in occur:
                occur[s[i]] = i
        ans = [0]
        currMax = occur[s[0]]
        for i in range(len(s)):
            currMax = max(currMax , occur[s[i]])
            if currMax == i:
                ans.append(i + 1 - sum(ans))
                print(s[:i+1] , i)

           
        return ans[1:]


