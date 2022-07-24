# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = ListNode()
        prev.next = current = ahead = head
        for i in range(n):
            ahead = ahead.next
        while ahead:
            current = current.next
            ahead = ahead.next
            prev = prev.next
        prev.next = current.next
        if current != head: return head
        return prev.next
