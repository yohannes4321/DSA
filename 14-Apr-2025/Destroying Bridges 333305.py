# Problem: Destroying Bridges - https://codeforces.com/problemset/problem/1944/A

n= int(input())
for _ in range(n):
    n,k=map(int,input().split())
    if k>=n-1:
        print(1)
    else:
        print(n)        