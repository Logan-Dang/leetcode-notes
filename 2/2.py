class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbersLOGAN(self, l1: ListNode, l2: ListNode) -> ListNode:
        """Strategy: Add l2 to l1, carry the 1 if l1 > 10. Uses recursion. O(n) solution
        """
        if not l1 and not l2:
            return None
        elif not l1:
            if l2.val < 10:
                return l2
            else:
                l2.val -= 10
                if not l2.next:
                    l2.next = ListNode(1, None)
                    return l2
                else:
                    l2.next.val += 1
                    l2.next = self.addTwoNumbersLOGAN(None, l2.next)
                    return l2
        elif not l2:
            if l1.val < 10:
                return l1
            else:
                l1.val -= 10
                if not l1.next:
                    l1.next = ListNode(1, None)
                    return l1
                else:
                    l1.next.val += 1
                    l1.next = self.addTwoNumbersLOGAN(l1.next, None)
                    return l1
        
        l1.val += l2.val
        if l1.val < 10:
            l1.next = self.addTwoNumbersLOGAN(l1.next, l2.next)
        else:
            l1.val -= 10
            if not l1.next:
                l1.next = ListNode(1, None)
                l1.next = self.addTwoNumbersLOGAN(l1.next, l2.next)
            else:
                l1.next.val += 1
                l1.next = self.addTwoNumbersLOGAN(l1.next, l2.next)
        return l1
    
    def addTwoNumbersCORRECT(self, l1, l2):
        carry = 0
        root = n = ListNode(0)
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry, val = divmod(v1+v2+carry, 10)
            n.next = ListNode(val)
            n = n.next
        return root.next