from collections import deque
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        queue=deque() 
        visted=set()
        adj_list=[]
        for i in range(len(rooms)):
            # print(i)
            # src,des=i
            adj_list.append(rooms[i])
        # print(adj_list)
        queue.append(0)
        visted.add(0)
        while queue:
            room=queue.popleft()
            for niegh in adj_list[room]:
                # print(niegh)
                if niegh not in visted:
                    queue.append(niegh)
                    visted.add(niegh)
        if (len(adj_list))==len(visted):
            return True
        else:
            return False
