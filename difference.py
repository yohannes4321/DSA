# Enter your code here. Read input from STDIN. Print output to STDOUT
input()
nums=map(int, input().split(" "))
input()
m=map(int, input().split(" "))
print(len(set(nums).difference(set(m))))
