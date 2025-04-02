# Problem: Limited Repainting - https://codeforces.com/contest/2070/problem/C

import sys
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right, insort
import random
import math
from heapq import heapify, heappush, heappop
 
def solve():
    n,k = map(int, sys.stdin.readline().split())
    s = input()
    penalty = list(map(int, sys.stdin.readline().split()))
    def check(mid):
        last = "R"
        cnt = 0
        for i in range(n):
            if penalty[i] > mid:
                if s[i] == "B" and last == "R":
                    cnt += 1
                last = s[i]
        return cnt <= k
    
                 
 
    l,r = 0,max(penalty)
 
    while l <= r:
        mid = (l + r) // 2
        if check(mid):
            r = mid - 1
        else:
            l = mid + 1
    return l
    
for _ in range(int(sys.stdin.readline().strip())):  
    print(solve())