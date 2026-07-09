# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# null 0 -> 1 -> 2 -> 3 -> null
# null <- 0 <- 1 <- 2 <- 3  null
#                        p    c,n

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None: return head
        prev, curr = None, head
        while curr:
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex
        return prev