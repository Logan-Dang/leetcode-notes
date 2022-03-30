from typing import Optional, List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def swapPairs(head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: 
            return head
        
        current = head
        next = current.next
        
        current.next = next.next
        next.next = current
        head = next
        
        prev = current
        current = current.next
        if not current:
            return head
        next = current.next
        while next:
            prev.next = next
            current.next = next.next
            next.next = current
            prev = current
            current = current.next
            if not current:
                return head
            next = current.next
        return head