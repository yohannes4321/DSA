# Problem: Employee Importance - https://leetcode.com/problems/employee-importance/

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id_value: int) -> int:
        total=0
        visted=set()
        graph={}
        def dfs(_id):
            nonlocal total
            if _id==None:
                return 
            visted.add(_id)
            for i in graph[_id][1]:
                if i not in visted:
                    total+=graph[i][0]
                    dfs(i)
        for i in employees:
            id_ = i.id
            importance = i.importance
            subordinates = i.subordinates
            # total+=importance
            graph[id_]=(importance,subordinates)
        print(graph)
        for key in graph:
            if key==id_value:
                dfs(key)
                total+=graph[key][0]
        return total