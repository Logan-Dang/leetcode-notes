class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        d = {}
        def uniqueRecurseTopDown(m, n):
            if m == 1 or n == 1: return 1
            if (m, n) in d: return d[(m, n)]
            res = uniqueRecurseTopDown(m - 1, n) + uniqueRecurseTopDown(m, n - 1)
            d[(m, n)] = res
            return res
        
        
        return uniqueRecurseTopDown(m, n)
