class Solution:
    def dailyTemperatures(self, nums: List[int]) -> List[int]:
        # decreasing montonic
        # stack=[]
        # dict_t={}
        # for i in range(len(nums)):
        #     while stack and nums[i]>nums[stack[-1]]:
        #         dict_t[nums[stack.pop()]] = i - stack[-1]
        #     stack.append(i)
        # print(dict_t)
        stack = []
        dict_t = {}
        result=[0]*len(nums)
        for i in range(len(nums)):
            
            while stack and nums[i] > nums[stack[-1]]:
                prev=stack.pop()
                result[prev] = i - prev
            stack.append(i)

        return result
        print(stack)
        print(dict_t)
        for i in range(len(nums)):
            result[i]+=dict_t.get(nums[i],)
        
        return result

        
