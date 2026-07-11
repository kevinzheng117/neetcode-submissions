# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        curr = head
        index = 1
        prev = None
        
        while index < left:
            prev = curr
            curr = curr.next
            index += 1
    
        newNext = None
        while index <= right:
            new = ListNode(curr.val, newNext)
            if index == left:
                end = new
            newNext = new
            curr = curr.next
            index += 1
        
        if left != 1:
            prev.next = new
            end.next = curr
            return head
        else:
            end.next = curr
            return new