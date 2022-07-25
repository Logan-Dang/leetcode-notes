# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def depth(node):
            nonlocal ans
            if not node: return 0
            left, right = depth(node.left), depth(node.right)
            ans = max(ans, left + right)
            return max(left, right) + 1
        depth(root)
        return ans
                
