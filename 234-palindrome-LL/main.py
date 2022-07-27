# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head.next: return True
        slow = fast = head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            slow.next, prev, slow = prev, slow, slow.next
        if not fast:
            fast = slow
        else:
            fast = slow.next
        slow = prev
        while fast or slow:
            if fast.val != slow.val: return False
            fast = fast.next
            slow = slow.next
        return True
