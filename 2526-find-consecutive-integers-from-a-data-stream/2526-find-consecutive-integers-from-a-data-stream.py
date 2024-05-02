from collections import deque

class DataStream:
    def __init__(self, value: int, k: int):
        self.value=value
        self.k=k
        self.q=deque()
        self.counter=0
    def consec(self, num: int) -> bool:
        if len(self.q)==self.k:
            if self.q[0]==self.value:
                self.counter-=1
            self.q.popleft()
        self.q.append(num)
        if num==self.value:
            self.counter+=1
        return self.counter==self.k