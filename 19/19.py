class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEndLOGAN(self, head: ListNode, n: int) -> ListNode:
        '''
        Keep track of the current node and the node n+1 away. When the other node is null, current.next = current.next.next. O(n) solution
        '''
        dummy = ListNode(val=-1, next=head)
        right = dummy
        left = dummy
        for i in range(n + 1):
            right = right.next
        while right != None:
            right = right.next
            left = left.next
        left.next = left.next.next
        return dummy.next