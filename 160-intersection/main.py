from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Naive time O(n + m) and space O(n) solution


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        s = set()
        current = headA
        while current:
            s.add(current)
            current = current.next
        current = headB
        while current:
            if current in s:
                return current
            current = current.next
        return None

    # Insane time O(n + m) and space O(1) solution
    # Rewritten from https://leetcode.com/problems/intersection-of-two-linked-lists/discuss/49785/Java-solution-without-knowing-the-difference-in-len!
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
          if not (headA and headB):
              return None
          a = headA
          b = headB
          while a != b:
              a = headB if not a else a.next
              b = headA if not b else b.next
          return a
