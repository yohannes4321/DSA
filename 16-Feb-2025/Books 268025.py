# Problem: Books - https://codeforces.com/contest/279/problem/B

n,m=map(int,input().split())
nums=list(map(int,input().split()))
def Book(nums,n,m):
    sum_value=0
    left=0
    max_length=0
    for i in range(n):
        sum_value+=nums[i]
        while sum_value >m:
            sum_value-=nums[left]
            left+=1
        max_length=max(max_length,i-left+1)
            

    return max_length
print(Book(nums,n,m))