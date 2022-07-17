# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        return self.inorderRecurse(root, res)
    def inorderIter(self, root):
        # O(n)
        if not root: return None
        res = []
        stack = [root]
        checked = {root}
        current = root
        while stack:
            if current.left and current.left not in checked:
                stack.append(current)
                current = current.left
            elif current.right and current.right not in checked:
                res.append(current.val)
                checked.add(current)
                current = current.right
            else:
                res.append(current.val)
                checked.add(current)
                current = stack.pop()
        return res
        
            
    def inorderRecurse(self, root, res):
        # O(n)
        if not root: return None
        self.inorderRecurse(root.left, res)
        res.append(root.val)
        self.inorderRecurse(root.right, res)
        return res
