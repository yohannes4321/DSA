from collections import deque

class RecentCounter:
    def __init__(self):
        self.q=deque()

    def ping(self, t: int) -> int:
        self.q.append(t)
        while t-self.q[0]>3000:
            if self.q:
                self.q.popleft()
        return len(self.q)