class ListNode:
    def __init__(self,val,next=None,prev=None):
        self.val=val
        self.prev=prev
        self.next=next
class BrowserHistory:
     
    def __init__(self, homepage: str):
        node = ListNode(homepage)
        self.head=node
        self.Tail=node
        

    def visit(self, url: str) -> None:    
        self.Tail.next=ListNode(url)
        self.Tail.next.prev = self.Tail
        self.Tail=self.Tail.next

    def back(self, steps: int) -> str:
        while steps>0 and self.Tail.prev:
            steps-=1
            self.Tail=self.Tail.prev
        return self.Tail.val

    def forward(self, steps: int) -> str:
        while steps>0 and self.Tail.next:
            steps-=1
            self.Tail=self.Tail.next
        return self.Tail.val
         
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)