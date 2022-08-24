class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # O(n) time maybe O(n^2) space maybe
        res = []
        def combRecurse(index, sum, current):
            if index >= len(candidates): return
            if sum == 0: 
                res.append(current)
                return
            if sum >= candidates[index]:
                combRecurse(index, sum - candidates[index], current + [candidates[index]])
            combRecurse(index + 1, sum, current)
        combRecurse(0, target, [])
        return res
