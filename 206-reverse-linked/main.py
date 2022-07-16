# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.reverseRecurse(head)
    
    def reverseIter(self, head):
        if not (head and head.next): return head
        current = head.next
        head.next = None
        prev = head
        while current.next:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        current.next = prev
        return current
    
    def reverseRecurse(self, head, prev = None):
        if not head: return None
        if not head.next:
            head.next = prev
            return head
        temp = head.next
        head.next = prev
        return self.reverseRecurse(temp, head)
            
            
