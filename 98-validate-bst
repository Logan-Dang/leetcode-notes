# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validRecurse(node, low = None, high = None):
            if not node: return True
            if low != None and node.val <= low: return False
            if high != None and node.val >= high: return False
            return validRecurse(node.left, low, node.val) and validRecurse(node.right, node.val, high)
        return validRecurse(root.left, high = root.val) and validRecurse(root.right, low = root.val)
