class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        list_t=[]
        
        def search(val,array):
            sum_value=0
            for i in range(len(nums)):
                if val > nums[i]:
                    sum_value +=1
            list_t.append(sum_value)
            return list_t
        for i in range(len(nums)):
            s=search(nums[i],nums)
            print(s)
        return s