# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def flatRecurse(root):
            if not (root and (root.left or root.right)): return root
            left_tail, right_tail = flatRecurse(root.left), flatRecurse(root.right)
            if left_tail:
                left_tail.right = root.right
                root.right = root.left
                root.left = None
            return right_tail or left_tail
        flatRecurse(root)
