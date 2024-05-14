# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #the idea is if the next of the current is the same as the current one we gona delete the next one and we must connect to the next .next even if they are abosolutly the same because the current is not changing the next new node even the same as the current node in the second time in the while we gona chechk and delete ###$#one tip the current is not updating 
        #we have the cahnce to cheack for the next one if it is the same we gona delete it 
        # if not the same we gona updata the current pointer
        current=head
        while current:
            while current.next and current.next.val == current.val:
                current.next=current.next.next
                # this is loop so it goes as there is no duplicate
                # when the loop terminate it cheaks the current is not equal to None so
                #it change the current to null then it ends why not it not end in current .next.val because there is no statment in while loop in current .next on ly to cheack for equlliy with the current not other meaning besides t his intiution 
            current=current.next
        return head