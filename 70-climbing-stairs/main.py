class Solution:
    def climbStairs(self, n: int) -> int:
        self.memo = {}
        return self.climbRecurse(n)
        
    def climbRecurse(self, n):
        if n in {1, 2}: return n
        if n in self.memo:
            return self.memo[n]
        val = self.climbRecurse(n - 1) + self.climbRecurse(n - 2)
        self.memo[n] = val
        return val
