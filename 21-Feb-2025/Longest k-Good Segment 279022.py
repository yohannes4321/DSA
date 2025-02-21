# Problem: Longest k-Good Segment - https://codeforces.com/problemset/problem/616/D

from collections import defaultdict
n, k = map(int, input().split())
arr = list(map(int, input().split()))
start = 0
end = 0
left = 0
res_max = 0
distinct = 0
count_dict = defaultdict(int)
for right in range(n):
    cur_elem = arr[right]
    if count_dict[cur_elem] == 0:
        distinct += 1
    count_dict[cur_elem] += 1
    
    while distinct > k:
        erl_ele = arr[left]
        count_dict[erl_ele] -= 1
        if count_dict[erl_ele] == 0:
            distinct -= 1
        left += 1
    
    cur_max = right - left + 1
    if cur_max > res_max:
        res_max = cur_max
        start = left
        end = right

print(start + 1, end + 1)