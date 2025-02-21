# Problem: Karen and Coffee - https://codeforces.com/contest/816/problem/B

n,k,q = map(int,input().split())
recipe = []
for _ in range(n):
    a = list(map(int,input().split()))
    recipe.append(a)
array = [0] * (200002)
for r in recipe:
    array[r[0]] +=1
    array[r[1]+1] -=1
binary = [0] * (200002)
for i in range(1,len(array)):
    array[i] += array[i-1]
    if array[i] >= k:
        binary[i] = 1
for i in range(1,len(array)):
    binary[i] += binary[i-1]
for __ in range(q):
    question = list(map(int,input().split()))
    b = question[1]
    a = question[0] - 1
    if a > 0:
        print(binary[b] - binary[a])
    else:
        print(binary[b])