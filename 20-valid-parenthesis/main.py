class Solution:
    def isValid(self, s: str) -> bool:
        # O(n)
        d = {'}': '{', ']': '[', ')': '('}
        stack = []
        for c in s:
            if c in d:
                if not stack or not stack[-1] == d[c]:
                    return False
                stack.pop(-1)
            else:
                stack.append(c)
        return not stack
