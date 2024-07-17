# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

df = defaultdict(lambda: -1)
b = []
n,m = input().split()

for i in range(1, int(n)+1):
    vl = input()
    if vl in df:
        df[vl] += str(i) + ' '
    else:
        df[vl] = str(i) + ' '

for _ in range(int(m)):
    b.append(input())

for j in b:
    print(df[j])
