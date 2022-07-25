class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        res.append([])
        for i in nums:
            j = 0
            l = len(res)
            while j < l:
                res.append(res[j] + [i])
                j += 1
        return res
            
