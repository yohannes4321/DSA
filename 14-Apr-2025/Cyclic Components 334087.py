# Problem: Cyclic Components - https://codeforces.com/problemset/problem/977/E

n,m=map(int,input().split())
adj_list=[[] for _ in range(n)]
visted=set()
for _ in range(m):
    src,des=map(int,input().split())
    adj_list[src-1].append(des)
    adj_list[des-1].append(src)
def dfs(node,component):
    visted.add(node)
    component.append(node)
    for neighbour in adj_list[node-1]:
        if neighbour not in visted:
            dfs(neighbour,component)
count=0
for i in range(1,n+1):
    if i not in visted:
        component=[]
        cyclic=True
        dfs(i ,component)
        if len(component) <3:
            cyclic=False
        for j in component :
            if len(adj_list[j-1])!=2:
                cyclic=False 
        if cyclic==True:
            count+=1
print( count)