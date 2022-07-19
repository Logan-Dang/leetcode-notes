# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = current = ListNode(next = head)
        while current.next and current.next.next:
            next = current.next
            mext = current.next.next.next
            current.next = current.next.next
            current.next.next = next
            next.next = mext
            current = next
        return dummy.next
