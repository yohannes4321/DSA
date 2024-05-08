class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #we cannot use hashmap because there isnot unque
        stack=[]
        res=[0]*len(temperatures)
        hash_map={value:key for key ,value in enumerate(temperatures)}
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                n=stack.pop()# this is index value 
                res[n]=i-n
            stack.append(i)
        return res
            