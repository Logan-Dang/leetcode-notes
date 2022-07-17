# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.invertRecurse(root)
            
    # O(n)
    def invertBFS(self, root):
        if not root: return None
        queue = [root]
        while queue:
            current = queue.pop(0)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
            current.left, current.right = current.right, current.left
        return root
        
    # O(n)
    def invertDFS(self, root):
        def invert(root):
            inverted.add(root)
            root.left, root.right = root.right, root.left
            return root
        
        if root:
            stack = [root]
            inverted = set()
            current = invert(root)
            while stack:
                if not (current.left or current.right):
                    current = stack.pop(-1)
                elif current.left and current.left not in inverted:
                    stack.append(current)
                    current = invert(current.left)
                elif current.right and current.right not in inverted:
                    stack.append(current)
                    current = invert(current.right)
                else:
                    current = stack.pop(-1)
            return root    
    
    # O(n)
    def invertRecurse(self, root):
        if root:
            root.left, root.right = root.right, root.left
            self.invertTree(root.left)
            self.invertTree(root.right)
            return root
