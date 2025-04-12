# Problem:  Network Topology - https://codeforces.com/problemset/problem/292/B

import sys,threading
imput=lambda :sys.stdin.readline().strip()
n,m=map(int,input().split())
power_node=[0]*n
how_many_element_power=[0]*n
for _ in range(m):
    #reciving the edges
    j,k=map(int,input().split())
    power_node[j-1]+=1
    power_node[k-1]+=1
for i in power_node:
    how_many_element_power[i-1]+=1
 
if m==n-1 and how_many_element_power[0]==2 and how_many_element_power[1]==n-2:
    print("bus topology")

elif m==n and how_many_element_power[1]==n  :
    print("ring topology")
elif m==n-1 and how_many_element_power[0]==n-1 and how_many_element_power[n-2]==1:
    print("star topology")
else:
    print("unknown topology")
