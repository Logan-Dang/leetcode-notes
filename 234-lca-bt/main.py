# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':        
        stack = [root]
        checked = set()
        res = None
        while stack:
            current = stack[-1]
            
            if not res and current == p:
                res = p
            if not res and current == q:
                res = q
            if res != q and current == q:
                return res
            if res != p and current == p:
                return res
            
            if current.left and current.left not in checked: 
                stack.append(current.left)
                checked.add(current.left)
            elif current.right and current.right not in checked: 
                stack.append(current.right)
                checked.add(current.right)
            else: 
                if stack.pop(-1) == res:
                    res = stack[-1]
