# Problem: Maximum Twin Sum of a Linked List - https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        stack = []

        temp = head
        while temp:
            stack.append(temp.val)
            temp = temp.next

        start = 0
        end = len(stack) - 1
        max_sum = 0

        while start < end:
            max_sum = max(max_sum, stack[start] + stack[end])
            start += 1
            end -= 1

        return max_sum